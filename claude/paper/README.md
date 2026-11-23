# paper

**Any scanned document turns into text Claude can read.**

Type `/paper` and point it at a file or a whole folder of old invoices, quotes and letters (PDF, jpg, png or heic). Claude reads them, makes a searchable text copy of each one, and builds an index in a folder next to your scans. Then you ask:

- What did we quote this customer in 2022?
- Which invoices this month never got paid?

It answers from the paper and tells you the file and the page every answer came from.

The reading happens on your own computer. No page goes to a cloud reading service, so the reading is free, however many pages you have. (When Claude answers a question, the text of the pages it opens goes to Claude, like any file you open in Claude.)

**[Download paper-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/paper-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `paper-skill.md` in and type **set this up**.
3. Type `/paper` and the path of a file or folder.

## What you need

- A Mac is the main case. It uses the text recognition that is already built into macOS. It also needs Apple's free Command Line Tools. Claude asks before it installs them.
- On Windows or Linux, Claude uses the free program Tesseract instead. It asks before it installs it.
- Nothing to pay, no account, no key.

## Limits

- Handwriting and bad scans may read wrong. Claude marks numbers it doubts, and you check the original page.
- It takes about one to three seconds a page. Thousands of pages take a while.
- The index (dates, amounts, names) is found by simple patterns. It is a map, not the truth. Claude reads the page before it answers.
- It never changes or deletes your scans. New files go in a `paper-text` folder.

The source is right here: [`SKILL.md`](SKILL.md), [`paper_ocr.swift`](paper_ocr.swift) and [`paper_index.py`](paper_index.py).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
