---
name: LLM Wiki Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# LLM Wiki Skill

Give Claude's memory a table of contents. Run it once and it sorts your CLAUDE.md, memory files and notes into topic pages, writes an index page, and adds a short rule to CLAUDE.md so Claude reads the index first instead of guessing. Based on Andrej Karpathy's LLM Wiki idea (gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /llm-wiki

It backs up your files first, never changes the originals, and asks before it edits CLAUDE.md.

## What gets installed

- `~/.claude/skills/llm-wiki/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/llm-wiki/` (on Windows: `%USERPROFILE%\.claude\skills\llm-wiki\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/llm-wiki`. If `/llm-wiki` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/llm-wiki/SKILL.md`

`````markdown
---
name: llm-wiki
description: Reorganizes Claude's memory into a wiki. Based on Andrej Karpathy's LLM Wiki idea (raw sources, a wiki of interlinked markdown pages the LLM keeps up to date, and a schema file). Run once, it reads the person's CLAUDE.md, memory files and project docs, sorts them into topic pages, writes an index page (a table of contents Claude made itself), and adds a short rule to CLAUDE.md so Claude reads the index first. Afterwards it can add new sources, answer from the wiki, and check the wiki for problems. Use when someone types /llm-wiki, or asks to organize, clean up or index Claude's memory.
---

# LLM Wiki

Claude's memory is usually a pile: a long CLAUDE.md, a folder of memory notes, a few project docs. Claude has to search the pile every time, and when it cannot find something it guesses. This skill turns the pile into a small wiki with a table of contents. Claude reads the table of contents first, then opens only the pages it needs.

## Where this comes from

The idea is Andrej Karpathy's **LLM Wiki** (an "idea file", April 2026): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

His idea, in short: instead of searching raw documents again on every question, let the LLM build and maintain a wiki of interlinked markdown pages between you and your sources. It has three parts:

- **Raw sources:** your original files. The LLM reads them and never changes them.
- **The wiki:** markdown pages the LLM writes and keeps up to date: summaries, topic pages, an `index.md` (a catalog of every page) and a `log.md` (a dated list of what happened).
- **The schema:** a file such as CLAUDE.md that tells the LLM how the wiki works.

And three jobs: **ingest** (add a source), **query** (ask questions and file good answers back), and **lint** (check the wiki for problems).

**This skill's version of the idea:** it is a one-time "organize my memory" run. It points the idea at the things Claude already remembers (CLAUDE.md, memory files, project docs) and ends with a short rule in CLAUDE.md that tells Claude to read the index first. After that, the three jobs are there when you want them.

## 0. Start

Say what you are about to do in two lines: you will read the person's memory and notes, copy them to a backup, build a wiki from them, and ask before changing CLAUDE.md. Nothing is deleted.

## 1. Find the pile

Look for these and list what you find, with the size of each (lines or words):

- the global `~/.claude/CLAUDE.md`;
- the project's `CLAUDE.md` (and `AGENTS.md` if it exists) in the current folder;
- Claude's memory folder for this project, usually `~/.claude/projects/<project-folder>/memory/` (list the folder to find it), including its `MEMORY.md`;
- any docs folder the person points to (notes, plans, READMEs).

Show the list and ask which to include. Default: all of the above, except long code files. If you find nothing, say so and ask where their notes are. Do not make a wiki out of nothing.

**Secrets:** if you see anything that looks like a password, API key or token, do not copy it into the wiki. Leave a pointer ("the Stripe key is in .env") and tell the person which file held it.

## 2. Back up first

Copy every file you will read into a folder named `~/.claude/wiki-backup-<today's date>/`. Tell the person where it is. These are the raw sources: you never change or delete the originals.

## 3. Build the wiki

Ask once where it should live. Default: `~/.claude/wiki/` (works in every project). Option: a `wiki/` folder inside one project.

Read all the sources. Then:

1. **Choose the topics yourself** from what is really in the notes. Typical ones: about the person and the business, people and clients, each project, tools and accounts, rules and preferences (how they like things done), decisions and why, how-to steps, open to-dos. Do not use a topic with nothing in it. Aim for pages of one screen or so. Split a page that grows past about 150 lines.
2. **Write one page per topic.** Each page starts with a small header:

   ```
   ---
   title: Short name
   summary: One line saying what is on this page
   sources: [file names it came from]
   updated: YYYY-MM-DD
   ---
   ```

   Then plain notes. Keep the person's facts and rules in their own words. Link to related pages with normal markdown links.
3. **Merge duplicates.** If the same fact is in three files, write it once.
4. **Do not settle contradictions yourself.** If two notes disagree (for example two different prices), write both on the page under "Conflict" with their sources and dates, and ask the person which is right at the end.
5. **Mark old things.** If a note has a date, an end date, or reads like it is out of date, add "(check: may be old)" instead of deleting it.
6. **Never invent.** A page holds only what the sources say.

## 4. Write the index

Make `index.md` at the top of the wiki. This is the table of contents. It lists every page, grouped by category, one line each:

```
## Projects
- [Project name](projects/name.md): what it is and its state, one line
```

At the top, two lines: what this wiki is, and today's date. Also make `log.md`, with the first entry in this form so it can be searched:

`## [YYYY-MM-DD] organize | built the wiki from N files`

## 5. Add the rule to CLAUDE.md

This is what makes Claude use it. Show the person this block, and **ask before you add it**. Put it in the global `~/.claude/CLAUDE.md`, or the project's if the wiki is inside a project:

```
## Memory wiki
My notes live in <wiki path>. Read <wiki path>/index.md first.
Open only the pages that fit the question. If the wiki has the answer, use it.
If it does not, say "not in my notes" and ask. Do not guess.
When I tell you something lasting, add it to the right page, update index.md, and add a line to log.md.
```

If Claude's automatic memory file `MEMORY.md` exists, leave it as it is. Add one line at the top of it pointing to the wiki index.

## 6. Show the result

Tell the person:

- how many files went in and how many pages came out;
- the table of contents (paste the index);
- every conflict you found, each as a question for them to answer;
- anything you left out and why (secrets, long code files);
- where the backup is, and how to undo: delete the wiki folder and the CLAUDE.md block.

Then test it. Pick 3 facts from different pages, ask yourself the question as if it were new, and answer from the index and the pages only. Show the person the test.

## Later: the three jobs

When the person types `/llm-wiki` again (or asks), ask which job:

- **Ingest:** they give a new source (a file, a link, pasted notes). Read it, say the key points in a few lines, write or update the pages it touches (often several), update the index, add a log line. One source at a time, and show what changed.
- **Query:** they ask a question. Read the index, open the right pages, answer, and say which pages you used. If the answer is worth keeping (a comparison, a decision), offer to save it as a page.
- **Lint:** check the whole wiki and report: pages that disagree, facts that look old, pages no other page links to, topics mentioned many times without a page, and pages missing from the index. Fix the safe ones (links, index) and ask about the rest.

## Rules

- Never change or delete the original files. Work from the backup copy and the originals as read-only.
- Never copy passwords, keys or tokens into the wiki.
- Ask before editing CLAUDE.md. Show the exact block first.
- Never invent facts, and never choose between two conflicting notes without asking.
- When the wiki does not have the answer, say so. Do not guess.
- This makes Claude look things up instead of guessing. It does not make it perfect: if a note is wrong or missing, the answer can still be wrong.
- Plain words. No jargon unless you explain it in the same sentence.
`````
