# google-ads (for Claude)

**Turn Claude into a Google Ads machine.**

Type `/google-ads` and your website into Claude. It researches your industry and pulls the search ads your competitors are running right now, with their headlines and landing pages, straight out of the Google Ads Transparency Center. Connect your own Google Ads account and it rewrites your ads based on what is already working: the headlines, the keywords, the landing pages, and where to move the budget.

Three tools in one skill:

- **Ad Library Scraper:** your competitors' current search ads from the Google Ads Transparency Center, and the search words their ads go after.
- **Ad Writer:** responsive search ads (15 headlines, 4 descriptions, every character limit checked) based on what already works.
- **Keyword Tool:** a keyword plan by intent, with a negative keyword list.

**[Download google-ads-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/google-ads-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `google-ads-skill.md` in and type **set this up**.
3. Type `/google-ads yourwebsite.com`.

## Connect your Google Ads account (optional)

Google has an official, read-only Google Ads MCP server: [Google's setup guide](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server). Once it is connected to Claude Code, the skill reads your campaigns, ads, keywords and search terms by itself. It needs a Google Ads API developer token. No token yet? Export a report from Google Ads (campaigns, ads, keywords or search terms, with cost, clicks and conversions) and drop it into the chat. The skill only reads your account, it never changes it.

The Transparency Center shows ads, not bids or budgets, so competitor keywords are read from their ads and landing pages. Search volumes need your own Keyword Planner data.

Using Claude in the browser instead? Download [`google-ads-claude.zip`](https://github.com/alexgodlewski/ai-skills/releases/latest/download/google-ads-claude.zip) and upload it under Settings, Capabilities, Skills.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
