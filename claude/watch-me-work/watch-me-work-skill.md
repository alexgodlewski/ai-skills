---
name: Watch Me Work Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Watch Me Work Skill

Record your screen while you do a task once, and talk through it like you are showing a new hire. Drop the video into Claude Code and say: watch this and turn it into a skill. Claude looks at every step on screen, hears why you do it, and writes the skill. Next time you type one word and it does the whole thing.

## Set it up in 2 minutes

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude installs it and tells you when it is ready.

## Then use it like this

Record your screen with any screen recorder while you do the task once and say out loud what you do and why. Drop the video into Claude Code and type:

> Watch this and turn it into a skill. I want to run it with one word.

## How to record a good one

- Talk like you are training a new hire. Say what you do as you do it.
- Say why you do each step. The reasons are what make the skill good.
- One task per video, from the first click to the last.
- Go a bit slow, and pause on screens you want Claude to read.
- Say what changes between runs, and what you check at the end.
- Close private tabs first. Claude reads everything that shows on screen.
- Any screen recorder works. Save it as mp4 or mov, under about 15 minutes.

## What it needs

| What | Needed? | Why | Cost |
|---|---|---|---|
| Claude desktop app, Code tab | Yes | This is where it runs | Any paid Claude plan |
| ffmpeg | Yes | Pulls the pictures and sound out of your video | Free, Claude installs it if you say yes |
| Python 3.10 or newer | Yes | Runs the small tool | Free, Claude installs it if missing |
| faster-whisper | Yes | Turns your voice into text on your own computer | Free, about 150 MB, nothing is sent anywhere |

Works on Mac, Windows and Linux. It reads the screen from still pictures, so it can miss a click between two frames and will ask you about anything it is not sure of. It writes the skill; whether Claude can run each step later depends on the tools it has, and the skill says which steps it does itself.

## What gets installed

- `~/.claude/skills/watch-me-work/SKILL.md`: tells Claude how to watch a recording and write a skill.
- `~/.claude/skills/watch-me-work/watch.py`: a small tool that pulls frames and a timed transcript from the video.
- ffmpeg and faster-whisper, if they are missing and you say yes.

Every skill Claude writes from your videos goes into its own folder in `~/.claude/skills/`, so you can see it, edit it or delete it.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to run commands on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This runs in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/watch-me-work/` (on Windows: `%USERPROFILE%\.claude\skills\watch-me-work\`) and write the two files below into it exactly as they are. If a SKILL.md is already there, ask before you replace it.
3. **Check the tools now, so the first run is smooth.** Test `ffmpeg -version`, find Python 3.10 or newer (`python3 --version`, or `py -3 --version` on Windows), and test `python3 -c "import faster_whisper"`. For each one that is missing, say plainly what it is and what it costs (nothing), ask, then install it as described in step 2 of the skill below. The speech model itself downloads the first time they run a video.
4. **Test it** if they have a video handy, or make a 10 second one: `python3 ~/.claude/skills/watch-me-work/watch.py "<video>"`. It should print "Done" and make a `-watch` folder next to the video. If it fails, read the error and fix the cause.
5. **Tell them it is ready.** Then give them the steps: record the screen while they do the task once and explain why, drop the file into Claude Code, and type: "Watch this and turn it into a skill. I want to run it with one word."

### File 1: `~/.claude/skills/watch-me-work/SKILL.md`

`````markdown
---
name: watch-me-work
description: Turn a screen recording with spoken narration into a new skill. Pulls frames from the video, writes down what was said with times, lines each spoken step up with what was on screen, and saves a skill in ~/.claude/skills/ that Claude runs next time from one word. Use when the person drops in a screen recording (mp4 or mov) and says watch this, learn this, or turn it into a skill.
---

# Watch Me Work

The person recorded their screen while they did a task once and talked through it like they were showing a new hire. You watch it, listen to it, and write a skill so next time they type one word and you do the task.

## 1. Find the video

