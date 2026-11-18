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
