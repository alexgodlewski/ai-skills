---
name: humanizer
description: Rewrite text so it does not read like AI wrote it, in the person's own voice. Finds the common AI writing patterns (correctio "not X, it's Y", long dashes, the word "quietly", purple prose, lists of three, "here's the thing", fake questions, hype words and more), removes them, and rewrites using samples of the person's real writing. Use when someone asks to humanize text, remove AI patterns, make a draft sound like them, or check a post, email or script for AI tells.
---

# Humanizer

You take text that sounds like AI and make it sound like the person. You do this in two parts: you remove the AI patterns below, and you write in the person's own voice.

Be honest about the limit. This makes writing read like a person wrote it. It does not guarantee that an AI detector tool will pass it. Never promise that.

## 1. Get the text

If the person did not paste the text to fix, ask: "Paste the text you want me to fix."

## 2. Get their voice

You need real writing by the person, not writing by AI.

- If they gave samples, use them.
- If not, ask: "Paste 2 or 3 things you wrote yourself, like old posts, emails or messages. Real ones, not AI ones. Longer is better."
- If they have a file or a folder of their posts, offer to read it.
- If they have nothing, say so and use plain, short, spoken English instead. Tell them the result will be less like them, and ask for samples next time.

Read the samples and write down, for yourself:

- how long their sentences are, and how long their paragraphs are;
- words and phrases they use a lot;
- words they never use;
- how they open and how they end;
- how they use punctuation (commas, question marks, exclamation marks, line breaks);
- how they talk to the reader (you, we, I);
- whether they swear, joke, or use slang.

## 3. The AI patterns

Find every one of these in the text. Each has a plain description and a before and after.

**1. Correctio ("not X, it's Y")**
AI says what something is not, then what it is, to sound deep. It adds no fact.
Before: "You don't have a traffic problem. You have a trust problem."
After: "Your visitors do not trust you yet, so they leave."

**2. The long dash in the middle of a sentence**
AI puts one in almost every paragraph. Most people do not even know how to type it. Remove every long dash and every medium dash. Use a period, a comma, or the word "and".
Before: "The tool is fast [long dash] and honestly, it is cheap."
After: "The tool is fast. It is also cheap."

**3. The word "quietly" and its cousins**
AI uses "quietly" to add a mood that is not earned. Cousins: "subtly", "silently", "gently", "slowly but surely". Delete the word, or say the real fact.
Before: "The industry is quietly changing."
After: "Three of my clients dropped their agency this year."

**4. Purple prose**
Big feeling words with no fact under them. Replace with one small, true detail.
Before: "A symphony of possibility unfolded before me."
After: "I opened the file and saw 40 new orders."

**5. Lists of three**
AI loves three items with the same rhythm. Real people give two, four, or one.
Before: "It is fast, simple, and powerful."
After: "It is fast and it takes one click."

**6. "Here's the thing" and other setup lines**
Lines that announce a point instead of making it. Others: "Let me be clear", "Here's the kicker", "Let that sink in", "Read that again". Cut the line and start with the point.
Before: "Here's the thing: most people never follow up."
After: "Most people never follow up."

**7. Fake questions**
A question the writer answers right away. Just say it.
Before: "So what is the secret? Consistency."
After: "The secret is to show up every day."

**8. Hype words**
"Game-changer", "revolutionary", "unlock", "supercharge", "next level", "cutting-edge". They claim a lot and prove nothing. Say what changed, with a number.
Before: "This game-changer will supercharge your sales."
After: "This cut my follow-up time from 20 minutes to 2."

**9. Fancy filler words**
"Delve", "tapestry", "landscape", "realm", "testament", "navigate", "embark", "leverage", "foster", "pivotal". Use the plain word.
Before: "Let's delve into the rich tapestry of the marketing landscape."
After: "Let's look at how marketing works today."

**10. Hedging**
"It's important to note", "it could be argued", "in many cases", "may potentially". If you know it, say it. If you do not know it, say that once.
Before: "It's important to note that results may potentially vary."
After: "Results vary. Mine took six weeks."

**11. Empty intensifiers**
"Truly", "really", "incredibly", "absolutely", "deeply", "extremely". Delete them, or use a number.
Before: "This is an incredibly powerful and truly amazing result."
After: "This result doubled my reply rate."

**12. Tidy wrap-up endings**
"In conclusion", "At the end of the day", "Ultimately", "The bottom line", and a closing line that repeats the whole text. End when you are done, or end with one real next step.
Before: "In conclusion, at the end of the day, consistency is key."
After: "Send one email a day for a month, then check your replies."

**13. Opening with praise or throat-clearing**
"Great question!", "In today's fast-paced world", "In the ever-evolving landscape of". Start with the first useful sentence.
Before: "In today's fast-paced world, email is more important than ever."
After: "I send 30 emails a day. Here is how I keep them short."

## 4. Rewrite

1. Mark each pattern you find in the text.
2. Rewrite the whole text in the person's voice, using what you learned from their samples.
3. Keep all facts, names, numbers, links and the meaning. Never invent a fact, a number or a story to replace a pattern. If a sentence says nothing without the pattern, cut it, or ask the person for the real detail.
4. Keep roughly the same length, unless the cuts make it shorter. Shorter is fine.
5. Vary sentence length the way the person does.

## 5. Check before you hand it over

- No long dash and no medium dash anywhere. Search the text for them.
- None of the 13 patterns above is left. Read it once more, line by line.
- It matches the samples: same kind of words, same sentence length, same tone.
- It still says what the original said.

## 6. Show the result

Give the person:

1. The rewritten text.
2. A short list of what you changed, one line each, for example: "Removed 3 long dashes. Cut 'quietly' in line 2. Changed the list of three to two items."
3. One line asking if it sounds like them. If not, ask what is off and fix it.

Offer to save their voice notes in `~/.claude/skills/humanizer/voice.md`, so next time you do not need new samples. Only save it if they say yes.
