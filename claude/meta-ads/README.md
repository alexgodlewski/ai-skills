# meta-ads (for Claude)

**Find the ads your competitors keep running, then write yours from them.**

Type `/meta-ads` and your website into Claude. It works out your industry, finds your competitors, and goes through their ads in the public Meta Ad Library. It looks for the ads that have been running the longest, because an ad that stays on for weeks is probably making money. It groups what it finds by format, hook and call to action. Connect your own ad account and it also rewrites your ads from what already works, and says where to move the budget.

Three tools in one skill:

- **Ad Library Scraper:** your competitors' active Facebook and Instagram ads, with start dates, formats, copy, calls to action and landing pages, grouped into patterns.
- **Ad Writer:** new primary texts, headlines and descriptions for your offer, built from those patterns and from your own results.
- **Creative Tool:** an image or video brief and a ready-to-paste image prompt for each winning format.

**[Download meta-ads-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/meta-ads-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `meta-ads-skill.md` in and type **set this up**.
3. Type `/meta-ads yourwebsite.com`.

## What you need

- **The ad library part needs no login** if Claude can use a browser tool. The Meta Ad Library is public.
- **The official Ad Library API is optional and stricter.** It needs a Meta access token, and you must confirm your identity with Meta first. For normal business ads it only returns ads shown in the European Union and the UK. If you sell elsewhere, use the web library through a browser tool, or paste ads in yourself.
- **Your own ad account is optional.** To let Claude read your results, connect Meta's ads MCP in Claude Code (you log in and approve access), or export a report from Ads Manager (campaigns or ads, with spend, results and cost per result) and drop it into the chat. The skill only reads your account. It never changes it.

## What it cannot do

- The Ad Library does not show spend, clicks or sales for most ads. "Running a long time" is a strong hint that an ad works, not proof.
- It reports the real number of ads it finds. That can be dozens or hundreds, depending on how many ads your competitors run.
- It writes image briefs and prompts. It does not make the images unless you connect an image tool and ask.

Using Claude in the browser instead? The skill needs browser and file tools, so the Code tab is the best place for it.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