- The person drops in or names a screen recording (mp4, mov, mkv, webm). Get its full path.
- If there is no video, say: "Drop the screen recording in here and say: Watch this and turn it into a skill." Do not guess a file.
- If they only want to know how to record one, give them the list in the section "How to record a good one" below.

## 2. Check the tools, and say plainly what you install

You need three things. Check each one and tell the person in one line what you found.

1. **ffmpeg** (pulls the pictures and the sound out of the video). Test with `ffmpeg -version`. If missing, ask first, then install: `brew install ffmpeg` on a Mac, `winget install -e --id Gyan.FFmpeg` on Windows, `sudo apt install ffmpeg` on Linux. On Windows, a new terminal may be needed before it shows up.
2. **Python 3.10 or newer.** Try `python3 --version`, then `py -3 --version` on Windows. Below, `python3` means the command that worked.
3. **A speech model that runs on this computer.** Test with `python3 -c "import faster_whisper"`, then `python3 -c "import whisper"`. If neither works, say plainly: "I need to install faster-whisper. It is free, it downloads a speech model of about 150 MB the first time, and it runs on your computer. Your video is not sent anywhere." Ask, then run `python3 -m pip install --user faster-whisper "av<16"`. If pip says the Python is "externally managed", add `--break-system-packages` after telling them why.

## 3. Run the tool

```
python3 ~/.claude/skills/watch-me-work/watch.py "<video path>"
```

On Windows use `py -3` and `%USERPROFILE%\.claude\skills\watch-me-work\watch.py`.

It makes a folder next to the video, named like the video and ending in `-watch`, with:

- `timeline.md`: each spoken part, its time, its words, and the frames from that moment.
- `frames/`: the pictures, one at every big change on screen and at least one every 5 seconds, at most 60. The file name holds the time, for example `f007_01m12s.jpg`.
- `words.json`: every word with its start and end time.

Useful options: `--every 3` for more frames, `--max-frames 80` for a longer video, `--model small` for a better transcript (slower), `--lang` for a spoken language other than English. The first run downloads the speech model, so it takes a bit longer. A 10 minute video usually takes a few minutes.

If the tool says the video has no sound, tell the person: without their voice you only get what happened, not why. Ask if they want to record it again with narration, or tell you the reasons now in chat.

## 4. Read all of it, then look at the frames

1. Read `timeline.md` from top to bottom. Read the whole thing.
2. Open the frames with the Read tool, in time order. Look at every frame the timeline lists. If there are many, open them in batches of about 10. Do not skip the middle.
3. For each spoken part, write down:
   - **What they did:** the app or site, the button or menu, the thing they typed or picked, what changed on screen. Use only what the frames and the words show.
   - **Why:** the reason they gave, in their own words, as close to word for word as you can.
   - **What they checked:** anything they looked at to decide, or to make sure it worked.
4. Mark anything you are not sure of. A frame shows a screen, not a mouse click. If two readings are possible, or a step happens between frames, write "not sure" and ask in step 5. Never make up a step to fill a gap.
5. Watch for what the person said about things that change: "this one is different when...", "usually", "if it says...". Those become the checks and the questions.
6. Frames may show private things, like names, emails, prices or passwords. Never copy a password, a key or private contact details into the skill. Use a placeholder such as `<client name>` and say what goes there.

## 5. Ask only what you need

Before you write, ask in one short message, and only about real gaps. For example:

- the steps you are not sure of, with the time in the video;
- what changes from one run to the next (a name, a date, a file), so you know what to ask for each time;
- anything they must never do on their own: send, pay, delete, post;
- the one word they want to run it with. Suggest a short name in lowercase, for example `invoices`.

If there are no gaps, skip the questions and say what you will build.

## 6. Write the new skill

Pick the name (lowercase words joined by hyphens). Check `~/.claude/skills/<name>/`. If it already exists, ask before changing it. Never overwrite without a yes.

Create `~/.claude/skills/<name>/SKILL.md` (on Windows: `%USERPROFILE%\.claude\skills\<name>\SKILL.md`) in this shape:

