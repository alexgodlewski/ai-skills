# seo (for Claude)

**See exactly why Google is not sending you customers.**

Type `/seo` and your website into Claude. It crawls your site, checks every page, shows the searches you show up for and the searches your competitors win that you do not, then ranks every fix with the biggest wins first. Give it access to your website and it can make the fixes for you: page titles, descriptions and the pages you are missing.

Three tools in one skill:

- **SEO Audit:** crawls your sitemap and links (up to 100 pages) and checks each page: title, description, H1, word count, indexable or not, status and missing alt text. Then the site-wide checks, the searches you show up for, the searches your competitors win, and one fix list ranked by impact and effort.
- **Keyword Finder:** seed terms from your site, Google autocomplete and People also ask, competitor page titles and search intent. It groups the terms into pages and says which pages you already have, which are weak and which are missing.
- **Page Writer:** new titles and descriptions with every length checked, plus the missing pages (service pages, town pages, FAQ). With your site files it shows a diff and edits them after you say yes. Without them it gives you ready-to-paste text.

**[Download seo-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/seo-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `seo-skill.md` in and type **set this up**.
3. Type `/seo yourwebsite.com`.

## Use your real numbers (optional, free)

The searches you show up for come from **Google Search Console**. Verify your site there (it is free), open Performance, and export Queries and Pages as CSV for the last 3 months. Drop the files into the chat. You can also connect Search Console to Claude Code if you have a connector. Without it, that part of the audit is clearly marked as estimated, and nothing is made up.

## What it can and cannot do

- It does not invent search volumes. Volumes show up only if they come from your Search Console file or a tool you have (Keyword Planner, Semrush, Ahrefs).
- It sees competitors through normal web searches, so results can differ a little from what your customers see in their own town.
- It reads the HTML of each page. A site that builds its text only with JavaScript may need a browser tool.
- Page speed is only reported if it can run a real test.
- It can edit your site only if the files (or a connection to your site) are open in Claude Code. It shows the diff and asks first. It never publishes by itself.
- Nobody can promise a ranking. SEO takes weeks to show.

For Google's AI answers, use the [search](../search) skill.

Using Claude in the browser instead? It needs the Code tab to read your files and crawl many pages.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
