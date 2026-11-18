---
name: agents
description: Work out what a person's business should build with a big team of Claude Code sub-agents, and write the exact prompt for each build. Proposes concrete multi-agent jobs (research 100 competitor sites, enrich a lead list, rewrite a whole website, audit every ad) with the ultracode keyword and a team size, plus honest notes on cost and time. Use when someone asks what to build with agents, how to use 100 agents, or how to write an ultracode prompt.
---

# Agents

You help the person decide what to build with a team of sub-agents in Claude Code, and you write the prompt that starts it.

A sub-agent is a helper that takes one piece of a job. A team of them works at the same time and can pass notes to each other. This is good when a job has many similar pieces: 100 websites, 500 leads, 40 pages.

It is not good for one small job. If one agent can do it in a few minutes, tell the person to just ask Claude.

## 1. Check where you are

This runs in Claude Code, not in the normal chat window. If you are in a normal chat, say: "Open the Claude desktop app, click the Code tab, and run this there." Then give them the prompts anyway.

## 2. Learn the business

Ask these, one at a time, and keep them short:

1. "What does your business do, and who are your customers?"
2. "What takes your team the most hours each week? What work is the same thing done again and again?"
3. "What do you have that a team of helpers could work on? For example: a list of leads, a website, ads, customer emails, a folder of documents."
4. "What would you like to know about your market that you do not have time to look up?"
5. "How much do you want to spend, and how long can it run? A rough idea is enough."

If they do not know, show them the 10 examples below and ask which ones fit.

## 3. Propose 3 builds

Pick the 3 best fits. For each one, write:

- **What it builds:** one sentence.
- **How the team splits it:** what one agent does, how many agents, and who puts it together.
- **What you get at the end:** a folder, a spreadsheet, a report.
- **Cost and time:** an honest range (see the notes below).
- **The prompt:** exact text they can paste.

Ask which one they want. Run it only when they say yes.

## 4. How to write the prompt

Start with the word `ultracode`, then say how big the team is, then the job. Use this shape:

```
ultracode

Spin up a team of <N> sub-agents.

Goal: <one sentence about the finished result>

The work: <the list of things to work on, or where to find it>
Each agent takes: <one item, or a group of items>
Each agent must: <the exact steps, in plain words>
Each agent saves: <one file per item, in the folder <folder name>, named <how>>

When all agents are done: one final agent reads every file and writes <the combined result, for example summary.md or results.csv>.

Rules:
- Do not guess. If something cannot be found, write "not found".
- Do not send anything, post anything or delete anything.
- Show me the first 3 results before you do the rest.

Done means: <how to check it is good>
```

Why each part is there:

- **ultracode** tells Claude Code to use a team of sub-agents. If it does not seem to do anything in the person's version, replace it with the plain words "Use a team of sub-agents" and keep the rest. It works the same way.
- **The team size** is yours to choose. More agents is not always better. One agent per item is a good rule. 100 items means up to 100 agents.
- **One agent, one piece, one file.** Small, clear pieces give clean results and an easy way to check the work.
- **A final agent** puts it all together.
- **"Show me the first 3 results"** catches a bad prompt early, before you spend on the whole job.

## 5. Honest notes on cost and time

Say these plainly to the person before they start.

- **Cost:** every agent uses Claude, so 100 agents use many times what one agent uses. On a plan with a usage limit, a big run can use a large part of the limit. On an API key, it is charged by use. Claude cannot know the exact cost ahead of time.
- **Time:** it depends on the job. Small jobs can finish in minutes. A big one can run for an hour or more. Agents also wait their turn when a limit is reached, so a run can be slower than you expect.
- **Always test small first.** Run the same prompt with 5 items and 5 agents. Check the result and the cost. Then run all of it.
- **Errors happen.** Some agents will fail or return weak work. Tell the person to check a sample, and ask Claude to redo the ones that failed.
- **Facts must be checked.** For research, ask for the link where each fact was found. Open a few.
- **Do not let a big team send things.** For emails, posts and anything public, have the team write drafts, then a human sends.

## 6. Ten ready examples for business owners

Each one is a prompt to paste. Change the words in [brackets]. Put any input file in the folder you are working in first.

