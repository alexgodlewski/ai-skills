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
