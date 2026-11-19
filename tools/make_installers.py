#!/usr/bin/env python3
"""Build the one-file installers (claude/<skill>/<skill>-skill.md) from each claude/<skill>/SKILL.md, then check them.

A person drags <skill>-skill.md into the Claude desktop app (Code tab), types "set this up", and Claude writes
~/.claude/skills/<skill>/SKILL.md. SKILL.md is the source of truth: edit it, then run this script.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILLS = {
    "search": dict(
        title="Search Skill",
        pitch="Get your business named in Google's AI answer. Type `/search` and your website into Claude. It sends agents to check how Google's AI sees your business, finds what is missing (reviews, service pages, the answers to the questions your customers actually ask), and then fixes it.",
        use="> /search yourbusiness.com\n\nIf your website's files are open in Claude Code, it makes the changes for you after you say yes. If not, it writes every fix ready to paste.",
    ),
    "outcome-first": dict(
        title="Outcome First Skill",
        pitch="Stop telling Claude how. Tell it what. Before Claude builds anything, this skill asks you the right questions about the finished result, writes a one-page brief, and builds it in one go when you say yes.",
        use="Just ask for something, the way you always do:\n\n> Make me a landing page for my coffee roaster.\n\nOr call it by name: `/outcome-first` and what you want.",
    ),
    "google-ads": dict(
        title="Google Ads Skill",
        pitch="Turn Claude into a Google Ads machine. Type `/google-ads` and your website. It pulls your competitors' search ads from the Google Ads Transparency Center, then rewrites your ads from what already works in your account. Three tools in one skill: the Ad Library Scraper, the Ad Writer and the Keyword Tool.",
        use="> /google-ads yourwebsite.com\n\nTo rewrite your own ads, connect your Google Ads account (Google's official Google Ads MCP server, read-only) or drop in a report exported from Google Ads.",
    ),
    "buyer-panel": dict(
        title="Buyer Panel Skill",
        pitch="Test your idea on 20 simulated buyers before you spend a dollar. Type `/buyer-panel` and your offer. A Board of 3 advisors pokes holes in the plan, a CFO works out your real margin and break-even from your numbers, and 20 simulated buyers each say buy or not buy and why. The buyers are simulated, so you test the winner on real people next.",
        use="> /buyer-panel a $500 website audit for dentists\n\nIt asks for any number it is missing, such as your costs, and never makes one up.",
    ),
    "meta-ads": dict(
        title="Meta Ads Skill",
        pitch="Find the ads your competitors keep running, then write yours from them. Type `/meta-ads` and your website. It goes through your competitors' ads in the public Meta Ad Library, picks the ones that have run the longest, and groups them by format, hook and call to action. Three tools in one skill: the Ad Library Scraper, the Ad Writer and the Creative Tool (image briefs).",
        use="> /meta-ads yourwebsite.com\n\nThe public Ad Library needs no login if Claude can use a browser tool. To rewrite your own ads and get budget moves, connect your Meta ad account (Meta's ads MCP, read-only use) or drop in a report exported from Ads Manager.",
    ),
    "captions": dict(
        title="Captions Skill",
        pitch="Captions that go behind your head and never sit under Instagram's buttons. Type `/captions` and the path to your talking head video. It makes a captioned vertical reel with HyperFrames: whisper word timings, 4 to 5 word captions on one line, you cut out on every frame so the text sits behind your head, and a measured Instagram safe zone.",
        use="> /captions ~/Desktop/my-reel.mp4\n\nNo account or API key. Everything runs on your own computer, and it needs Node.js and ffmpeg.",
    ),
    "llm-wiki": dict(
        title="LLM Wiki Skill",
        pitch="Give Claude's memory a table of contents. Run it once and it sorts your CLAUDE.md, memory files and notes into topic pages, writes an index page, and adds a short rule to CLAUDE.md so Claude reads the index first instead of guessing. Based on Andrej Karpathy's LLM Wiki idea (gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).",
        use="> /llm-wiki\n\nIt backs up your files first, never changes the originals, and asks before it edits CLAUDE.md.",
    ),
    "presell-audit": dict(
        title="Presell Audit Skill",
        pitch="Find out why your content gets views but not buyers. Paste your last posts or scripts and `/presell-audit` scores each one on three things: one single desire, the frustrations your buyer already tried, and the beliefs that stop them buying. It quotes the weak lines, rewrites them, and gives you 5 post ideas that pre-sell. Made for coaches and service businesses.",
        use="> /presell-audit\n\nThen paste your last 5 to 20 posts, scripts or captions, plus a few lines about your offer.",
    ),
}

TEMPLATE = """---
name: {title}
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# {title}

{pitch}

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

{use}

## What gets installed

- `~/.claude/skills/{name}/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/{name}/` (on Windows: `%USERPROFILE%\\.claude\\skills\\{name}\\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: {use_short}. If `/{name}` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/{name}/SKILL.md`

`````markdown
{skill}
`````
"""

USE_SHORT = {
    "search": "type `/search` and their website",
    "outcome-first": "ask for anything they want built, or type `/outcome-first` and what they want",
    "google-ads": "type `/google-ads` and their website",
    "buyer-panel": "type `/buyer-panel` and their offer",
    "meta-ads": "type `/meta-ads` and their website",
    "captions": "type `/captions` and the path to their video",
    "llm-wiki": "type `/llm-wiki`",
    "presell-audit": "type `/presell-audit` and paste in their posts",
}

for name, s in SKILLS.items():
    d = ROOT / "claude" / name
    skill = (d / "SKILL.md").read_text().rstrip()
    out = TEMPLATE.format(name=name, skill=skill, use_short=USE_SHORT[name], **s)
    assert "{" + "{" not in out and "—" not in out and "–" not in out, f"{name}: template slot left or a dash"
    blocks = re.findall(r"`````markdown\n(.*?)\n`````", out, re.S)
    assert blocks == [skill], f"{name}: SKILL.md does not round-trip"
    (d / f"{name}-skill.md").write_text(out)
    print(f"claude/{name}/{name}-skill.md: {len(out)} chars, SKILL.md round-trip OK")