```
---
name: <name>
description: <one or two sentences: what it does, and the words the person says to start it, starting with "<name>">
---

# <Title>

Learned from a screen recording on <date>. Video: <file name>.

## What this does
<one or two lines, and what a finished job looks like>

## What I need from you each time
<the things that change each run: a name, a date, a file, a link. If nothing, write "Nothing. Just run it.">

## Tools and places it uses
<apps, websites, folders, connected tools. Say which ones I can use myself here and which ones I cannot.>

## Steps
1. <what to do, with the exact place on screen, button or field>
   Why: <the reason, in the person's own words>
   Check: <how to see that this step worked>
2. ...

## Checks before I say it is done
<the checks the person said or showed, as a short list>

## Ask the person when
<what to ask if something differs from the recording: a button is missing, a number is outside the usual range, a new kind of case, a login screen>

## Never do without asking
<send, pay, delete, post, or anything the person flagged. Always include this section.>

## Not sure yet
<steps from the video that were unclear, until the person confirms them. Remove this section when empty.>
```

Rules for writing it:

- Plain words, as instructions to yourself. Short sentences.
- Keep the person's reasons. The Why lines are the most valuable part, so quote them as closely as you can.
- Put steps in the order of the video. Merge steps that are one action.
- If you cannot do a step yourself (for example a desktop app you cannot control), say so inside that step and write what you will do instead, such as: do the part you can, then tell the person exactly what to click.
- One page is plenty. Under 150 lines.

## 7. Tell them how to run it

Say all of this:

- "I saved it as `<name>` in `~/.claude/skills/<name>/SKILL.md`."
- "Next time, open Claude Code and type `/<name>`, or say: run <name>." If `/<name>` does not show up in the `/` list, they start a new session.
- A one-line summary of the steps, and the list of things you will ask each time.
- "Open the file any time to read or change it. Or tell me what to change: update <name> so it also does X."
- Anything you are not sure about, and that the first real run is the test: "Watch the first run, and tell me if a step is wrong. I fix the skill once and it stays fixed."

Then offer: "Want to do a first run now, with me asking before anything that sends, pays or deletes?"

## How to record a good one

Share this when they ask, or when the recording was thin.

- Talk like you are training a new hire. Say what you are doing as you do it.
- Say why. "I check the total here because last month the invoice was wrong." The reasons are what make the skill good.
- One task per video. Do the whole task from the first click to the last, once.
- Go a bit slow. Pause on screens you want me to read.
- Say what changes. "Normally it is this, but if the client is new I do that."
- Say what you check at the end, and what you never do without a person looking.
- Any screen recorder works. Use the one on your computer. Save it as mp4 or mov. Keep it under about 15 minutes.
- Close private tabs first. I read everything that shows on your screen.

## Rules

