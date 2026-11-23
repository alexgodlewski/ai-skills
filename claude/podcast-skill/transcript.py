#!/usr/bin/env python3
"""Get the words of podcast episodes and videos.

  python3 transcript.py <link> [<link> ...] [--max 5] [--lang en] [--out DIR] [--api]

A link can be: a YouTube video, playlist or channel; an Apple Podcasts episode or show page; a Spotify episode or
show page (found again through the show's public feed); a podcast RSS feed; or a direct audio file.
Order: captions first (no download). Otherwise the audio is downloaded and turned into text on this computer with
faster-whisper. With --api (and OPENAI_API_KEY set) the audio goes to OpenAI instead, which costs money.
With --out DIR every transcript is saved as its own .txt file in DIR. Without it they print to the screen.
"""
import argparse, json, os, re, shutil, ssl, subprocess, sys, tempfile, time, urllib.error, urllib.parse, urllib.request, uuid
import xml.etree.ElementTree as ET

try:   # python.org installs on macOS often ship without certificates: use certifi's when it is there
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where()); CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CTX = ssl.create_default_context()

UA = {"User-Agent": "Mozilla/5.0 (podcast-skill transcript.py)"}
USE_API = False


def fetch(url, limit=50_000_000, headers=None):
    if urllib.parse.urlsplit(url).scheme not in ("http", "https"):
        raise SystemExit(f"Only http(s) links work: {url}")
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read(limit), r.headers.get("Content-Type", "")


def get_json(url):
    return json.loads(fetch(url, 20_000_000)[0].decode("utf-8", "replace"))


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", "", (s or "").lower()).strip()


def feed_items(url):
    """A podcast feed: every episode as (title, audio url), newest first. None when it is not a feed."""
    try:
        body, ctype = fetch(url, 20_000_000)
        if "xml" not in ctype and not body.lstrip().startswith(b"<"):
            return None
        root = ET.fromstring(body)
    except (ET.ParseError, OSError, ValueError):
        return None
    eps = []
    for item in root.iter("item"):
        enc = item.find("enclosure")
        if enc is not None and enc.get("url"):
            eps.append(((item.findtext("title") or "Episode").strip(), enc.get("url")))
    return eps or None


def apple_items(url, n):
    """Apple Podcasts page -> episodes, through Apple's public lookup (no key needed)."""
    show = re.search(r"/id(\d+)", url)
    if not show:
        return None
    ep = re.search(r"[?&]i=(\d+)", url)
    data = get_json(f"https://itunes.apple.com/lookup?id={show.group(1)}&entity=podcastEpisode&limit=200")
    rows = data.get("results", [])
    if ep:
        for r in rows:
            if str(r.get("trackId")) == ep.group(1) and r.get("episodeUrl"):
                return [(r.get("trackName"), r["episodeUrl"])]
        raise SystemExit("That Apple Podcasts episode is not in the newest 200 of the show. Paste the show's RSS feed instead.")
    eps = [(r.get("trackName"), r["episodeUrl"]) for r in rows if r.get("kind") == "podcast-episode" and r.get("episodeUrl")]
    return eps[:n] or None


def spotify_items(url, n):
    """Spotify cannot be downloaded (it is protected). Find the same show's public feed and match by title."""
    html = fetch(url, 2_000_000)[0].decode("utf-8", "replace")
    og = lambda k: (re.search(rf'<meta[^>]+property="og:{k}"[^>]+content="([^"]*)"', html) or [None, ""])[1]
    import html as H
    title, desc = H.unescape(og("title")), H.unescape(og("description"))
    show = (re.search(r"from (.+?) on Spotify", desc) or re.search(r"Listen to (.+?) on Spotify", desc) or [None, ""])[1]
    if "/show/" in url:
        show = show or title
    if not show:
        return None
    res = get_json("https://itunes.apple.com/search?entity=podcast&limit=5&term=" + urllib.parse.quote(show))
    feeds = [r["feedUrl"] for r in res.get("results", []) if r.get("feedUrl") and norm(r.get("collectionName")) == norm(show)]
    if not feeds:
        raise SystemExit(f'Could not find a public feed for "{show}". It may be a Spotify exclusive. Try YouTube for the same episode.')
    eps = feed_items(feeds[0]) or []
    if "/episode/" in url:
        hit = [e for e in eps if norm(e[0]) == norm(title) or (norm(title) and norm(title) in norm(e[0]))]
        if not hit:
            raise SystemExit(f'Found the show, but not the episode "{title}" in its feed.')
        return hit[:1]
    return eps[:n] or None


