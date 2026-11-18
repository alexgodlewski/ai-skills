---
name: First Skill Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# First Skill Skill

The first skill anyone should build, built with you in a few minutes.

Tell Claude one task you do every day. It does the task with you, step by step, in Claude Code, using your connected tools like Gmail, Google Calendar and Google Drive. Then it saves the whole thing as a skill. Tomorrow you say **run** and the name of the skill, and the work runs without you walking through it again.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

Type `/first-skill`, or say: *Let's build my first skill.*

## What it needs

Claude Code. Connect the tools you use most (Settings, Connectors) for the best result.

## What gets installed

- `~/.claude/skills/first-skill/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/first-skill/` (on Windows: `%USERPROFILE%\.claude\skills\first-skill\`) and write the file below into it exactly as it is. If the folder already has a SKILL.md, ask before you replace it.
3. **Tell them it is ready**, and how to use it: Type `/first-skill`, or say: *Let's build my first skill.* If `/first-skill` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/first-skill/SKILL.md`

`````markdown
---
name: first-skill
description: Build the first skill with the person. Asks which task they do every day, does that task with them step by step in Claude Code (using their connected tools such as Gmail, Google Calendar and Google Drive when available), then writes a new SKILL.md into ~/.claude/skills/<name>/ so next time they just say "run <name>". Use when someone wants to turn a daily task or routine into a saved workflow, or asks how to build their first skill.
---

# First Skill

A skill is a saved workflow that Claude can run again. You build one with the person, from a task they really do, so tomorrow they say "run <name>" and the work happens without them walking through it again.

You work in Claude Code. Each step is done for real, with the person watching, and you write down what you did.

## 1. Check the tools

Look at which tools you can use here: Gmail, Google Calendar, Google Drive, files on the computer, the web. Many daily tasks use Gmail, Google Calendar and Google Drive.

- Tell the person which of these you can see.
- If a tool they need is missing, say so in one line and tell them to open Settings in the Claude desktop app and look under Connectors to add it. Then continue with the tools that work, or wait if they want to add it first.

## 2. Ask these questions

Ask them one at a time. Wait for each answer. Keep your side short.

1. "What is one task you do every single day, or almost every day?"
2. "Walk me through it from the first click to the last. What do you do first?"
3. "What tools or places do you use for it (for example Gmail, Calendar, Drive, a website, a spreadsheet)?"
4. "What do you look at to decide what to do? For example: who the email is from, a date, a word."
5. "What does a finished, good result look like? Where does it end up?"
6. "Is there anything I should never do on my own? For example: send an email, delete a file, reply to a client."
7. "How long does it take you now, and how often do you do it?"

If the answer to question 1 is too big (for example "my whole job"), ask for the smallest daily piece of it.

## 3. Do the task together, for real

Now do the task once, start to finish, in this session.

- Do one step at a time. Say what you are about to do in one short line, then do it.
- Use their connected tools to do the real work. Read real emails, check the real calendar, open the real files.
- After each step, ask: "Is that right? Anything you would do differently?" Fix it before you move on.
- When a step would send, delete, move or change something, ask first, even if it is a test run.
- Write down each step as you go: what you looked at, what you did, how you decided, what came out.

If the person says "that is not how I do it", change the step. Their way wins.

## 4. Write the skill

When the task is done and they are happy, say: "I can save this as a skill now."

1. Pick a short name in lowercase words joined by hyphens, for example `inbox-summary`. Ask if they like it.
2. Check `~/.claude/skills/<name>/`. If it already exists, ask before you change it. Never overwrite without a yes.
3. Create `~/.claude/skills/<name>/SKILL.md` (on Windows: `%USERPROFILE%\.claude\skills\<name>\SKILL.md`) in this shape:

```
---
name: <name>
description: <one or two sentences: what it does, and the words the person will say to start it>
---

# <Title>

## What this does
<one or two lines>

## Tools it uses
<for example Gmail, Google Calendar, Google Drive>

## Steps
1. <step, in the order you did them, with the exact thing to look at>
2. <step>
3. <step>

## How to decide
<the rules the person gave you: what counts as important, what to skip, what to flag>

## What the result looks like
<where it goes, what it contains, how long it is>

## Never do without asking
<the things from question 6, and anything that sends, deletes or changes things>

## Check before you finish
<two or three checks, for example: every item has a link, nothing is longer than 10 lines>
```

4. Write it in plain words, as instructions to yourself. Use the person's own words for their rules.
5. Keep it short. One page is plenty.

## 5. Tell them how to use it

Say:

- The skill's name and where it lives.
- "Tomorrow, open Claude Code and say: run <name>." If `/<name>` does not show up in the `/` list, they start a new session.
- That they can open the file and edit it, and that they can ask you to change it: "update <name> so it also does X".

Then offer the next one: "What is the next task you do every day? We can do the same again."

## Worked example: a daily inbox summary

This shows the shape of a finished skill. Do not copy it for someone else. Build theirs from their answers.

What the person said:

- Task: every morning, read unread email and work out what needs a reply.
- Tools: Gmail and Google Calendar.
- Decide by: emails from clients and anything with a question or a date in it matter most. Newsletters and receipts do not.
- Result: a short list in the chat, with a draft reply for the top three.
- Never: send an email without asking.
- Time: 25 minutes a day.

The skill written to `~/.claude/skills/inbox-summary/SKILL.md`:

```
---
name: inbox-summary
description: Summarize unread Gmail each morning, say what needs a reply today, and draft replies for the top three. Use when the person says "run inbox-summary", "inbox summary" or "what needs my attention".
---

# Inbox Summary

## What this does
Reads unread email from the last day, sorts it, and gives a short list with draft replies.

## Tools it uses
Gmail, Google Calendar.

## Steps
1. Read unread email from the last 24 hours in Gmail.
2. Put each email in one group: Client, Needs a reply, Waiting on someone, Ignore.
3. Check today's Google Calendar. If an email asks for a time, look for free slots.
4. Pick the top 3 emails that need a reply today.
5. Write a draft reply for each of the 3, in the person's tone: short, friendly, no jargon.
6. Show the list.

## How to decide
- Client emails come first.
- An email with a question or a date needs a reply.
- Newsletters, receipts and notifications go in Ignore.

## What the result looks like
A list in the chat. One line per email: who, what they want, the group. Then the 3 drafts. Under 40 lines in all.

## Never do without asking
Send, archive or delete any email. Create a calendar event.

## Check before you finish
- Every email in the list says who sent it.
- Each draft answers the question that was asked.
- Nothing was sent.
```

After that, the person's morning is: open Claude Code, type "run inbox-summary", read the list.

## Rules

- Only claim a tool works if you used it in this session.
- Never save a step you did not actually do together, and never guess a rule. If you are unsure, ask.
- Never write a password, a key or private contact details into the skill.
- Do not promise a time saving. Say what the skill does, and let them measure it.
`````
