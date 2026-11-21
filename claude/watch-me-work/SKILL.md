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