def caption_text(raw, ext):
    """json3 or vtt captions -> plain text, with the rolling repeats of auto-captions removed."""
    lines = []
    if ext == "json3":
        for ev in json.loads(raw).get("events", []):
            t = "".join(s.get("utf8", "") for s in ev.get("segs", []) or []).replace("\n", " ").strip()
            if t: lines.append(t)
    else:
        for ln in raw.decode("utf-8", "replace").splitlines():
            ln = re.sub(r"<[^>]+>", "", ln).strip()
            if not ln or "-->" in ln or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or ln.isdigit():
                continue
            lines.append(ln)
    out = []
    for ln in lines:
        if not out or ln != out[-1]: out.append(ln)
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def pick_captions(info, lang):
    for pool in (info.get("subtitles") or {}, info.get("automatic_captions") or {}):
        keys = [k for k in pool if k == lang] + [k for k in pool if k.startswith(lang) and k != lang] + [k for k in pool if k.endswith("-orig")]
        for k in keys:
            for f in pool[k]:
                if f.get("ext") in ("json3", "vtt") and f.get("url"):
                    return f["url"], f["ext"]
    return None


def whisper_local(path):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    model = WhisperModel(os.environ.get("WHISPER_MODEL", "base"), device="cpu", compute_type="int8")
    segs, _ = model.transcribe(path, vad_filter=True)
    return " ".join(s.text.strip() for s in segs).strip()


def whisper_api(path, tmp):
    """OpenAI transcription. Files over 25 MB are shrunk first with ffmpeg (mono, 32 kbps)."""
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        return None
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is needed to shrink the audio for the API (brew install ffmpeg)")
    small = os.path.join(tmp, "small.mp3")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", path, "-ac", "1", "-b:a", "32k", small], check=True)
    parts = [small]
    if os.path.getsize(small) > 24_000_000:   # about 100 minutes at 32 kbps: cut into 20 minute pieces
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", small, "-f", "segment", "-segment_time", "1200", "-c", "copy", os.path.join(tmp, "part%03d.mp3")], check=True)
        parts = sorted(os.path.join(tmp, f) for f in os.listdir(tmp) if f.startswith("part"))
    model, texts = os.environ.get("OPENAI_TRANSCRIBE_MODEL", "gpt-4o-mini-transcribe"), []
    for p in parts:
        b = uuid.uuid4().hex
        body = b"".join([
            f'--{b}\r\nContent-Disposition: form-data; name="model"\r\n\r\n{model}\r\n'.encode(),
            f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="a.mp3"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode(),
            open(p, "rb").read(), f"\r\n--{b}--\r\n".encode()])
        req = urllib.request.Request("https://api.openai.com/v1/audio/transcriptions", data=body, headers={
            "Authorization": f"Bearer {key}", "Content-Type": f"multipart/form-data; boundary={b}"})
        with urllib.request.urlopen(req, timeout=600, context=CTX) as r:
            texts.append(json.loads(r.read())["text"].strip())
    return " ".join(texts)


def audio_file(url, tmp):
    import yt_dlp
    opts = {"format": "bestaudio/best", "outtmpl": os.path.join(tmp, "audio.%(ext)s"), "quiet": True, "no_warnings": True, "noprogress": True, "noplaylist": True}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(url, download=True)
        return y.prepare_filename(info)


