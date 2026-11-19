---
name: Captions Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Captions Skill

Captions that go behind your head and never sit under Instagram's buttons. Type `/captions` and the path to your talking head video. It makes a captioned vertical reel with HyperFrames: whisper word timings, 4 to 5 word captions on one line, you cut out on every frame so the text sits behind your head, and a measured Instagram safe zone.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /captions ~/Desktop/my-reel.mp4

No account or API key. Everything runs on your own computer, and it needs Node.js and ffmpeg.

## What gets installed

- `~/.claude/skills/captions/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/captions/` (on Windows: `%USERPROFILE%\.claude\skills\captions\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/captions` and the path to their video. If `/captions` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/captions/SKILL.md`

`````markdown
---
name: captions
description: Turns a talking head video into a captioned vertical reel with HyperFrames (npx hyperframes, HTML rendered to video). Word timings come from whisper, captions show 4 to 5 words on one line, and the speaker is cut out on every frame so the text can sit behind their head. Captions stay out of Instagram's button zones. Default look is a lime pill with black bold text. Use when someone types /captions with a video file, or wants captions that go behind the head and never sit under Instagram's buttons.
---

# Captions

You turn the person's talking head video into a finished vertical reel (1080 x 1920) with captions that sit **between the background and the speaker**: the text is behind their head, and never under Instagram's buttons.

How it works, in one line: whisper gives the words and their times, a matte video cuts the person out of every frame, and a HyperFrames page stacks three layers (video, then captions, then the person cut-out on top) and renders it to MP4.

## 0. Start

The video is what the person typed after `/captions` (a file path). If there is none, ask for it in one line and wait.

Check what you need before you start, and tell the person plainly if something is missing:

- **Node.js and ffmpeg.** Run `node -v`, `ffmpeg -version`, and `npx --yes hyperframes@latest doctor`. The doctor lists what is missing and how to fix it.
- **Nothing needs an account or an API key.** Whisper, the person cut-out and the render all run on the person's own computer. The first run downloads the models, which takes a few minutes. The cut-out is the slow part and needs a few GB of free memory: run it on one video at a time.
- Read the HyperFrames skill if it is installed (`hyperframes-core`), or run `npx hyperframes docs compositions`. Follow its rules for the page: `data-start`, `data-duration`, `data-track-index`, `class="clip"`, and muted video elements.

Look at the video with `ffprobe`: size, length, frame rate, and whether it has sound. Tell the person what you found. A video without speech cannot be captioned: say so and stop.

## 1. Set up the project

1. Make a new folder for the project and run `npx --yes hyperframes@latest init <name> --resolution portrait --non-interactive` inside the person's chosen location. This makes a 1080 x 1920 canvas.
2. Copy the video into the project's `assets/` folder as `input.mp4`.
3. If the video is not 1080 x 1920 (for example it is landscape), tell the person you will scale and crop it to fill the vertical frame, centered on the speaker. Use the same crop and scale on the video and the cut-out so they line up exactly. Never stretch it.
4. Cut the audio out with ffmpeg into `assets/voice.m4a` (or `.wav`). The final reel uses this audio, not the video layer's.

## 2. Word timings

Run `npx --yes hyperframes@latest transcribe assets/voice.m4a --model small.en` (English). For another language use `--model small --language <code>`. Always pass `--model`: the default one translates other languages into English. Whisper makes mistakes: tell the person they can pass `--model medium.en` for better results, slower.

Read the result. It holds every word with a start and end time. Check the real file shape before you build on it.

**Read the transcript yourself and fix it.** Names, brands, numbers and product words are the usual mistakes. Correct the text, keep the times. Ask the person to confirm names you are unsure about. Do not guess a spelling.

## 3. Cut the person out

Run:

`npx --yes hyperframes@latest remove-background assets/input.mp4 -o assets/matte.webm`

This makes a transparent video of only the person, with the same length and the same timing as the original. It runs a local model, so give it time. If you also made a crop or scale in step 1, cut out the already-cropped video, so the matte matches the layer below it.

Check it: look at 3 frames (start, middle, end) and make sure the hair, the hands and the shoulders are cut cleanly. If the cut is rough, say so before going further. If it is rough, try `--quality best` for a cleaner color match, and tell the person the edges may still be soft on fast moves.

## 4. Write the captions

Group the words into captions with these rules:

- **4 to 5 words per caption,** on one line. Never 1 or 2 words. The last caption of a sentence may be 3 words if there is no other way, but never 1 or 2.
- **Never end a caption on** `of`, `the`, `to`, `a`, `an`, `if`, `and`, `or`, `in`, `I`. Move that word to the next caption.
- **Break at the end of a sentence** (`.` `?` `!`) and at a comma that starts a new thought. A caption never crosses a sentence end.
- Each caption starts when its first word starts and ends when the next caption starts. If the person pauses for longer than about half a second, let the caption go away during the pause.
- **No em dashes or en dashes** in any caption. Use a comma or a period instead.
- Keep the person's words. Remove nothing, add nothing. You may fix spelling and add a period or comma.

## 5. The look (default)

This is the default look. Use it unless the person asks for something else:

- **Pill:** background `#C6FF3D` (lime), border radius 6 px, padding about `12px 24px 17px`.
- **Text:** `#0a0a0a`, font weight 700, 54 px, letter spacing -0.04em, line height 1, one line (`white-space: nowrap`).
- **Width:** never wider than 860 px. If a caption is wider at 54 px, shrink that caption's font size until it fits. Do not wrap it.
- **Font:** a bold sans font that is allowed to render. Use a font file in the project's `assets/` folder with `@font-face`, or a font HyperFrames can load. Check a snapshot to make sure it really used your font and did not fall back to a default.
- **Animation:** each caption pops in with a scale from 0.92 to 1 over 4 frames, then hard-cuts to the next. Nothing else moves.

If the person asks for another color or font, change only that. The rules in steps 4 and 6 stay.

## 6. Instagram safe zones

Instagram puts its own buttons on top of the video. The frame is 1080 x 1920. These are the zones this skill uses. They are rounded, cautious numbers (Instagram changes its screen from time to time), so say that to the person:

- **Bottom 20%:** `y` from 1536 to 1920 is for Instagram's caption, username, and music line. **No caption may go below y = 1536.**
- **Right side:** a column about 140 px wide holds the like, comment, share and more buttons. **No caption may go right of x = 940.**
- **Left side:** keep a margin of 70 px, so the text is not cramped. **No caption left of x = 70.**
- **Top:** keep captions below y = 250. The top bar of Instagram sits there.

So every caption pill must fit inside the box **x 70 to 940, y 250 to 1536**. Center the pills inside that box (at x = 505), not on the middle of the frame.

You must check this with numbers, not by eye. After you build the page, read the position and size of every caption pill in the browser (for example with `getBoundingClientRect` for each caption at its most extreme size, or with `npx hyperframes inspect`) and confirm all four edges are inside the box. Print the worst numbers for the person. Also look at one frame with the Instagram zones drawn on it, and show it to the person.

## 7. Put the text behind the head

Build the page with three layers, from bottom to top:

1. **Layer 1:** the video (`assets/input.mp4`), muted.
2. **Layer 2:** the captions.
3. **Layer 3:** the cut-out (`assets/matte.webm`), muted, at exactly the same position, size and start time as layer 1.

Because the cut-out is on top, anything of the person that overlaps a caption hides part of it. That is the effect. Audio comes from the separate voice file, not from the muted video layers.

But the text must stay readable. Choose the caption height with a measurement:

1. Find where the speaker's head is: from a few matte frames, get the top of the head and the chin line.
2. Put the caption box vertically so the top of the head, or the edge of the shoulders, only overlaps part of the pill. Start with the pill's middle about 160 px below the chin line and move it until the head overlaps a small part of the text.
3. **Measure it.** For each caption, take the matte frame at the middle of its time, and work out how much of the caption's box is covered by the person (pixels with alpha above 50%). If more than 25% of a caption's box is covered, move the caption or make it smaller. Aim for 5 to 20%. A caption fully hidden or fully in front is a failure.
4. The pill must still be inside the safe box from step 6 after you move it. If the safe box and a readable overlap cannot both be met on a given video (for example the speaker is very tall in the frame), keep the safe box and say that the behind-the-head effect is small on this video. Never break the safe zone to get the effect.
5. If the person moves a lot, one fixed height may not work. You may use two or three fixed heights and pick the best per caption. Do not make the captions move around smoothly.

## 8. Check, then render

1. Run `npx --yes hyperframes@latest lint` and `npx --yes hyperframes@latest check`. Fix everything they report.
2. Take snapshots at 5 or more moments (`npx hyperframes snapshot`), including the first caption and the last. Look at them. Check: the text is readable, the head hides part of it and not all, nothing is inside a button zone, no caption is cut off.
3. Show the person the snapshots and ask once if they want changes.
4. Render: `npx --yes hyperframes@latest render -o captioned.mp4 --fps 30` (use the video's own frame rate if it is 24, 25, 30 or 60). Tell the person where the file is.

## 9. Hand over

Tell the person, in a few plain lines:

- where the finished video is;
- the safe-zone box you used and the worst measured edges;
- the share of each caption that the head hides (lowest, highest, average);
- anything you fixed in the transcript;
- anything that is not perfect (a rough cut-out on fast hand moves, for example).

## Rules

- Everything runs on the person's computer. Do not upload their video anywhere.
- Never invent words the person did not say.
- No em dashes or en dashes in captions.
- Captions never go inside the Instagram zones, even for the behind-the-head effect.
- Measure the zones and the overlap. Do not judge them by eye.
- Plain words. No jargon unless you explain it in the same sentence.
`````
