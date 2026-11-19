# captions (for Claude)

**Captions that go behind your head and never sit under Instagram's buttons.**

Type `/captions` and the path to your talking head video into Claude. It turns the video into a finished vertical reel (1080 x 1920) with captions that sit between the background and you: your head covers a small part of the text, which gives that layered look. It also keeps every caption out of the zones where Instagram puts its buttons.

It uses [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML rendered to video) and does this:

1. **Word timings.** Whisper turns your speech into words with start and end times. Claude fixes names and brand words.
2. **Short captions.** 4 to 5 words per caption, on one line. Never 1 or 2 words. Never ending on a word like "of", "the", "to" or "a".
3. **You, cut out.** `npx hyperframes remove-background` makes a transparent video of only you, so text can sit behind your head.
4. **Safe zones.** Captions stay inside this box on a 1080 px wide frame: x 70 to 940, y 250 to 1536. That keeps them out of the bottom 20% (Instagram's caption and username) and the right-side button column (about 140 px). Claude measures this with numbers. Instagram changes its screen sometimes, so treat these as careful estimates.
5. **The look.** Default is a lime `#C6FF3D` pill, black text, weight 700, 54 px, rounded 6 px. Ask for another color or font and Claude changes only that.

**[Download captions-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/captions-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `captions-skill.md` in and type **set this up**.
3. Type `/captions` and the path to your video, for example `/captions ~/Desktop/my-reel.mp4`.

## What you need

- **No account and no API key.** Whisper, the cut-out and the render all run on your own computer. Your video is not uploaded anywhere.
- **Node.js and ffmpeg** installed. Claude checks this first with `npx hyperframes doctor` and tells you what is missing.
- **Time and memory.** The first run downloads the models. The cut-out is the slow part and needs a few GB of free memory, so do one video at a time.

## What it cannot do

- A video without speech cannot be captioned.
- The cut-out can be a little rough on fast hand moves. Claude checks three frames and tells you if it is.
- If you stand very tall in the frame, the behind-the-head effect may be small, because the safe zones come first. Claude tells you when that happens.

Using Claude in the browser instead? The skill runs commands on your computer, so use the Code tab.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