def one(url, title, lang):
    import yt_dlp
    text = None
    with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True, "skip_download": True, "noplaylist": True}) as y:
        try:
            info = y.extract_info(url, download=False)
        except Exception as e:  # noqa: BLE001  (a direct audio link yt-dlp cannot read still gets transcribed below)
            info = {"title": title, "webpage_url": url}
            print(f"(yt-dlp could not read the page: {str(e)[:120]})", file=sys.stderr)
    title = info.get("title") or title or url
    cap = pick_captions(info, lang)
    for attempt in range(3 if cap else 0):   # YouTube rate-limits caption files (429): wait and retry, then use audio
        try:
            raw, _ = fetch(cap[0]); text = caption_text(raw, cap[1]); break
        except urllib.error.HTTPError as e:
            if e.code != 429: break
            time.sleep(5 * (attempt + 1))
    how = "captions"
    if not text:
        with tempfile.TemporaryDirectory() as tmp:
            try:
                path = audio_file(url, tmp)
            except Exception:  # noqa: BLE001
                body, _ = fetch(url, 500_000_000); path = os.path.join(tmp, "audio.mp3"); open(path, "wb").write(body)
            if USE_API:
                text, how = whisper_api(path, tmp), "OpenAI API"
            else:
                text, how = whisper_local(path), "local whisper"
        if text is None:
            how = "none"
            text = ("[No captions, and no way to turn audio into text. Install the free local model with: "
                    "python3 -m pip install --user faster-whisper   or set OPENAI_API_KEY and use --api]")
    return title, info.get("webpage_url") or url, how, text


def expand(link, n):
    host = urllib.parse.urlsplit(link).netloc.lower()
    if "spotify.com" in host:
        return spotify_items(link, n)
    if "podcasts.apple.com" in host:
        return apple_items(link, n)
    if re.search(r"youtube\.com|youtu\.be", host):
        return None
    return (feed_items(link) or [])[:n] or None


def main():
    global USE_API
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("links", nargs="+"); ap.add_argument("--max", type=int, default=5, help="episodes to read from a feed, show or playlist")
    ap.add_argument("--lang", default="en"); ap.add_argument("--out", help="folder: save one .txt per episode")
    ap.add_argument("--api", action="store_true", help="use the OpenAI API (OPENAI_API_KEY) instead of local whisper when there are no captions")
    a = ap.parse_args(); USE_API = a.api
    try:
        import yt_dlp
    except ImportError:
        raise SystemExit('yt-dlp is missing. Install it with: python3 -m pip install --user --upgrade "yt-dlp[default]" certifi')
    if a.out: os.makedirs(a.out, exist_ok=True)
    count = 0
    for link in a.links:
        try:
            items = expand(link, a.max)
            if items is None:
                with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True, "extract_flat": "in_playlist", "skip_download": True}) as y:
                    info = y.extract_info(link, download=False)
                if info.get("_type") == "playlist":
                    items = [(e.get("title"), e.get("url") or f"https://www.youtube.com/watch?v={e['id']}") for e in (info.get("entries") or [])][:a.max]
                else:
                    items = [(info.get("title"), link)]
        except SystemExit as e:
            print(f"# {link}\n[Could not use this link: {e}]\n"); continue
        except Exception as e:  # noqa: BLE001
            print(f"# {link}\n[Could not use this link: {str(e)[:200]}]\n"); continue
        for title, url in items:
            count += 1
            try:
                t, u, how, text = one(url, title, a.lang)
            except Exception as e:  # noqa: BLE001  (one bad episode never stops the rest)
                t, u, how, text = title or url, url, "none", f"[Could not read this one: {str(e)[:200]}]"
            doc = f"# {t}\n{u}\n(source of the words: {how})\n\n{text}\n"
            if a.out:
                fn = os.path.join(a.out, f"{count:02d}-{re.sub(r'[^A-Za-z0-9]+', '-', t)[:60].strip('-')}.txt")
                open(fn, "w", encoding="utf-8").write(doc); print(f"{fn}  ({len(text.split())} words, from {how})")
            else:
                print(doc)
            sys.stdout.flush()


if __name__ == "__main__":
    main()
