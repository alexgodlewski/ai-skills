---
name: Lead Finder
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Lead Finder

Claude scrolls social media and finds you customers. Type `/lead-finder` and paste your website. It reads who you sell to, finds people who talk about that problem on Instagram, TikTok, LinkedIn, X and Reddit, writes each person's pains, dreams and objections in their own words, finds their public contact details, and drafts the outreach in your Gmail. Four parts in one skill: a scraper, a profile builder, an email finder and a sender.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /lead-finder yourwebsite.com

Start small. Claude tests with 10 results, shows you the cost, and asks before it does a big run.

## What it needs

| What | Needed? | Why | Cost |
|---|---|---|---|
| Claude desktop app, Code tab | Yes | This is where it runs | Any paid Claude plan |
| An Apify account and token | Yes | Runs the scrapers | Free plan has a small monthly credit, then you pay per use |
| Gmail connector | For the sender | Saves outreach as drafts. You read them and press send yourself | Free |
| An email finder account (Hunter, Apollo or similar) | Optional | Finds more emails than public pages show | Their price, your own key |

It cannot send DMs on Instagram, TikTok, X or LinkedIn. It writes them for you to paste. Many people have no public email, so expect to find one for only some of the list.

## What gets installed

- `~/.claude/skills/lead-finder/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.
- A `lead-finder-run/` folder is made in the folder you work in when you run it, with your profiles and drafts.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write files on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/lead-finder` and their website. If the command does not show up in the `/` list yet, they start a new session.
4. **Remind them of the one thing they must add themselves:** their own Apify token (a free account at apify.com, then Settings, API and integrations) in the environment variable `APIFY_TOKEN`. You never ask them to paste it into a file.

### File: `~/.claude/skills/lead-finder/SKILL.md`

`````markdown
---
name: lead-finder
description: Find customers on social media from a website. Reads the website to learn who the business sells to, scrapes public posts and comments with Apify, writes each lead's pains, dreams and objections in their own words, finds public contact details, and drafts outreach in Gmail for approval. Use when the person types /lead-finder, pastes their website and asks for leads, customers, a lead list or outreach.
---

# Lead Finder

You turn a website into a list of real people who might buy, with proof in their own words, and then you draft the first message to each one. You have four parts: a scraper, a profile builder, an email finder and a sender. The sender writes drafts only. Claude cannot send email or DMs for the person: they read the drafts and press send themselves.

## Before you start

Ask only for what is missing, in one short message:

1. **The website.** The person pastes it.
2. **Their Apify token.** Apify is a service that runs scrapers. The person makes a free account at apify.com, opens Settings, then API and integrations, and copies the token. Tell them to put it in an environment variable called `APIFY_TOKEN` (or paste it once in this chat). Never write the token into a file you create, never print it back.
3. **A size for this run.** Default: 100 profiles. Say what it costs (see "Limits") and get a yes before you scrape more than 500.

Read the token from `$APIFY_TOKEN`. If it is empty, stop and ask. Do not guess.

## Part 1: Learn who they sell to

Fetch the website. Read the home page, the offer pages and the about page. Write a short brief and show it:

- What they sell, in one sentence.
- The one best customer: who they are, what they do, what they are stuck on.
- 8 to 12 words and phrases this customer would type or say when they have the problem (not the company's own words).
- Which platforms this customer is on. Pick the 2 or 3 that fit. Do not scrape all of them for the sake of it.

Ask: "Is this the right customer?" Fix it if not. Do not scrape until they say yes.

## Part 2: The scraper

Use Apify actors. Call them with the Apify API. Replace `<ACTOR>` with the ID in the table (the `~` is part of the ID):

```
curl -s -X POST "https://api.apify.com/v2/acts/<ACTOR>/runs" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '<INPUT JSON>'
```

That starts a run and returns a run ID and a `defaultDatasetId`. Check the run with `GET https://api.apify.com/v2/actor-runs/<RUN_ID>` until `status` is `SUCCEEDED`. Then download the rows with `GET https://api.apify.com/v2/datasets/<DATASET_ID>/items?format=json`. Save the rows in a folder called `lead-finder-run/` in the current folder. If a run fails, show the message and tell the person. Do not retry more than once.

Always start with a small test run (`10` items) and look at the rows before the full run. Actor settings can change, so if a field name is rejected, open the actor's page at `https://apify.com/<owner>/<name>` and read its current input fields.

| Platform | Actor ID | Use it for | Main input fields |
|---|---|---|---|
| Instagram | `apify~instagram-scraper` | Posts and profiles from hashtags or accounts | `search`, `searchType` (`hashtag`, `user` or `place`), `directUrls`, `resultsType`, `resultsLimit` |
| Instagram comments | `apify~instagram-comment-scraper` | The comments under a post | `directUrls`, `resultsLimit` |
| TikTok | `clockworks~tiktok-scraper` | Videos, profiles and comments from hashtags, search words or accounts | `hashtags`, `searchQueries`, `profiles`, `resultsPerPage`, `commentsPerPost` |
| TikTok comments | `clockworks~tiktok-comments-scraper` | Comments under given video links | `postURLs`, `commentsPerPost` |
| LinkedIn | `harvestapi~linkedin-post-search` | Public posts that match search words, with the author, and optionally comments | `searchQueries`, `maxPosts`, `scrapeComments`, `maxComments`, `postedLimit` |
| X (Twitter) | `apidojo~tweet-scraper` | Posts and replies that match search words | `searchTerms`, `maxItems`, `sort`, `tweetLanguage` |
| Reddit | `trudax~reddit-scraper-lite` | Posts and comments that match search words, in chosen subreddits | `searches`, `searchCommunityName`, `searchPosts`, `searchComments`, `sort`, `maxItems` |

