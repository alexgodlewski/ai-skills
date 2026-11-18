---
name: Outcome First Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Outcome First Skill

Stop telling Claude how. Tell it what. Before Claude builds anything, this skill asks you the right questions about the finished result, writes a one-page brief, and builds it in one go when you say yes.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

Just ask for something, the way you always do:

> Make me a landing page for my coffee roaster.

Or call it by name: `/outcome-first` and what you want.

## What gets installed

- `~/.claude/skills/outcome-first/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/outcome-first/` (on Windows: `%USERPROFILE%\.claude\skills\outcome-first\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: ask for anything they want built, or type `/outcome-first` and what they want. If `/outcome-first` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/outcome-first/SKILL.md`

`````markdown
---
name: outcome-first
description: Before building anything (a page, a document, an email, code, a plan, a design), ask the person the right questions about the finished result, write a one-page result brief, get a yes, and only then build it in one go. Use whenever someone asks Claude to make, write, build or create something and has not already described the end result in detail.
---

# Outcome First

The people who build Claude say the same thing: stop telling it how, tell it what. Explain the task, describe what a good result looks like, and say how to check it. Most people do the opposite. They write one line about the result and a page about how to do it, so Claude guesses everything that matters. Every guess can cost hours of fixing.

This skill flips that. It gets a full picture of the finished result first, then builds it in one go.

## 1. Spot the request

Use this skill when the person asks you to make something and the finished result is not yet clear. Skip it when they already gave a detailed brief, or when the task is tiny (one short answer, one quick fix).

## 2. Ask about the result, not the method

Ask in one message, as a short numbered list, only the questions that matter for this request. Pick from:

1. **Who is it for?** The reader, user or customer, and what they already know.
2. **What does done look like?** Describe the finished thing as if it already exists.
3. **What must it include?** Sections, facts, features, numbers, names, links.
4. **What must it never do?** Tone, claims, words, styles to avoid.
5. **An example you like?** A link, a file, or a short description of something close.
6. **Where will it be used?** Website, email, Instagram, a meeting, a printed page.
7. **How will you judge it?** The one or two things that make it a win.

Never ask how they want you to build it. That part is your job.

If they answer only some questions, fill the rest with sensible defaults and say which ones you assumed.

## 3. Write the result brief

Write a short brief, at most one page, with these headings:

- **The result** (two or three sentences, in the present tense, as if it exists)
- **For**
- **Must include**
- **Must avoid**
- **Done means** (how you will check it before you hand it over)
- **Assumed** (the defaults you chose)

End with: "Build this? Reply yes, or tell me what to change."

## 4. Build it

When they say yes, build the whole thing in one go, matching the brief line by line. Do not ask more questions unless something in the brief is impossible.

After it is built, check it against "Done means" and "Must avoid", fix anything that misses, and give a two-line summary of what you made.

## Rules

- Questions are about the result, never about the steps.
- Keep the questions to one message. Seven at most, fewer is better.
- Never guess a fact you could ask for. Every guess can cost hours of fixing.
- Plain words. No jargon.
`````
