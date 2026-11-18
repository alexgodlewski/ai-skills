# leads

**Claude can now pull the leads that fit your ideal customer, rank them, and write the emails in your voice.**

Type `/leads` and paste any website. It finds the businesses that fit your ideal customer on Google Maps and on their own websites (name, email, phone and LinkedIn where they are public), ranks every one against your criteria, and writes a short email to each in your voice. Emails are saved as Gmail drafts: you read them and press send yourself. It runs on [Apify](https://apify.com), so you never buy a lead list.

Three skills in one file:

- [`leads`](SKILL.md): finds and ranks the leads.
- [`cold-email`](cold-email/SKILL.md): learns your voice from 2 or 3 emails you wrote, then writes the emails.
- [`humanizer`](humanizer/SKILL.md): removes AI habits (the "not X, it's Y" line, long dashes, lists of three, "quietly", purple prose).

**[Download leads-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/leads-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `leads-skill.md` in and type **set this up**.
3. Type `/leads yourwebsite.com`.

You bring your own free Apify account and token (`APIFY_TOKEN`). Scraping costs Apify credit, and Claude tells you the estimate and tests with 10 results first. Google Maps gives business details. Emails and LinkedIn links appear only when a business shows them in public, so expect gaps. Nothing here promises replies or sales.

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
