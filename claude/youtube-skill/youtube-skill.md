---
name: YouTube Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# YouTube Skill

Give Claude a YouTube video, a playlist or a podcast. It reads the whole thing, learns what it teaches, and saves it as a skill it keeps and uses from then on.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude installs everything and tells you when it is ready.

## Then use it like this

Paste a link and say:

> Watch this, learn what it teaches, and turn it into a skill I can use forever.

For the best result, add what you want to use it for:

> Watch this: [LINK]
> I want to use it for: [WHAT YOU DO, for example writing my sales follow-ups]
> Learn what it teaches and turn it into a skill I can use forever.

Ideas:
- the best sales training on YouTube, so Claude writes your follow-ups that way;
- a creator's hook videos, so Claude writes your hooks that way;
- a whole playlist or channel at once (Claude reads up to 5 videos by default, more if you ask);
- a podcast episode or a podcast feed.

## What it needs

| What | Needed? | Why | Cost |
|---|---|---|---|
| Claude desktop app, Code tab | Yes | This is where it runs | Any paid Claude plan |
| Python 3.10 or newer | Yes | Runs the small transcript tool | Free, Claude installs it if missing |
| yt-dlp | Yes | Reads YouTube captions and podcast audio | Free |
| A speech model (faster-whisper) | Only for videos with no captions, and for podcasts | Turns audio into text on your own computer | Free, about 150 MB, nothing is sent anywhere |

It reads what is **said**, not what is shown on screen. Talking videos, trainings and podcasts work best.

## What gets installed

- `~/.claude/skills/learn-from-video/SKILL.md`: tells Claude how to learn from a video.
- `~/.claude/skills/learn-from-video/transcript.py`: a small tool that gets the words from a link.
- The Python packages `yt-dlp` and `certifi`, plus `faster-whisper` if you say yes to it.

Nothing else on your computer is changed. Every skill Claude learns later goes into its own folder in `~/.claude/skills/`, so you can see it, edit it or delete it.

---

## Setup steps for Claude

Work through these in order. Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to run commands on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This runs in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Find Python 3.10 or newer.** Try `python3 --version`, then `py -3 --version` on Windows. On Windows, ignore a `python` that only opens the Microsoft Store. If none is found, ask first, then install it: `brew install python` on a Mac, or `winget install -e --id Python.Python.3.12` on Windows. If that fails, give them https://www.python.org/downloads/ and wait until they say it is done. In the steps below, `python3` means the command that worked.
3. **Install the transcript packages:** `python3 -m pip install --user --upgrade "yt-dlp[default]" certifi`. If pip refuses because the Python is "externally managed", add `--break-system-packages`, after telling them why.
4. **Ask about the speech model:** "Do you also want videos without captions and podcasts to work? It downloads a free speech model, about 150 MB, and runs on your computer." If they say yes, run `python3 -m pip install --user faster-whisper "av<16"`.
5. **Create the folder** `~/.claude/skills/learn-from-video/` (on Windows: `%USERPROFILE%\.claude\skills\learn-from-video\`), and write the two files below into it exactly as they are.
6. **Test it:** `python3 ~/.claude/skills/learn-from-video/transcript.py "https://www.youtube.com/watch?v=jNQXAC9IVRw"`. It should print a short text about elephants. If it fails with a certificate error on a Mac, run `open "/Applications/Python 3.12/Install Certificates.command"` (use their version number) and test again. For any other error, read it, fix the cause, and test again.
7. **Tell them it is ready.** Then give them the prompt: "Watch this: [LINK]. I want to use it for: [WHAT YOU DO]. Learn what it teaches and turn it into a skill I can use forever."

### File 1: `~/.claude/skills/learn-from-video/SKILL.md`

`````markdown
---
name: learn-from-video
description: Learn from a YouTube video, a YouTube playlist or channel, or a podcast episode or feed, and save what it teaches as a new skill Claude uses from then on. Use when the person pastes a video or podcast link and asks to watch it, learn it, study it, or turn it into a skill.
---

# Learn From a Video

You turn what a video teaches into a skill the person can use again and again.

## 1. Get the words

Run the transcript tool on the link and save its output:

```
python3 ~/.claude/skills/learn-from-video/transcript.py "<link>" --max 5 > /tmp/learn-transcript.txt
```

- On Windows use `py -3` instead of `python3`, and a temp file in the current folder.
- For a playlist, a channel or a podcast feed, `--max` sets how many videos or episodes to read. The default is 5. Ask before going over 10, because each one takes time.
- If a block says it could not be read, tell the person which one and carry on with the rest.
- If the person pasted a transcript instead of a link, use that.

## 2. Read all of it, then pull out what it teaches

Read the whole transcript, not only the start. Write down:

- the method, as steps in the order the video gives them;
- the rules, numbers and limits it states;
- the templates, scripts, phrases and examples it uses, word for word where they matter;
- the mistakes it warns about;
- how to tell that the result is good.

Keep only what the video actually says. Never add steps of your own and present them as the video's.

## 3. Ask one question if you need to

If the person did not say what they want to use it for, ask in one line, for example: "What do you want to use this for: your own posts, client work, something else?"

## 4. Write the new skill

Create `~/.claude/skills/<short-topic-name>/SKILL.md`, with a name in lowercase words joined by hyphens, such as `sales-follow-ups` or `reel-hooks`.

```
---
name: <short-topic-name>
description: <one or two sentences: what it does and the requests it should be used for>
---

# <Title>

Source: <video title> (<link>)

## When to use it
## The steps
## Rules
## Templates and examples
## Check before you hand it over
```

- Write it in plain words, as instructions to yourself.
- Keep it under about 300 lines. Merge repeats and drop filler.
- If a skill on the same topic already exists, ask before you replace it. If they say yes, add to it instead of overwriting it, and list the source of each part.

## 5. Show it working

- Tell the person the skill's name and two example requests that will use it.
- Offer to try it right away on a real task of theirs.
`````

### File 2: `~/.claude/skills/learn-from-video/transcript.py`

`````python
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
`````