**1. Research 100 competitor websites**
```
ultracode
Spin up a team of 100 sub-agents.
Goal: a clear picture of how my competitors sell.
The work: the list of websites in competitors.csv, one per row.
Each agent takes one website and reads its home page, pricing page and about page.
Each agent saves one file in the folder competitors/ named after the site, with: what they sell, their prices, who it is for, their main promise, and what looks weak.
Then one final agent reads all files and writes summary.md: the 10 most common promises, the price range, and 5 gaps nobody covers.
Rules: do not guess, write "not found" if a page is missing. Show me the first 3 files before the rest.
```

**2. Enrich a lead list**
```
ultracode
Spin up a team of 50 sub-agents.
Goal: add useful facts to every lead in leads.csv.
Each agent takes 10 rows. For each row, it opens the company website and writes: what the company does in one line, its size if shown, and one thing worth mentioning in a first message.
Each agent saves its rows to enriched/part-<number>.csv. A final agent joins them into enriched-leads.csv.
Rules: use only what is on the website. Do not invent. Do not contact anyone.
```

**3. Rewrite every page of a website**
```
ultracode
Spin up a team of 20 sub-agents.
Goal: new text for every page of [my site], in my voice, to get more customers.
The work: the page files in the folder site/.
Each agent takes one page, keeps the facts, and rewrites the text in plain English, with one clear next step for the visitor.
Each agent saves the new page in site-new/ with the same file name. Never change the original.
A final agent checks that every page has a heading, a clear next step, and no missing facts, and lists any problems.
```

**4. Audit every ad you run**
```
ultracode
Spin up a team of 30 sub-agents.
Goal: find out which of my ads are weak and why.
The work: the ads in ads.csv (headline, text, picture description, results).
Each agent takes one ad and scores it: is the promise clear, is there a reason to act now, does it match the landing page. It saves a short note in ad-audit/.
A final agent writes summary.md: the 5 best ads and why, the 5 worst and why, and 10 new ad ideas based on the best.
```

**5. Answer every old customer email**
```
ultracode
Spin up a team of 40 sub-agents.
Goal: draft replies for the customer emails in the folder inbox-export/.
Each agent takes one email and writes a short, kind draft reply using the answers in faq.md.
If the answer is not in faq.md, the agent writes "needs a human" and says what is missing.
Save drafts in drafts/. Do not send anything.
```

**6. Turn one long video or podcast into content**
```
ultracode
Spin up a team of 10 sub-agents.
Goal: use transcript.txt to make posts.
Each agent takes one section of the transcript and writes: 3 post ideas, 1 short script, and the best quote from that section.
A final agent picks the 15 best ideas and orders them by how strong the first line is.
```

**7. Read every review and find what customers want**
```
ultracode
Spin up a team of 25 sub-agents.
Goal: understand what customers love and hate.
The work: the reviews in reviews.csv.
Each agent takes 40 reviews and counts the reasons people praise or complain, with 3 real quotes each.
A final agent writes summary.md: top 10 praises, top 10 complaints, and 5 changes worth making.
```

**8. Check every page of your site for problems**
```
ultracode
Spin up a team of 30 sub-agents.
Goal: find broken or weak pages on [my site].
Each agent takes a group of pages from sitemap.xml and checks: broken links, missing titles, missing descriptions, very short text, and slow-looking images.
A final agent writes fixes.md, sorted by what to fix first.
```

**9. Build a document library from a messy folder**
```
ultracode
Spin up a team of 40 sub-agents.
Goal: make my documents easy to search.
The work: the files in the folder docs/.
Each agent takes a few files and writes a one-paragraph summary, a list of the people and dates mentioned, and 5 keywords.
A final agent builds index.md, with every file listed by topic. Never move or delete the originals.
```

**10. Research a market before you launch**
```
ultracode
Spin up a team of 60 sub-agents.
Goal: understand the market for [my product idea].
Each agent takes one company, forum thread or article from a search I give it, and writes down: who the customer is, what they pay, what they complain about.
A final agent writes market.md: who buys, what they pay, what they hate, and where the gap is.
Rules: write the link for every fact.
```

## 7. After the run

- Open the final file first, then open 3 or 4 of the small files to check the work.
- Tell the person what worked, what failed, and what it cost in usage if they can see it.
- Offer to run the next build, or the same build on more items.
