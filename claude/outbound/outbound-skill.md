---
name: Outbound Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Outbound Skill

Type `/outbound` and your website. Claude reads the site, writes your ideal customer profile, then builds an assembly line of agents: one team finds the leads, one finds their emails, one writes the emails, and the last one gets them ready to send (Gmail drafts and a CSV). You say how big each team is, for example "build me 100 agents". It never sends: you read the drafts and answer the people who reply.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /outbound yourwebsite.com

Or set the team sizes: `/outbound yourwebsite.com 5/5/5/2`, or say "build me 100 agents". The default is small (3/3/3/1). Test small first: big teams use a lot of Claude usage.

## What it needs

Claude Code and a paid Claude plan. Optional: an Apify token (Google Maps leads), the Gmail connector (drafts), and the `leads` skill (`leads-skill.md`) for the cold email writer and humanizer. Without them it still works: web search, a CSV and plainer emails.

## What gets installed

- `~/.claude/skills/outbound/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/outbound/` (on Windows: `%USERPROFILE%\.claude\skills\outbound\`) and write the file below into it exactly as it is. If the folder already has a SKILL.md, ask before you replace it.
3. **Offer the extra skills.** If `~/.claude/skills/cold-email/` and `~/.claude/skills/humanizer/` are missing, say: "For better emails, also add leads-skill.md from github.com/alexgodlewski/ai-skills (claude/leads). This works without it."
4. **Tell them it is ready**, and how to use it: type `/outbound` and their website, with a team size if they have one. If `/outbound` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/outbound/SKILL.md`

`````markdown
---
name: outbound
description: Build an outbound assembly line from a website. Reads the site, writes the ideal customer profile, then runs four teams of sub-agents in waves (lead finders, email finders, email writers, a sender), in the sizes the person asks for ("build me 100 agents"). Saves leads with a score, a personal email for each, a run log and a CSV in an outbound/ folder, and makes Gmail drafts. Never sends. Use when the person types /outbound, pastes a website and asks for outbound, cold email at scale, or a team of agents that finds leads and writes to them.
---

# Outbound

You turn a website into an assembly line of sub-agents. One team finds leads. One team finds their emails. One team writes a personal email to each. One team gets them ready to send. You run the teams in waves and save everything to files, so a big run can stop and start again.

You never send an email. "Ready to send" means Gmail drafts and a CSV. The person reads and sends.

This skill uses parts of three other skills. Do not copy them. Read them from disk when you need them:

- `leads` for the Apify steps (Google Maps and contact scrapers), ranking, and the send rules.
- `cold-email` for the voice card and the shape of the email.
- `humanizer` for the pass that removes AI habits.

They are all in `leads-skill.md` from https://github.com/alexgodlewski/ai-skills/tree/main/claude/leads. They live in `~/.claude/skills/leads/`, `~/.claude/skills/cold-email/` and `~/.claude/skills/humanizer/`.

## 0. Check where you are

1. You need Claude Code with the Agent tool (older versions call it Task). In a normal chat, say: "Open the Claude desktop app, click the Code tab and run this there." Stop.
2. Look for an `outbound/` folder in the current folder. If it has a `run-log.md`, this is a **resume**: read the log and `leads.csv`, tell the person in two lines where it stopped, and carry on from the next unfinished batch (see "Stop and resume").
3. Check that `~/.claude/skills/cold-email/SKILL.md` and `~/.claude/skills/humanizer/SKILL.md` exist. If not, say: "For the best emails, add the `leads` skill too (leads-skill.md in the same repo). I can go on without it, with plain short emails." If they say go on, use the short rules in step 5.

## 1. Read the website and write the ideal customer profile

Ask only for what is missing: the website.

Fetch the home page, the offer pages and the about page. Write `outbound/profile.md` and show it:

- **What they sell**, in one sentence.
- **Who buys:** the type of business, the job title of the person who decides, the size. Say what you saw on the site, and what you are guessing.
- **Where they are:** the cities, the regions, the places on the web to look.
- **Pains:** 3 to 5 problems this buyer has, in plain words they would use. Use only what the site or real search results support.
- **Search ideas:** 8 to 12 phrases a finder agent can search (for example "[type of business] in [city]").
- **Ranking criteria:** 3 to 5 things that make a lead a better fit, each with a weight from 1 to 3 (for example "has a website", "4 stars or more", "in Texas", "shows a contact email").

Ask: "Is this who you want to sell to?" Fix it. Do not start a team until they say yes.

Also ask once, and save to `outbound/sender.md`: the sender's real name, the business name, a real mailing address, and the opt-out line they want (default: "If you do not want emails from me, reply 'no' and I will not write again."). Never invent an address. If they have none, say it is needed (see "Why you never send").

## 2. Set the team sizes

Take the sizes from the prompt if they gave them. Otherwise ask in one line: "How big should each team be? Default is 3 finders, 3 email finders, 3 writers and 1 sender."

- Four numbers, like "5/5/5/2": use them.
- One number, like "build me 100 agents": split it 30% finders, 30% email finders, 30% writers, 10% sender. 100 becomes 30/30/30/10. Round, keep at least 1 per team, and make the total match what they asked.
- Nothing said: use 3/3/3/1.

Each finder agent covers one search slice (one search phrase in one place) and returns up to **20 leads** (the person can change this). So the most leads one round can produce is finders times 20, before duplicates and misses. Say that number. 30 finders is up to about 600 leads in a round, not "thousands". To work through thousands, run more rounds with new search slices. You can say a run covers thousands only after the files show it did.

Show a plan table: team, number of agents, what each does, leads per agent. Then say the truth about cost and time:

- Every agent uses Claude, so 100 agents use many times what one agent uses. You cannot know the exact cost ahead.
- Claude Code runs a limited number of agents at once, so a big team runs in waves. It takes longer than you may expect.
- Do a **test first** with 3/3/3/1 and 10 leads. Show the result. Then run the real size. Ask before going over 30 agents in one go.

Get a yes before you launch the team.

## 3. The files

Everything goes in `outbound/`:

```
outbound/
  profile.md        the ideal customer profile
  sender.md         name, business, address, opt-out line
  plan.md           team sizes, leads per agent, the search slices
  leads.csv         the master list (one row per lead)
  work/             one file per agent, named by team and number
  emails/           one file per lead: <id>.md
  send-ready.csv    the CSV for import
  do-not-contact.csv  anyone who said no (never write to them)
  run-log.md        what ran, when, how many came back
```

`leads.csv` columns: `id, business, website, city, category, contact_name, contact_role, email, email_status, email_source, score, why, source_url, stage, draft`.

- `email_status` is `found` (seen on a page), `guess` (built from a pattern) or `none`.
- `stage` is `found`, `emailed`, `written`, `drafted` or `skipped`.

Rules for the files:

- Sub-agents write only to their own file in `work/` (or their own `emails/<id>.md`). They never edit `leads.csv`. You merge, so two agents never write the same file.
- Use Python's `csv` module to read and write CSVs so commas and line breaks are quoted right.
- After every wave, add a line to `run-log.md`: time, team, wave number, agents sent, files that came back, rows added, failures.

## 4. Run the teams, in waves

Run the teams in order. Each team starts when the one before it is merged. Within a team, send agents in **waves of up to 10 at a time**: put up to 10 Agent calls in one message so they run side by side, wait for them, check the files, then send the next wave. Give each agent only its own piece and the files it needs. Tell every agent: use only what you can see, write "not found" when you cannot find it, and never contact anyone.

If an agent fails or returns nothing, note it in the log and send one more agent for the same piece. Do not retry more than once.

### Team 1: Finders

One agent per search slice. Each gets `outbound/profile.md`, its slice, the lead target, and the path to `leads.csv` so it can skip businesses already there.

Each finder:

1. Uses web search to find real businesses that match the profile in its slice. Opens each website to check that the business exists and fits.
2. Scores each lead from 0 to 100 using the weights in `profile.md`, with one short line for why. Never invent a rating, a review count or a fact. Leave a cell empty if it is not known.
3. Writes `outbound/work/finders-NN.csv` with: `business, website, city, category, score, why, source_url`.

**Optional, Apify.** If `APIFY_TOKEN` is set, finders can use the Google Maps actor `compass~crawler-google-places` as the `leads` skill describes. Follow `~/.claude/skills/leads/SKILL.md` for the calls. Test 10 results first, and tell the person the cost. If the token is empty, use web search only. Never write the token in a file or print it.

Then you merge: add the rows to `leads.csv`, remove duplicates by website domain, give each lead an id (`L0001`, `L0002`, and so on), set `stage` to `found`.

### Team 2: Email finders

Split the leads without an email into pieces of about 10. One agent per piece.

Each email finder, for each lead:

1. Opens the home page, the contact page, the about page, the team page and the footer.
2. Writes down every email that is shown on a page, with the page address in `email_source`. Prefer a named person who decides (owner, founder, head of the area from the profile). A general address like info@ is fine when it is all there is. Set `email_status` to `found`.
3. If there is no email but there is a named person, and another real email on the same site shows the pattern (for example first.last@), it may write the pattern address. It sets `email_status` to `guess` and writes the pattern it used. It never guesses with nothing to base it on.
4. If there is nothing, set `email_status` to `none` and save the contact form address if there is one. These leads are "call or form only".
5. Does not log in, does not get around a block, and does not scrape social media accounts.

Output: `outbound/work/emails-NN.csv` with `id, contact_name, contact_role, email, email_status, email_source`. You merge it into `leads.csv` and set `stage` to `emailed`.

**Guesses are risky.** A wrong address bounces, and bounces hurt the sender's name with mail providers. Guesses stay in the CSV, marked `guess`. They do not become Gmail drafts unless the person says so. Suggest they check the guesses with an email verifier first.

### Team 3: Writers

Split the leads with `found` (and `guess`) emails into pieces of about 10, best score first. One agent per piece. Skip anyone in `do-not-contact.csv`.

Each writer reads the voice card (`~/.claude/skills/cold-email/voice.md`), `~/.claude/skills/cold-email/SKILL.md`, `~/.claude/skills/humanizer/SKILL.md`, `outbound/profile.md` and `outbound/sender.md`.

If there is no voice card yet, you get one **before** this wave, once, as the `cold-email` skill says: ask for 2 or 3 real emails the person wrote, write the voice card, and ask "Is this you?". Do not send writers out without it.

For each lead, the writer:

1. Opens the lead's website and finds one real fact to mention (a city, a rating, a line on the site, a service they list). If there is no real fact, it says less. It never invents a fact, a result, a client or a number.
2. Writes one personal email: subject of 2 to 5 words, first line is the real fact, then one plain sentence about what the person sells and one small question. 50 to 90 words, in the voice card.
3. Passes it through the humanizer rules (no dashes, no "not X, it's Y", no hype words).
4. Adds the sign-off: the sender's name, business, address and the opt-out line from `sender.md`.
5. Saves `outbound/emails/<id>.md`: the first lines are `to:`, `subject:` and `fact_source:`, then a blank line, then the body.

You check 3 emails from the first wave yourself against the profile and show them to the person: "Do these sound like you?" Fix the style before the rest run. Then set `stage` to `written`.

If the short rules apply (no cold-email skill): short sentences, plain words, one real fact, one question, 50 to 90 words, no dashes, no hype.

### Team 4: Sender

This team gets the emails ready to send. It does not send.

1. **Gmail connector on:** split the written emails into pieces of about 10, best score first. Each sender agent creates one Gmail **draft** per email, with the found address in the To field. No sending. It writes `outbound/work/sender-NN.csv` with `id, draft_status, note`. Default is drafts for the top 50 leads by score (the person can say more). Thousands of drafts in one inbox is hard to read, so the rest stay in the CSV. If the sender agents cannot reach the Gmail connector, make the drafts yourself in the main session.
2. **Gmail connector off:** tell the person to turn it on in Claude's connector settings if they want drafts. Do not stop: the CSV is enough.
3. **Always:** write `outbound/send-ready.csv` with `to, subject, body, name, business, website, score, email_status, email_source`. Only `found` emails are in it. Guesses go in a second file, `outbound/guesses.csv`, for the person to check. Build both with Python's `csv` module.

Set `stage` to `drafted` (or `skipped`, with a reason in `why`).

## 5. Why you never send

Say this to the person in plain words at the start and at the end.

- **Deliverability.** If one mailbox sends hundreds of cold emails fast, mail providers learn to put its mail in spam. Real replies from real customers then go there too. Send a small batch a day (for example 20) from a mailbox you can afford to protect, and watch the bounces.
- **The law.** Cold email is regulated. In the US, CAN-SPAM says the email must say truthfully who sent it, must not have a misleading subject, must include a real mailing address, and must give an easy way to opt out that you honor. In Europe, GDPR is stricter and can need a legal reason to write to someone. This is not legal advice. Ask a lawyer if you are not sure.
- **So:** every email has the sender's real name, address and an opt-out line. Any "no" goes into `do-not-contact.csv` at once. Never write to the same lead twice without the person saying so.

## 6. Stop and resume

- A batch is done when its output file exists in `work/` (or its `emails/<id>.md` exists). On resume, skip those and send only what is missing.
- `leads.csv` `stage` shows where each lead is. `run-log.md` shows the last wave.
- The person can say "stop after this wave" at any point. Finish the wave, merge, log, and say how to continue: type `/outbound` in the same folder.

## 7. What to tell the person at the end

- The numbers from the files: leads found, emails found, how many are guesses, emails written, drafts made. Count them from the files. Do not round up.
- Where everything is: `outbound/leads.csv`, `outbound/send-ready.csv`, `outbound/emails/`.
- What to do next: read the drafts, change what you want, send a small batch yourself, and answer the people who reply. Claude does not read or answer replies in this skill. To sort replies, paste them into `/lead-heat`. For a lead that went quiet, use `/revive`.

## Limits (say them in plain words)

- **It finds fewer leads than the plan says if the web does not have them.** Web search finds businesses that have a site. Apify finds more.
- **Emails are only as good as what is on public pages.** Expect gaps. A found email does not mean the person wants to hear from you.
- **Agents can be wrong.** Check 10 leads and 10 emails by hand before you send any.
- **Cost.** Big teams use a lot of Claude usage, and Apify has its own price. Test small first.
- **Nothing here promises replies or sales.**

## Check before you hand it over

- The person said yes to the profile and to the team sizes.
- Every email address has a source page, and guesses are marked.
- No fact in any email is made up.
- No dashes in the emails.
- Every email has the sender's name, address and opt-out line.
- Nothing was sent.
`````