- Say only what the video and the words show. Never invent a step, a button or a reason.
- Never claim you ran the task. This skill only reads the recording and writes a new skill.
- Frames and the transcript stay on this computer. Tell the person the folder `<video>-watch` can be deleted when they are done.
`````

### File 2: `~/.claude/skills/watch-me-work/watch.py`

`````python
#!/usr/bin/env python3
"""Turn a screen recording with narration into frames plus a timed transcript, ready for Claude to read.

  python3 watch.py <video> [--out DIR] [--every 5] [--scene 0.25] [--max-frames 60] [--model base] [--lang en]

Needs ffmpeg (on your PATH) and either faster-whisper or openai-whisper (pip). The speech is turned into text on
this computer. Nothing is sent anywhere.

Writes into DIR (default: a folder named like the video, next to it, ending in -watch):
  frames/        pictures, named with the time they were taken (f001_00m12s.jpg)
  words.json     every spoken word with its start and end time in seconds
  timeline.md    each spoken part with its time, its words and the frames from that moment
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def need_ffmpeg():
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise SystemExit(
                f"{tool} is missing. Install ffmpeg: brew install ffmpeg (Mac), winget install -e --id Gyan.FFmpeg (Windows), "
                "sudo apt install ffmpeg (Linux). Then open a new terminal and run this again.")


def duration(video):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", video])
    try:
        return float(r.stdout.strip())
    except ValueError:
        raise SystemExit(f"ffprobe could not read this file as a video: {video}\n{r.stderr.strip()[:300]}")


def has_audio(video):
    r = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", video])
    return bool(r.stdout.strip())


def mmss(t):
    t = int(t)
    return f"{t // 60:02d}m{t % 60:02d}s"


def clock(t):
    t = int(t)
    return f"{t // 60}:{t % 60:02d}"


def pull_frames(video, frames_dir, every, scene, max_frames, dur):
    """Frames at every scene change, plus one at least every `every` seconds. Thinned evenly if there are too many."""
    tmp = tempfile.mkdtemp(prefix="watch-")
    expr = f"select='isnan(prev_selected_t)+gt(scene,{scene})+gte(t-prev_selected_t,{every})',showinfo,scale='min(1280,iw)':-2"
    r = run(["ffmpeg", "-hide_banner", "-y", "-i", video, "-an", "-vf", expr, "-vsync", "vfr", "-q:v", "4",
             os.path.join(tmp, "%05d.jpg")])
    times = [float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)]
    files = sorted(f for f in os.listdir(tmp) if f.endswith(".jpg"))
    if not files:
        raise SystemExit("ffmpeg made no frames from this video.\n" + r.stderr[-400:])
    times = (times + [0.0] * len(files))[:len(files)]
    pairs = list(zip(times, files))
    scene_count = len(pairs)
    if len(pairs) > max_frames:   # keep the first and last, spread the rest evenly
        idx = sorted({round(i * (len(pairs) - 1) / (max_frames - 1)) for i in range(max_frames)})
        pairs = [pairs[i] for i in idx]
    os.makedirs(frames_dir, exist_ok=True)
    for old in os.listdir(frames_dir):
        if old.endswith(".jpg"):
            os.remove(os.path.join(frames_dir, old))
    out = []
    for n, (t, f) in enumerate(pairs, 1):
        name = f"f{n:03d}_{mmss(t)}.jpg"
        shutil.move(os.path.join(tmp, f), os.path.join(frames_dir, name))
        out.append((t, name))
    shutil.rmtree(tmp, ignore_errors=True)
    return out, scene_count


def transcribe(video, model_name, lang):
    """Returns (segments, words). Each segment: (start, end, text). Each word: (start, end, word)."""
    wav = os.path.join(tempfile.mkdtemp(prefix="watch-"), "speech.wav")
    r = run(["ffmpeg", "-hide_banner", "-y", "-i", video, "-vn", "-ac", "1", "-ar", "16000", wav])
    if r.returncode != 0 or not os.path.exists(wav):
        raise SystemExit("ffmpeg could not pull the sound out of this video.\n" + r.stderr[-300:])
    segs, words = [], []
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel(model_name, device="cpu", compute_type="int8")
        it, _ = model.transcribe(wav, word_timestamps=True, vad_filter=True, language=lang or None)
        for s in it:
            segs.append((s.start, s.end, s.text.strip()))
            for w in s.words or []:
                words.append((w.start, w.end, w.word.strip()))
        return segs, words
    except ImportError:
        pass
    try:
        import whisper
    except ImportError:
        raise SystemExit("No speech model is installed. Install one with: python3 -m pip install --user faster-whisper "
                         "(or: python3 -m pip install --user openai-whisper). Then run this again.")
    res = whisper.load_model(model_name).transcribe(wav, word_timestamps=True, language=lang or None, fp16=False)
    for s in res["segments"]:
        segs.append((s["start"], s["end"], s["text"].strip()))
        for w in s.get("words", []):
            words.append((w["start"], w["end"], w["word"].strip()))
    return segs, words


def sentences(words, segs):
    """Split the speech at the end of each sentence, so every spoken step gets its own time."""
    if not words:
        return segs
    out, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        pause = i + 1 < len(words) and words[i + 1][0] - w[1] > 0.8   # a long pause also ends a spoken step
        if re.search(r"[.!?]$", w[2]) or pause or len(cur) >= 40:
            out.append((cur[0][0], cur[-1][1], " ".join(x[2] for x in cur)))
            cur = []
    if cur:
        out.append((cur[0][0], cur[-1][1], " ".join(x[2] for x in cur)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("video")
    ap.add_argument("--out")
    ap.add_argument("--every", type=float, default=5, help="at least one frame this often, in seconds")
    ap.add_argument("--scene", type=float, default=0.25, help="how big a change on screen counts as a new scene (0 to 1)")
    ap.add_argument("--max-frames", type=int, default=60, help="never keep more frames than this")
    ap.add_argument("--model", default="base", help="speech model size: tiny, base, small, medium")
    ap.add_argument("--lang", default="en", help="spoken language code, or empty to detect it")
    a = ap.parse_args()

    video = os.path.abspath(os.path.expanduser(a.video))
    if not os.path.isfile(video):
        raise SystemExit(f"File not found: {video}")
    need_ffmpeg()
    dur = duration(video)
    out = os.path.abspath(a.out) if a.out else os.path.splitext(video)[0] + "-watch"
    os.makedirs(out, exist_ok=True)
    frames_dir = os.path.join(out, "frames")

    print(f"Video: {video} ({clock(dur)} long)")
    if not has_audio(video):
        print("WARNING: this video has no sound track. There is no narration to read, so the WHY of each step is missing.")
        segs, words = [], []
    else:
        print("Listening to the narration (the first time, the speech model downloads once)...")
        segs, words = transcribe(video, a.model, a.lang)
        segs = sentences(words, segs)
    print("Pulling frames...")
    frames, scene_count = pull_frames(video, frames_dir, a.every, a.scene, a.max_frames, dur)

    with open(os.path.join(out, "words.json"), "w") as f:
        json.dump([{"start": round(s, 2), "end": round(e, 2), "word": w} for s, e, w in words], f, indent=0)

    # Put each frame under the spoken part that is going on when it was taken.
    notes = []
    L = ["# Timeline", "", f"Video: {os.path.basename(video)}, {clock(dur)} long. Frames are in `{frames_dir}`.", ""]
    if scene_count > len(frames):
        L.append(f"Note: {scene_count} frames were found and thinned to {len(frames)} so they fit. "
                 "Use --max-frames or --every to change that.\n")
        notes.append("thinned")
    if not segs:
        L.append("No speech was found in this video.\n")
    used = set()
    bounds = [(s, (segs[i + 1][0] if i + 1 < len(segs) else dur + 1)) for i, (s, e, t) in enumerate(segs)]
    for i, (s, e, text) in enumerate(segs):
        lo, hi = (0 if i == 0 else bounds[i][0]), bounds[i][1]
        mine = [(t, n) for t, n in frames if lo <= t < hi]
        used.update(n for _, n in mine)
        L.append(f"## {clock(s)} to {clock(e)}")
        L.append(f"Said: {text}")
        L.append("Frames: " + (", ".join(f"{n} ({clock(t)})" for t, n in mine) if mine else "none in this part"))
        L.append("")
    rest = [(t, n) for t, n in frames if n not in used]
    if rest:
        L.append("## Frames with no speech around them")
        L.append(", ".join(f"{n} ({clock(t)})" for t, n in rest))
        L.append("")
    with open(os.path.join(out, "timeline.md"), "w") as f:
        f.write("\n".join(L))

    print(f"Done. {len(frames)} frames, {len(words)} words, {len(segs)} spoken parts.")
    print(f"Read this first: {os.path.join(out, 'timeline.md')}")
    print(f"Frames: {frames_dir}")


if __name__ == "__main__":
    main()
`````
