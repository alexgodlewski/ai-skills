# The 2 door setup

Teach Meta who can pay, with one question and two pages. A free guide by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/).

<img src="cover.png" width="420" alt="The 2 door setup">

**PDF for your phone:** [two-door-setup.pdf](two-door-setup.pdf)

## What goes wrong now

Somebody fills in your form. Your page tells Meta: this is a win. Meta looks for more people like that one.

If three out of four are junk, Meta learns junk.

You fix it with one question and two pages. Same ad, same money.

## Step 1 one question

1. **Ask it on the form.** What do you make a month? Under $5,000. $5,000 to $20,000. $20,000 to $50,000. More than $50,000.
2. **Pick your line.** The lowest answer that can pay for your offer. Example: $20,000.
3. **Only one question.** Every extra question loses good people too.

## Or ask when they start

1. **A second question that works.** When do you want to start? This month. Next month. Later than that. Just looking.
2. **Pick your line.** This month and next month go through. The other two do not.
3. **Which one to use?** Use start date if people do not like to tell you their income. Use income if the price is high. Only one of them. Never both.
4. **Same rule.** The answer only picks the page. It is never sent to Meta.

## Step 2 two pages

1. **Door 1: yoursite.com/call** Your calendar. Only people over the line land here.
2. **Door 2: yoursite.com/thanks** A nice page with something free: a video or a guide. No calendar.
3. **Send them there by the answer.** In your form tool look for logic, redirect or ending by answer. Over the line goes to /call, everybody else goes to /thanks.

## Step 3 one win

1. **Take the old win off.** Remove the Lead event from the form and from /thanks. The normal page view can stay.
2. **Make a new one.** Meta Events Manager, Custom conversions, new: the page address contains /call. Name it Good lead.
3. **Tell the ad.** Copy your ad set, pick Good lead as the conversion, turn the old one off.
4. **Not enough of them?** Meta learns best with about 50 wins a week in one ad set. With fewer, count landing on /call, not the finished booking.

## Never send this

1. **No answers in the page address.** Bad: /call?income=20k. Good: /call.
2. **No income in the event.** Meta's terms do not allow financial details about a person. The page alone tells Meta enough.
3. **Say it in your privacy policy.** You use the Meta pixel, and why.

## Step 4 test it

1. **Fill in the form as a good lead.** You land on /call. In Events Manager, Test events, you see the page and Good lead.
2. **Fill it in as a bad lead.** You land on /thanks. Good lead does not show up.
3. **Do both on a phone.** Most people come from a phone.

## The pixel goes here

1. **On the form page.** Normal page view only. No Lead event.
2. **On /call.** The page view here is the win. The Good lead rule from step 3 counts it.
3. **Not on /thanks.** Nothing there. No base code, no event. The simplest way to be sure Meta learns nothing from it.
4. **Not in the address.** /call is right. /call?income=20k is wrong.

## Let Claude build both pages

Paste this into Claude. It asks about your offer first, then writes the question and the two pages.

```text
Help me set up two doors for my Meta lead ads. I will answer your questions. Ask them one at a time and wait.

First ask me about my offer: what I sell, who it is for, the price, and the smallest customer who can pay for it. Ask if my form tool can send people to different pages by answer (logic, redirect or ending by answer), and which calendar I use (a link I can open).

Then do these four things.

1. Write ONE question for my form. Pick the better one for my offer:
   (a) "When do you want to start?" Options: This month. Next month. Later than that. Just looking.
   (b) "How much does your business make a month?" Options: 4 or 5 ranges, where the lowest range that can pay for my offer is the line.
   Give 4 answer options in plain words. Tell me which options go through the line and which do not. Do not add a second question.

2. Build Door 1, the page /call. It shows my calendar and one short line that says "You are in. Pick a time." Only people who pass the line land here.

3. Build Door 2, the page /thanks. A friendly page with something free (a video or a guide, I will tell you the link). No calendar. No booking button.

4. Tell me how to send people to the right door by their answer. If my form tool has logic, give me the exact steps for my tool. If it has not, write a small HTML form that sends the person to /call or /thanks by the answer, and tell me plainly that it does not save the lead: I have to connect it to my form tool or my CRM.

Give me simple HTML for both pages, or, if I use a page builder, step by step instructions for that builder.

Then write a section called "Where the pixel goes" with these rules, and check your own pages against them:
- The Meta pixel base code goes on the form page and on /call. The page view on /call is the win for Meta.
- The pixel must NOT be on /thanks. Not the base code, not any event.
- No Lead event anywhere.
- The answer must never be in the page address. /call is good. /call?income=20k is bad.
- Never send the answer, or any money or personal detail, to Meta as event data.
- Do not invent my pixel code or ID. Ask me for the pixel ID and use Meta's own base code.
- My privacy policy must say I use the Meta pixel and why. Offer to write that line.

Finish with a test list: how I test as a good lead and as a bad lead on a phone, and what I should and should not see in Meta Events Manager, Test events.
```

## What happens next

1. **Your price per lead goes up.** That is right. You pay for fewer, better people.
2. **Count the price per call.** Ad money divided by calls that happened. Compare two weeks before with two weeks after.
3. **Do not touch it for a week.** Every big change starts the learning again.
4. **Forms inside Facebook?** They have no thank you page of yours. Use the form's own logic for answers, or send the good leads back to Meta from your CRM.

---

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/), founder of [Setor](https://setor.ai). We book sales calls in the DMs.
