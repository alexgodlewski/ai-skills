# lookalike

**Drop in your customer list. Claude finds more people just like them.**

Type `/lookalike` and give it your customers (a CSV, or a pasted list of names, handles or websites). One skill, three tools:

- **Customer profiler.** Reads what your customers post in public, what they complain about and what they want, and writes it down in their own words.
- **Lookalike finder.** Searches Instagram, TikTok, X, Reddit and LinkedIn for people who say the same things, and ranks them by match.
- **Message writer.** Writes the first message for each person from the words they used.

Everything is saved as a draft: a CSV, and Gmail drafts for people who show a public email. **It never sends anything.** You read each one and decide.

**[Download lookalike-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/lookalike-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `lookalike-skill.md` in and type **set this up**.
3. Type `/lookalike` and give it your customer list.

You bring your own free [Apify](https://apify.com) account and token (`APIFY_TOKEN`). Scraping costs Apify credit. Claude tells you the estimate and tests with 10 results first.

## Limits

- Matches are guesses. The same words do not always mean the same need. You check each one.
- Public data only. Private accounts are skipped. Claude never logs in as you.
- Most people have no public email, so most messages are DMs that you paste yourself. Claude cannot send DMs.
- Platforms have rules and can block scrapers. Some runs return fewer people than asked.
- Nothing here promises replies or sales.

The source is right here: [`SKILL.md`](SKILL.md). It builds on [lead-finder](../lead-finder).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
