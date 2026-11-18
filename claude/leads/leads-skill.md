---
name: Leads
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Leads

Fill a sales calendar without buying a lead list. Type `/leads` and paste any website. It finds the businesses that fit your ideal customer on Google Maps and on their own websites (name, email, phone and LinkedIn where they are public), ranks every one against your criteria, then writes the emails in your voice and saves them as Gmail drafts. Three skills in one: `/leads`, a cold email writer and a humanizer that removes AI habits from the text.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves all three skills and tells you when it is ready.

## Then use it like this

> /leads yourwebsite.com

Claude shows you who it thinks your ideal customer is, asks for your ranking rules, tests with 10 results, then does the full run. Emails are drafts. You read them and press send yourself.

## What it needs

| What | Needed? | Why | Cost |
|---|---|---|---|
| Claude desktop app, Code tab | Yes | This is where it runs | Any paid Claude plan |
| An Apify account and token | Yes | Runs the Google Maps and website scrapers | Free plan has a small monthly credit, then you pay per use |
| Gmail connector | For the drafts | Saves the emails as drafts. You read them and press send yourself | Free |
| 2 or 3 emails you wrote | Yes, once | So the emails sound like you | Free |

Google Maps gives business details. Emails, phones and LinkedIn links only show up when the business puts them on its own website, so expect gaps.

## What gets installed

- `~/.claude/skills/leads/SKILL.md`: finds and ranks the leads.
- `~/.claude/skills/cold-email/SKILL.md`: writes the emails in your voice.
- `~/.claude/skills/humanizer/SKILL.md`: removes AI patterns from any text.

Nothing else on your computer is changed. A `leads-run/` folder is made in the folder you work in when you run it.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write files on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folders** and write each file below into its folder exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/leads` and their website. If the command does not show up in the `/` list yet, they start a new session.
4. **Remind them of the one thing they must add themselves:** their own Apify token (a free account at apify.com, then Settings, API and integrations) in the environment variable `APIFY_TOKEN`. You never ask them to paste it into a file.

### Files

### File: `~/.claude/skills/leads/SKILL.md`

`````markdown
---
name: leads
description: Find leads that fit a business's ideal customer from any website, using Apify (Google Maps and any website). Pulls name, email, phone and LinkedIn where they are public, ranks every lead against the person's criteria, then writes cold emails with the cold-email skill, cleans them with the humanizer skill, and saves them as Gmail drafts. Use when the person types /leads, pastes a website, or asks for a lead list, prospects or outbound emails.
---

# Leads

You find businesses that fit the person's ideal customer, rank them, and write the first email to each in the person's own voice. You are one of three skills that work together: `leads` (this one), `cold-email` (writes the emails) and `humanizer` (removes AI habits from the text). You never send email: you make Gmail drafts, and the person reads them and sends them.

## Before you start

Ask only for what is missing, in one short message:

1. **A website.** Either their own (so you learn what they sell) or a customer's. Read it first.
2. **Their Apify token.** Apify runs scrapers. The person makes an account at apify.com, opens Settings, then API and integrations, and copies the token. It lives in the environment variable `APIFY_TOKEN`. Never write it into a file or print it.
3. **The ideal customer.** Show what you understood from the website: the type of business, the places, the size. Ask: "Is this who you want to sell to?" Then ask for 3 to 5 **criteria** to rank by, for example "has a website", "4 stars or more", "at least 20 reviews", "in Texas", "has a contact email". Put each criterion in a table with a weight from 1 to 3.
4. **How many.** Default 100 leads. Ask before going over 500.

## Step 1: Find the leads (Apify)

Start a run with the Apify API. Replace `<ACTOR>` with the ID below (the `~` is part of the ID):

```
curl -s -X POST "https://api.apify.com/v2/acts/<ACTOR>/runs" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '<INPUT JSON>'
```

It returns a run ID and a `defaultDatasetId`. Check `GET https://api.apify.com/v2/actor-runs/<RUN_ID>` until `status` is `SUCCEEDED`. Download rows from `GET https://api.apify.com/v2/datasets/<DATASET_ID>/items?format=json`. Save everything in a folder called `leads-run/`.

Always start with a test run of 10 results and look at the rows. If Apify rejects a field, open the actor's page and read its current input fields, because actors change.

| Job | Actor ID | Main input fields |
|---|---|---|
| Businesses on Google Maps | `compass~crawler-google-places` | `searchStringsArray` (for example `["dentist"]`), `locationQuery` (for example `"Austin, Texas"`), `maxCrawledPlacesPerSearch`, `language`, `placeMinimumStars`, `website` |
| Contacts from any website | `vdrmota~contact-info-scraper` | `startUrls` (a list of `{ "url": "..." }`), `maxRequestsPerStartUrl`, `sameDomain` |
| Text of a website (for learning the offer) | `apify~website-content-crawler` | `startUrls`, `maxCrawlPages` |

