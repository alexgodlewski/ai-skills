# watch-me-work

**Do a task once on video. Claude turns it into a skill.**

Record your screen while you do the task once, and talk through it like you are showing a new hire. Drop the video into Claude Code and say: watch this and turn it into a skill. Claude looks at the steps on screen, listens to why you do each one, and writes the skill. Next time you type one word and it does the whole thing.

**[Download watch-me-work-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/watch-me-work-skill.md)**

## Install (2 minutes)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `watch-me-work-skill.md` in and type **set this up**.
3. Claude installs it and tells you what else it needs (it asks before it installs anything).

## The exact prompt

After you drop your recording into Claude Code, type:

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

| What | Why | Cost |
|---|---|---|
| Claude Code (the Code tab in the Claude desktop app) | This is where it runs | Any paid Claude plan |
| ffmpeg | Pulls the pictures and sound out of your video | Free |
| Python 3.10 or newer | Runs the small tool | Free |
| faster-whisper (or openai-whisper) | Turns your voice into text on your computer. About 150 MB the first time | Free |

Works on Mac, Windows and Linux. Your video is not uploaded to any speech service. The frames are only read by Claude in your session.

## What it cannot do

- It reads the screen from still pictures, so it can miss a click that happens between two frames. It asks you about anything it is not sure of.
- It writes the skill. It does not run your task. Whether Claude can run a step later depends on the tools it has (files, web, connected apps). The skill says which steps Claude does itself and which it hands back to you.

The source is right here: [`SKILL.md`](SKILL.md) and [`watch.py`](watch.py).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