These actors were checked on apify.com/store on 2026-11-18 and all were live then. They are made by other people and Apify, not by Alex. If one is gone or renamed, search the Apify Store for the same job and tell the person which one you swapped in.

How to pick searches: use the customer's own phrases from Part 1 as `searchTerms`, `searchQueries` and `searches`, not the company's product name. Look for people with the problem, not for competitors. Keep the people who talk about the problem, skip accounts that sell the same thing.

Public data only. Do not log in as the person to any platform. Do not use anyone's cookies or password.

## Part 3: The profile builder

For every person who passed the filter, build one profile from what they wrote. Read their posts and comments in full. Write:

- **Who:** name or handle, platform, a link to the post, what they do if they say it.
- **Pains:** what is hurting them. At least one **exact quote** per pain, in quotation marks, copied word for word from the rows.
- **Dreams:** what they want. Exact quote.
- **Objections:** what would make them say no or wait ("too expensive", "tried it before", "no time"). Exact quote if they said one. If they did not, write "none seen". Never make an objection up.
- **Fit score** from 1 to 5 against the customer in Part 1, with one line saying why.
- **Link to the quote's source** so the person can check it.

Rules for profiles:

- A quote must exist in the data. Copy it. If you are not sure, leave it out.
- Do not guess a person's age, health, money, religion, politics or other private facts.
- Use only what the person posted in public.
- Skip anyone who looks under 18, and skip private or business-closed accounts.

Then write one summary for the whole list: the 5 pains that came up most, the 5 dreams, the 5 objections, each with 2 or 3 quotes. This is the part the person can use for ads, pages and sales calls even if they never message anyone.

Save profiles as `lead-finder-run/profiles.csv` (one row per person) and `lead-finder-run/summary.md`.

## Part 4: The email finder

Find a way to reach each person, in this order. Stop at the first one that works.

1. **Their own public pages.** If the profile has a website, run `vdrmota~contact-info-scraper` on it. Input: `startUrls` (a list of `{ "url": "..." }`), `maxRequestsPerStartUrl` (for example 5), `sameDomain` true. It reads the contact and about pages and returns emails, phones and social links that are written there in public.
2. **The link in their bio.** If the bio links to a page, treat that as a website and do step 1.
3. **An enrichment service, only if the person wants it.** Ask once: "I found emails for X of Y people from public pages. If you have an account with an email finder (for example Hunter or Apollo), I can use your own API key for the rest. Want that?" Use only a service they pick and a key they give you. Do not buy or sign up for anything for them. Say what it costs per lookup before you run it.
4. **None found.** Mark the row "no email". For these, you can still write a DM (see Part 5).

Never guess an email by trying name patterns and sending to see what bounces. Never write an email down unless you found it on a page or got it from the person's own service. Put the source next to every email (the page link or the service name).

## Part 5: The sender

Write the first message for each person you have a contact for. Each message must be built from that person's own words.

- Open with something specific they said, in your own words or a short quote. Show you read it.
- Say in one sentence how you can help with that exact problem. No hype.
- One small ask, for example "Want me to send the 2-page guide?". Not a call booking in the first message.
- 60 to 90 words. Plain words. No fake flattery. No claim you cannot back up.
- Tell the person in your note to them which quote each message uses.

**Email.** Use the Gmail connector to create a **draft** for each email. Subject lines are short and plain. Put the person's real, found address in the To field. Do **not** send. After the drafts exist, tell the person: "N drafts are in your Gmail. Read them, change what you want, and press send on the ones you like." You cannot send them: the Gmail connector makes drafts, it does not send. If the Gmail connector is not on, tell them how to turn it on in Claude's connector settings, and in the meantime write all messages to `lead-finder-run/outreach.md`.

**DMs.** You cannot send DMs on Instagram, TikTok, X or LinkedIn. Write the DM text, with a link to the person's profile, in `lead-finder-run/outreach.md` for the person to paste by hand. Do not try to automate DMs with scripts or someone's login. Platforms ban accounts that do this.

Keep a log in `lead-finder-run/sent.csv`: who, when, which message, the source of the contact. Never message the same person twice without the person's say-so.

## Limits (tell the person these in plain words)

- **Cost.** Apify charges for compute or per result, depending on the actor. A free Apify account comes with a small monthly credit. Check each actor's pricing on its page. 10,000 profiles costs real money. Do the test run first and say the estimate before the big run.
- **How many.** "Thousands" is possible on paper. In practice it depends on your Apify plan and on how many public posts match your words. Fewer, better-fit people beat a huge messy list.
- **Platform rules.** Scraping public data is a gray area on some platforms, and their terms may not allow it. The person is responsible for how they use it. Private accounts and content behind a login are out of reach.
- **Rate limits and blocks.** Platforms slow or block scrapers. Runs can return fewer rows than asked. Actors can break when a platform changes. If so, say so, do not invent rows.
- **Emails.** Many people have no public email. Expect to find one for a minority of the list. A found address is not a promise that the person wants to hear from you.
- **Law.** Cold email and data about people are regulated (for example CAN-SPAM in the US, GDPR in Europe). Every email needs the sender's real name and a clear way to say "no more". Honor every "no" at once. This skill is not legal advice.
- **What it cannot do.** It cannot promise replies or sales. It does not read private messages. It does not send DMs for you.

## Check before you hand it over

- Every quote in the profiles appears in the scraped data.
- Every email has a source.
- No message went out. Gmail has drafts only, and the person sends them.
- The person knows the cost of the run and where the files are.
`````