All three were checked on apify.com/store on 2026-11-18 and were live. They are made by other people, not by Alex. If one is gone, search the Apify Store for the same job and tell the person what you used instead.

How it works:

1. Run the Google Maps actor for each search the person approved. You get the business name, address, phone, website, rating, review count and category.
2. For every lead that has a website, run the contact scraper on that website. It reads the contact and about pages and returns the emails, phones and social links (including LinkedIn pages) that are written there in public.
3. Merge by website. One row per business. Keep a `source` column for every email, phone and LinkedIn link (the page it came from).
4. Remove duplicates, closed places and chains the person said to skip.

Google Maps data is about businesses. Names of owners and personal LinkedIn pages are only there when the business's own website shows them. Do not claim you have the name of a decision maker when you do not. Leave the cell empty. Never guess an email by trying name patterns. Never invent a number.

## Step 2: Rank the leads

Score every lead from 0 to 100 using the criteria and weights the person gave you. Show the formula in one line. Write the score, and one short line saying why, in `leads-run/leads.csv` with these columns: name, business, email, phone, website, LinkedIn, city, rating, reviews, score, why, source.

Show the top 10 in the chat and ask: "Does this order look right?" If not, change the weights and rank again. Leads with no email still count. Tag them "call or form only".

## Step 3: Write the emails

1. If the person has not set up `cold-email` yet, ask for 2 or 3 emails they wrote themselves (real ones, or paragraphs from any messages that sound like them). Hand them to the `cold-email` skill, which learns their voice.
2. For the top leads (default 25, the person can say more), use the `cold-email` skill to write one email per lead. Each email uses a real fact about that business from the data (its city, its rating, a line from its website). No made up facts.
3. Pass every email through the `humanizer` skill before you show it.
4. Show 3 emails in the chat first. Ask: "Do these sound like you?" Fix the style, then do the rest.

## Step 4: Gmail drafts (the person sends)

Use the Gmail connector to create one **draft** per lead that has an email, with the real found address in the To field. Do not send. Then say: "N drafts are in your Gmail. Read them, change what you want, and press send on the ones you like." You cannot send them: the Gmail connector makes drafts, it does not send. If the Gmail connector is off, tell them to turn it on in Claude's connector settings, and save the emails to `leads-run/emails.md` in the meantime.

Every email needs the sender's real name and a clear way to say "no thanks". Honor every "no" at once. Keep `leads-run/sent.csv`: who, when, which email, source of the address. Never email the same lead twice without the person's say-so. Send in small batches (for example 20 a day) so the person's mailbox stays healthy.

## Limits (tell the person in plain words)

- **Cost.** Apify charges per run or per result, depending on the actor. The free plan includes a small monthly credit. Check each actor's price on its page, say the estimate, and test with 10 first.
- **How many.** Hundreds of leads in a run is normal. The number depends on the search and on your Apify plan.
- **What the data has.** Maps gives business name, phone, website, rating and reviews. Email and LinkedIn appear only when the business shows them in public. Expect gaps. A found email is not a promise that the person wants to hear from you.
- **Rules.** Google Maps and websites have terms. Scraping public pages is a gray area, and you are responsible for how you use it. Cold email is regulated (for example CAN-SPAM in the US and GDPR in Europe). This is not legal advice.
- **Replies.** Nothing here promises replies or sales. A good list and a clear email raise your chances. That is all.

## Check before you hand it over

- Every email address has a source page.
- No fact in an email is made up.
- Drafts only. The person sends them from Gmail.
- The person knows the cost and where `leads-run/` is.
`````

### File: `~/.claude/skills/cold-email/SKILL.md`

`````markdown
---
name: cold-email
description: Write cold emails in the person's own voice. Learns the voice from 2 or 3 emails or messages they wrote, then writes short first emails and follow-ups for a lead using real facts about that lead. Use when the person asks for a cold email, an outreach email, a follow-up, or when the leads skill needs emails written.
---

# Cold Email

You write the first email to a stranger so that it sounds like the person wrote it, and so that the reader can answer in one line.

## 1. Learn the voice (once)

Ask for 2 or 3 samples: emails, DMs or posts the person wrote themselves. Real ones, not polished ones. If they have none, ask them to write 3 sentences about what they do as if they were talking to a friend.

Read them and write a short **voice card**. Show it and ask "Is this you?":

- Average sentence length, in words.
- How they open and how they sign off.
- Words and phrases they use a lot. Words they never use.
- Do they use "I" or "we"? Contractions? Questions? Humor?
- How formal it is, on a scale of 1 to 5.

Save the card to `~/.claude/skills/cold-email/voice.md` so you do not ask again. If they change their mind, update it.

