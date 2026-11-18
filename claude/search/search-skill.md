---
name: Search Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Search Skill

Get your business named in Google's AI answer. Type `/search` and your website into Claude. It sends agents to check how Google's AI sees your business, finds what is missing (reviews, service pages, the answers to the questions your customers actually ask), and then fixes it.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /search yourbusiness.com

If your website's files are open in Claude Code, it makes the changes for you after you say yes. If not, it writes every fix ready to paste.

## What gets installed

- `~/.claude/skills/search/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/search/` (on Windows: `%USERPROFILE%\.claude\skills\search\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/search` and their website. If `/search` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/search/SKILL.md`

`````markdown
---
name: search
description: Check how Google's AI answer and other AI search see a local or service business. Sends agents to search the questions customers ask and to check reviews, service pages, answers to customer questions, business details, proof and page structure, then fixes what is missing. Use when someone types /search with their website, or asks why Google or AI does not show their business, or how to get named in AI answers.
---

# Search

Google now writes an AI answer at the top of many searches, and most people never scroll past it. If that answer names a competitor, the business just lost the customer. AI answers name the businesses they can find clear proof about. This skill sends agents to check that proof, then fixes what is missing.

Be honest with the person: nobody can force an AI answer. This makes the business the easiest one for AI to trust and name.

## 1. Get the website

The website is what the person typed after `/search`. If there is none, ask for it in one line and wait.

Open the site and write down in one short block:

- the business name, what it sells, and its main services;
- the town or area it serves;
- six questions a real customer would type, for example "best plumber in [town]", "emergency plumber near me open now", "how much does [service] cost in [town]".

If something important is unclear (usually the area served), ask one short question, then continue.

## 2. Send the agents

If you can start subagents (in Claude Code: the Agent or Task tool), send these 12 agents **at the same time**, in one message. If you cannot, do the same 12 jobs yourself, one after another.

**Six search agents, one per customer question.** Each one gets the business name, the website and one question. Its job: search the web for that question, write down which businesses are named or linked at the top, and whether this business shows up. If Google shows an AI answer and the agent can see it, write down who it names. Never invent results: if it cannot search, it says so.

**Six check agents, one per area.** Each one gets the business name, the website and one area from the table. Its job: check the website and public listings for that area, mark it **OK**, **Weak** or **Missing**, and list what exactly is missing, with links as proof.

| Area | What AI looks for |
|---|---|
| Reviews | Recent reviews on Google and other sites, with words that match the services |
| Service pages | One clear page per main service, saying what it is, where, and for whom |
| Customer questions | Plain answers to the questions people actually ask (prices, timing, areas, guarantees) |
| Business details | The same name, address, phone and hours everywhere (site, Google Business Profile, directories) |
| Proof | Photos of real work, licences, years in business, real case examples |
| Structure | A page title and first paragraph that say the service and the town; schema markup (LocalBusiness, FAQPage) |

Wait for all 12. Then put their findings together and remove anything an agent could not back up with a link or a quote.

## 3. Show what is missing

Show one short report, under one screen:

1. who gets named today for the six questions, and whether this business shows up;
2. the six areas with OK, Weak or Missing;
3. the three fixes that matter most, in order.

## 4. Fix it

Then fix every Missing or Weak area.

**If the website's files are here** (a code folder or an exported site you can edit): say in a few lines what you will change and ask "Make these changes? (yes / no)". On yes, make them:

- add or expand one page per missing service (title and first paragraph with the service and the town, what is included, the area served, a price guide only if they gave one, three questions and answers);
- add an FAQ section with 6 to 10 real customer questions and plain answers;
- add LocalBusiness and FAQPage schema (JSON-LD), filled in;
- fix page titles and first paragraphs so they say the service and the town.

Then show what changed. Never publish or deploy without asking first.

**If the website's files are not here** (Wix, Squarespace, a WordPress you cannot reach): write each fix ready to paste, and say exactly where it goes.

**Fixes only the owner can make** (write them, they do the last step):

- **Reviews:** a short, friendly message to send happy customers, asking for a review that mentions the service.
- **Business details:** a list of exactly where the name, address, phone or hours do not match, and what to change each one to.

## 5. Hand over

Finish with what you changed, what they still need to do themselves (in order), and when to run `/search` again (after the changes are live and a few new reviews are in).

## Rules

- Never make up reviews, prices, licences, facts or search results. Leave a clear [fill in] where you do not know.
- Never promise a ranking or a place in the AI answer.
- Plain words. No jargon unless you explain it in the same sentence.
`````
