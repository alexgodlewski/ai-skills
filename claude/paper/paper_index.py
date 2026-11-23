#!/usr/bin/env python3
"""Build index.csv from the text files that paper_ocr made.

  python3 paper_index.py <text-folder> <index.csv>

One row per page: file, page, dates found, amounts found, names found (guesses), first words.
Names come only from labels such as "Bill to" or "Customer". Anything else stays empty:
Claude reads the page text when a question needs more.
"""
import csv, os, re, sys

MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
DATE = re.compile(rf"\b(?:{MONTH}\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}|\d{{1,2}}\s+{MONTH}\s+\d{{4}}|\d{{4}}-\d{{2}}-\d{{2}}|\d{{1,2}}[/.]\d{{1,2}}[/.]\d{{2,4}})\b", re.I)
AMOUNT = re.compile(r"(?:[$€£]\s?\d[\d,]*(?:\.\d{2})?|\b\d[\d,]*\.\d{2}\s?(?:USD|EUR|GBP|PLN)\b)")
NAME = re.compile(r"(?:bill(?:ed)? to|sold to|customer|client|attn|attention|prepared for|quote for|dear)\s*[:\-]?\s*([^\n]{2,60})", re.I)


def pages(text):
    parts = re.split(r"^=== Page (\d+) ===\s*$", text, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        yield int(parts[i]), parts[i + 1].strip()


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    folder, out = sys.argv[1], sys.argv[2]
    rows = 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "page", "dates", "amounts", "names_guess", "first_words"])
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".txt"):
                continue
            text = open(os.path.join(folder, name), encoding="utf-8", errors="replace").read()
            for page, body in pages(text):
                dates = "; ".join(dict.fromkeys(DATE.findall(body)))
                amounts = "; ".join(dict.fromkeys(a.strip() for a in AMOUNT.findall(body)))
                names = "; ".join(dict.fromkeys(m.strip(" ,.") for m in NAME.findall(body)))
                w.writerow([name[:-4], page, dates, amounts, names, " ".join(body.split())[:120]])
                rows += 1
    print(f"{rows} pages indexed into {out}")


if __name__ == "__main__":
    main()
