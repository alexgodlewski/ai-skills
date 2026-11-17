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
