---
name: animate
description: Turn a voice note (an audio file) into an animated explainer video with no camera. Transcribes the audio with word timings, plans one scene per sentence, builds the video with HyperFrames (open source HTML to video from HeyGen) and renders a vertical 9:16 MP4 with captions. Use when someone gives an audio file or voice memo and wants an animated video, or asks for a post that does not need them on camera.
---

# Animate

You turn a voice note into a short animated video with their voice on top. No camera. The pictures are made from text, shapes, icons and motion that you build in HTML, and HyperFrames turns that into an MP4.

Be honest about what this makes. It makes clean motion graphics and captions. It does not make filmed footage, AI pictures or a talking person.

## 1. Check what is needed

Run these checks. Tell the person what is missing and fix it with their yes.

- **Node.js 22 or newer.** `node -v`. If missing or older, install it from https://nodejs.org (or `brew install node` on a Mac).
- **FFmpeg.** `ffmpeg -version`. If missing: `brew install ffmpeg` on a Mac, `winget install ffmpeg` on Windows.
- **Internet** for the first run. HyperFrames downloads a browser and a speech model the first time, and the video text animation library loads from a web link. It can take a few minutes.
- **The audio file.** Ask: "Where is your voice note?" Any common type works (m4a, mp3, wav). iPhone Voice Memos are m4a.

If a command here fails, read its error. HyperFrames prints a `Fix:` line. Run `npx hyperframes doctor` to check the setup.

## 2. Get the plan from the person

Ask in one message:

1. "Who is this video for?"
2. "Do you want a color or style? If not, I will use a dark background, one bright color and big white text."
3. "Should the video show captions? (Recommended.)"

Do not ask more than this. Pick the rest yourself.

## 3. Set up the project

Use a new folder, for example `voice-video/`:

```
npx hyperframes init voice-video --resolution portrait --skip-skills --non-interactive
cd voice-video
mkdir -p assets
ffmpeg -y -i "<path to the voice note>" -vn -ac 1 -ar 44100 assets/voice.mp3
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/voice.mp3
```

The last command prints the length in seconds. Keep it: it is the video length. `--resolution portrait` makes a 1080 by 1920 video (9:16). The new folder also gets an `AGENTS.md` file and a starter `index.html`: read `AGENTS.md`, then replace the starter page with yours.

For better results, read the HyperFrames docs before writing the page: `npx hyperframes docs` lists topics, and the project is at https://github.com/heygen-com/hyperframes. If a command or an option here does not match what `npx hyperframes <command> --help` says, trust the help.

## 4. Transcribe with word timings

```
npx hyperframes transcribe assets/voice.mp3 --model small.en --json
```

- For other languages use `--model small --language <code>` (for example `es`).
- If the voice is quiet or there is music under it, use `--model medium.en`.
- It writes `assets/transcript.json` (the last line of the output names the exact path). Each entry is a word with `text`, `start` and `end` in seconds.

Read the transcript. If it has nonsense words, or text over silence, run it again with a bigger model. Fix wrong words by hand, and never change the times.

## 5. Plan the scenes

1. Split the words into sentences. A sentence ends at a period, a question mark, or a pause longer than about 0.7 seconds.
2. Each sentence is one scene. If a sentence is shorter than 1.5 seconds, join it with the next one. If it is longer than 7 seconds, split it at a comma or a pause.
3. A scene starts at the first word's `start` and ends where the next scene begins. The first scene starts at 0, and the last ends at the audio length.
4. For each scene, write one line: the picture idea. Use what the sentence says.

Picture ideas that work well with only HTML, CSS and SVG:

- a big key word or short phrase that pops in;
- a number that counts up;
- a simple icon built from shapes (a phone, a clock, a coin, a check mark, an arrow);
- a before and after: two boxes with an arrow;
- a list that builds one line at a time;
- a simple chart with bars that grow;
- a line that draws a path from one thing to another.

Rules for the pictures:

- One idea per scene. Do not crowd the screen.
- Keep text short, at most about 6 words in the big text. The captions carry the full sentence.
- Keep the same colors, the same type, and the same style in every scene.
- Do not use pictures or logos you do not own. Use shapes and text.

Show the person the scene list in a short table (time, sentence, picture idea) and ask: "Want to change any?" Fix what they say, then build.

## 6. Build the video

Write `index.html` in the project. Follow the HyperFrames rules, which the `lint` command also checks:

- The root element has `data-composition-id="main"`, `data-width="1080"`, `data-height="1920"`, `data-start="0"` and `data-duration` set to the audio length.
- Each scene is a `<section class="clip">` with `data-start` and `data-duration` in seconds.
- Do not set `transform` in CSS on an element that GSAP also animates. Start from a hidden or moved state inside the GSAP call instead.
- Make one paused GSAP timeline and register it with `window.__timelines["main"] = tl;` after it is built. Load GSAP from `https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js`.
- Do not call `play()` on the audio. HyperFrames plays it.
- Use a font stack with no named font (`system-ui, sans-serif`), or ship the font file and add an `@font-face` for it. A named font with no `@font-face` is a lint error.
- No random numbers, no clocks, no network calls in the animation code.
- Every `<audio>` needs an `id`.

The audio goes in like this, inside the root:

```html
<audio id="voice" src="assets/voice.mp3" data-start="0" data-duration="LENGTH" data-track-index="0" data-volume="1"></audio>
```

Captions: one group of 3 to 5 words at a time at the bottom, each group opening at its first word's `start` and closing at its last word's `end`. Hide each group at its end with `tl.set(group, { opacity: 0 }, end)` so none stays on screen.

Each scene animates in at its start (about 0.3 to 0.5 seconds) and settles. Use gentle moves: fade, slide up a little, scale from 0.9. Do not make everything move at once.

## 7. Check it

```
npx hyperframes lint
npx hyperframes check --json
npx hyperframes snapshot
```

- Fix every error before going on.
- `snapshot` writes PNG frames under `.hyperframes/artifacts/snapshots/`. Open a few, one from the middle of each scene, and look: is text cut off, too small, or covered by captions? Fix and run again.
- For the person to watch live, run `npx hyperframes preview --background`, and give them the link it prints.

## 8. Render

When the person is happy:

```
npx hyperframes render --quality looks -o voice-video.mp4
```

- `--quality draft` is faster, for checking. `delivery` is the best quality.
- A 30 second video usually renders in a minute or two.
- Check the file: `ffprobe -v error -show_entries format=duration -of csv=p=0 voice-video.mp4` should match the audio length. If it does not, or the video has no sound, say so and fix it.

## 9. Hand it over

Tell the person:

- the full path of `voice-video.mp4`;
- the length, and that it is 1080 by 1920 (9:16), ready for Reels, TikTok and Shorts;
- that they can ask for changes ("make scene 3 shorter", "change the color to green") and you will re-render.

## Rules

- Never change what the speaker said. Fix a wrong word in the captions only when it is clearly a transcript mistake.
- Only claim what you checked. If the render fails or the snapshot looks wrong, say so.
- Keep the voice note and project folder. Never delete the original audio file.
