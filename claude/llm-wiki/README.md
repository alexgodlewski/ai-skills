# llm-wiki (for Claude)

**Give Claude's memory a table of contents.**

Claude's memory is often a pile: one long CLAUDE.md, a folder of memory notes, some project docs. Claude has to dig through it every time, and when it cannot find something it guesses. Run this skill once and it sorts the pile into topic pages, writes an index page (a table of contents Claude made itself), and adds a short rule to your CLAUDE.md: read the index first, open only the page you need, and say "not in my notes" instead of guessing.

## Where the idea comes from

This is built on Andrej Karpathy's **LLM Wiki** idea file: [gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). His idea: instead of searching raw documents again on every question, let the AI build and maintain a wiki of linked markdown pages. It has raw sources (never changed), the wiki (written by the AI), and a schema file (such as CLAUDE.md) that tells the AI how it works, with three jobs: ingest, query and lint. The skill is written in its own words and does not copy his file. Read his original, it is short.

**What this version adds:** a one-time "organize my memory" run. It points the idea at what Claude already remembers (CLAUDE.md, memory files, project docs) and ends by adding the "read the index first" rule to CLAUDE.md. After that you can still use the three jobs: add a new source, ask a question, or check the wiki for problems.

**[Download llm-wiki-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/llm-wiki-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `llm-wiki-skill.md` in and type **set this up**.
3. Type `/llm-wiki`.

## What happens when you run it

1. It finds your CLAUDE.md, your memory files and any notes folder you name, and shows you the list.
2. It copies everything to a backup folder first. Your original files are never changed or deleted.
3. It builds the wiki (default `~/.claude/wiki/`): topic pages, an `index.md`, and a `log.md`.
4. It shows you the table of contents, and any places where your notes disagree, as questions for you.
5. It shows you the rule it wants to add to CLAUDE.md and **asks first**.
6. It tests the result with three questions.

## What you need

- No account and no API key. It only reads and writes files on your own computer.
- Passwords, keys and tokens found in your notes are not copied into the wiki. Claude tells you which file held them.

## What it cannot do

- It makes Claude look things up instead of guessing. It does not make Claude perfect: if a note is wrong or missing, an answer can still be wrong.
- It only knows what is in your files. It does not read your old chats.

Using Claude in the browser instead? The skill reads and writes files on your computer, so use the Code tab.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
