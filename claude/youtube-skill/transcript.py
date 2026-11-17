#!/usr/bin/env python3
"""Print the transcript of a YouTube video, a YouTube playlist, a podcast episode or a podcast RSS feed.

  python3 transcript.py <link> [--max 5] [--lang en]

Captions first (fast, no download). No captions: the audio is transcribed on this computer with faster-whisper,
if it is installed (python3 -m pip install --user faster-whisper). Output is plain text, one block per video.
"""
import argparse, json, os, re, ssl, sys, tempfile, time, urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

try:   # python.org installs on macOS often ship without certificates: use certifi's when it is there
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where()); CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    CTX = ssl.create_default_context()

UA = {"User-Agent": "Mozilla/5.0 (transcript.py)"}


def fetch(url, limit=50_000_000):
    if urllib.parse.urlsplit(url).scheme not in ("http", "https"):
        raise SystemExit(f"Only http(s) links work: {url}")
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60, context=CTX) as r:
        return r.read(limit), r.headers.get("Content-Type", "")


def rss_episodes(url, n):
    """A podcast feed: the newest n episodes as (title, audio url)."""
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
    return eps[:n] if eps else None


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


def whisper(path):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    model = WhisperModel(os.environ.get("WHISPER_MODEL", "base"), device="cpu", compute_type="int8")
    segs, _ = model.transcribe(path, vad_filter=True)
    return " ".join(s.text.strip() for s in segs).strip()


def audio_file(url, tmp):
    """Download the audio of a link (yt-dlp handles YouTube and most direct audio links)."""
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
    for attempt in range(3 if cap else 0):   # YouTube rate-limits caption files (429): wait and retry, then fall back to audio
        try:
            raw, _ = fetch(cap[0]); text = caption_text(raw, cap[1]); break
        except urllib.error.HTTPError as e:
            if e.code != 429: break
            time.sleep(5 * (attempt + 1))
    if not text:
        with tempfile.TemporaryDirectory() as tmp:
            try:
                path = audio_file(url, tmp)
            except Exception:  # noqa: BLE001
                body, _ = fetch(url); path = os.path.join(tmp, "audio.mp3"); open(path, "wb").write(body)
            text = whisper(path)
        if text is None:
            text = ("[No captions, and faster-whisper is not installed, so this one could not be read. "
                    "Install it with: python3 -m pip install --user faster-whisper]")
    return f"# {title}\n{info.get('webpage_url') or url}\n\n{text}\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("link"); ap.add_argument("--max", type=int, default=5, help="videos or episodes to read from a playlist or feed")
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()
    try:
        import yt_dlp
    except ImportError:
        raise SystemExit('yt-dlp is missing. Install it with: python3 -m pip install --user --upgrade "yt-dlp[default]" certifi')
    items = rss_episodes(a.link, a.max) if not re.search(r"youtube\.com|youtu\.be", a.link) else None
    if items is None:
        with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True, "extract_flat": "in_playlist", "skip_download": True}) as y:
            info = y.extract_info(a.link, download=False)
        if info.get("_type") == "playlist":
            items = [(e.get("title"), e.get("url") or f"https://www.youtube.com/watch?v={e['id']}") for e in (info.get("entries") or [])][:a.max]
        else:
            items = [(info.get("title"), a.link)]
    for title, url in items:
        try:
            print(one(url, title, a.lang))
        except Exception as e:  # noqa: BLE001  (one bad video never stops the rest)
            print(f"# {title or url}\n{url}\n\n[Could not read this one: {str(e)[:200]}]\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
