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