## 2. Gather the facts for each lead

Use only facts that are in the lead's data or on their public page: their city, their rating or reviews, a line from their website, a post they wrote. If you have no real fact, say less. Never invent a fact, a result, a client name or a number.

## 3. Write the email

- **Subject:** 2 to 5 words, lower case is fine, no tricks, no "Re:" or "Fwd:" to fool anyone.
- **Line 1:** one real thing about them. It shows you looked.
- **Line 2 or 3:** what you do, for people like them, in one plain sentence. Then one result you can truly back up. If you have none, skip it.
- **Ask:** one small question they can answer with a few words. Not "Do you have 30 minutes?" in the first email.
- **Length:** 50 to 90 words.
- **Sign-off:** the person's real name, and one line "If this is not for you, just say so and I will not write again."
- Plain words a 12 year old understands. Short sentences. Match the voice card.

## 4. Follow-ups

Write two short follow-ups (under 50 words each). The first goes 3 days later and adds one new useful thing. The second goes 4 days after that and says you will stop writing. No guilt, no "just bumping this".

## 5. Clean it

Send every email through the `humanizer` skill before you show it. Then show 3 emails and ask if they sound like the person.

## Never

- Never claim you know the lead.
- Never promise results.
- Never use fake urgency or a fake "reply".
- Never send. You write. The `leads` skill makes Gmail drafts, and the person decides what goes out.
`````

### File: `~/.claude/skills/humanizer/SKILL.md`

`````markdown
---
name: humanizer
description: Remove the habits that make text sound like AI. Rewrites emails, posts and messages so they sound like a person wrote them, by cutting a list of known AI patterns and keeping the meaning and the person's voice. Use when the person asks to humanize, de-AI or clean up text, and on every email the cold-email skill writes.
---

# Humanizer

You take text and remove the patterns that make a reader think "a machine wrote this". You keep the meaning, the facts and the person's voice. You do not make it longer.

## How to work

1. Read the text once. Mark every pattern from the list below.
2. Fix each one with a plain, plainer or shorter version. If a sentence only exists to sound smart, delete it.
3. Read it out loud in your head. Does a real person say this? If the person has a voice card (`~/.claude/skills/cold-email/voice.md`), match it.
4. Check the facts did not change. Do not add a fact, a number or a claim.
5. Return the new text. If asked, show a short list of what you changed.

## The pattern list

**Shape**
- **Correctio:** "It's not X, it's Y." "Not just a tool, a partner." Say what it is.
- **Lists of three:** "fast, simple and effective." Cut to the one that is true, or use two, or four. Real life is not always three.
- **Tidy closing line** that repeats the point or sums up the email. Delete it.
- **Same sentence length** over and over. Mix short and a bit longer.
- **Rhetorical question then answer:** "The result? Amazing." Say the result.

**Punctuation**
- **Em dashes and en dashes.** Replace with a period, a comma or "and". Zero left.
- **Too many colons and semicolons.** Use full stops.
- **Exclamation marks.** At most one, and only if the person really talks that way.
- **Emojis** unless the person uses them.

**Words**
- Words people do not say: delve, tapestry, landscape, realm, leverage, unlock, elevate, seamless, robust, holistic, game-changer, cutting-edge, navigate, foster, testament, pivotal, vibrant, journey, ecosystem, synergy.
- **Adverbs that fake depth:** quietly, deeply, truly, genuinely, fundamentally, simply, effortlessly. Delete them.
- **Purple prose:** big images and weather words for plain facts ("a symphony of results", "in the ever-changing world of"). Say the plain fact.
- **Hedges that say nothing:** "It's worth noting that", "It's important to remember", "In today's fast-paced world". Delete.
- **Fake warmth openers:** "I hope this email finds you well", "I wanted to reach out". Start with the point.
- **Empty praise:** "Great question!", "Love what you are doing!" with nothing behind it. Say the one real thing.

**Email only**
- **Flattery without a fact.** Replace with one real detail or delete.
- **Big promises.** "Double your revenue" with no proof. Cut it or state what is true.
- **Three CTAs.** Keep one.

## Examples

Before: "I hope this finds you well! I wanted to reach out because your bakery is not just a shop, it's a community hub, and I help businesses like yours grow, scale and thrive."
After (an example, the numbers are made up): "Hi Sam. I saw your bakery has 4.8 stars from 212 reviews. I help local shops get more repeat customers. Can I send you one idea?"

Before: "Our seamless, cutting-edge platform quietly transforms your workflow."
After: "It saves your team about an hour a day on scheduling." (Only if that is true and the person can back it up. If not, cut the sentence.)

## Final check

- Zero em or en dashes.
- No word from the list.
- Not longer than the original.
- Every fact is still the person's fact.
`````
