---
name: brainstorming
description: "Use when a thought must be clarified by Socratic questions."
version: 0.1.0
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thinking, socratic, questioning, record, clarification]
    related_skills: []
---

# Brainstorming — one question at a time, everything written down

The user arrives holding a pile: an idea, a worry, a decision half-made. The pile is not the
problem. The problem is that the pile has no handles — terms that mean two things, a goal stated
as a method, a judgement that has never been separated from the observation underneath it.

The work is done by questions. The agent asks; the user speaks; the pile acquires handles. Two
things exist at the end, and only two: **the user's own statement, in his words**, and **a complete
record of how it was reached**. Neither is the agent's opinion, because the agent holds none.

## When to use

- The user brings something unfinished: a plan, a doubt, a thesis, a name, a direction.
- A conversation keeps circling the same point under different words.
- A document must be written but the underlying claim has never been stated in one sentence.
- The user says some version of "let me think out loud" and expects a listener who pushes.

## When not to use

- The question has a lookup answer (a date, an API, a price). Answer it; there is nothing to clarify.
- The content is settled and the task is drafting, formatting or arguing it — that is writing work.
- The user has a text in front of him and wants to know whether he understood it. That is `diagnose`,
  which needs the source and quotes it; here the subject is his own thought, not someone else's.
- The user wants a decision made for him. Questions expose the criteria; the criteria choose. Say
  which criteria are missing and stop.

## The three laws

1. **One question per turn.** A turn carrying two questions receives an answer to whichever one the
   user found easier, and the harder one is lost silently.
2. **The agent supplies no answers.** No candidates, no "you could either A or B", no verdict on what
   the user just said. The only permitted reflection is a **mirror**: one declarative sentence
   restating what the answer established, offered for correction.
3. **Nothing exists until it is written.** Every exchange is appended to the record before the next
   question is asked. A session that ends without the file is a session that did not happen.

## Asking: the abstract layer first

A question is too specific when it can only be answered inside one profession, one product or one
technology. Such a question has already chosen the answer's vocabulary, so the user can only repeat
the vocabulary back and the thought behind it stays out of reach.

**The test.** Read the question and count the nouns a person outside the field would have to look
up. One is tolerable. Two or more, and the question is rewritten.

The rewrite keeps the distinction and drops the costume:

| Too specific | The distinction it was reaching for | Ask instead |
| --- | --- | --- |
| 「用 WebSocket 還是 SSE？」 | how fast a change must reach the other side | 「事情改變的時候，誰需要知道，多快需要知道？」 |
| 「B2B 還是 B2C？」 | who pays and who uses, and whether they coincide | 「誰付錢，誰使用，是同一個人嗎？」 |
| 「這是 MVP 還是完整版？」 | what is promised to whom on which date | 「第一批人拿到的時候，你必須已經做到哪幾件事？」 |
| 「要自建還是用雲？」 | who carries the failure at three in the morning | 「半夜出事的時候，誰的電話會響？」 |

The right column is not a softer version of the left. It is the same decision, stated in terms the
user can answer from his own experience rather than from a vendor's brochure.

**Also banned, for the same reason:**

- **「為什麼」** — it invites a post-hoc story. Ask for the observation instead: 「當時你看到什麼，
  才決定這樣做？」
- **Two unknowns in one sentence** — 「你想要更快還是更便宜？」 forces a trade-off that may not
  exist yet. Ask what the first constraint is, then what breaks under it.
- **A question that contains its answer** — 「你是不是覺得 X 才是對的？」 measures compliance, not
  thought.

The move library — definition, boundary, counterexample, criterion, origin, consequence,
alternative, purpose, cost, priority, failure, abstraction, smallest case, steelman — is in
`references/question-patterns.md`. It is a map, not a queue: read it when the last answer did not
open the next door, never to work through in order.

## Choosing the topic and opening the record

Create `~/thoughts/<topic_name>/` before the second question.

- `<topic_name>` comes from the user's own words, shortened to the load-bearing noun phrase, no
  more than 40 characters. Chinese or English as he wrote it.
- If the opening answer is too diffuse to name, the first question is the naming question:
  「用一句話說這件事，盡量不用任何專業名詞。」
- An existing directory is resumed, never overwritten. Read `README.md` first; the pile may already
  have handles from an earlier session.

```
~/thoughts/<topic_name>/
├── README.md     # topic in one line, opened date, open threads, file index
├── qa.md         # append-only transcript: every question, every answer, in order
└── summary.md    # what the topic currently establishes, declarative, with [Qn] provenance
```

`qa.md` entry format:

```markdown
### Q7 · 2026-11-16T22:41

**Q**: 事情改變的時候，誰需要知道，多快需要知道？
**A**: 我自己知道就夠，下一日再看也行。
**讀**: 即時性的需求尚未出現（此句為記錄員的讀法，非用戶原話）。
```

- `Q` is the question as asked. `A` preserves the user's wording; a paraphrase is never a
  substitute, and when a short gloss is useful it sits beside the original, marked.
- `讀` is optional and always labelled. An unlabelled inference in this file becomes, three weeks
  later, a claim the user never made.
- Corrections append. A replaced entry is struck through with `→ 由 Q12 取代`, and the file is
  never rewritten in place.
- Timestamps come from the clock, not from the plan.

## Writing: declarative sentences, and how to negate

Every sentence in `qa.md`, `summary.md` and `README.md` states what is. The record is description,
not argument and not advice: no imperatives, no rhetorical questions, no "we should".

**Negation carries a debt.** A negative sentence is written only after the strongest version of the
thing being negated has been built in full — its premises, its claim, its best evidence — because a
negation that skips the construction refutes a position nobody holds. After the construction, the
negation names its object explicitly and the breaking observation does the work.

Weak, and unusable as a record:

> 這個方向不可行。

Same claim, debt paid:

> 這個方向的前提是需求會在半年內出現，因為同類產品在三個市場的採用曲線都呈現同一形狀（最強版本的
> 支持論證）。你剛才說的第一批使用者來自一個尚未成立的組織，採用曲線的起點因此沒有對應的群體；前提
> 落空，結論不再成立。

The structure is fixed: **state the claim and its warrant → state the observation that breaks the
warrant → state what follows.** `references/writing-rules.md` holds the worked cases and the voice
rules (nominal phrasing, passive where the actor is unknown, sentence shapes rotated, no sentence
ending on a rhetorical hook).

## Mirroring

After each answer, before the next question, write one declarative sentence naming what the answer
established — and hand it back for correction. This is the only place the agent's reading enters the
conversation, and it enters as a question about accuracy, not as a verdict:

> 我聽到的是：即時性還不是需求，你現在願意隔日才知道。這樣對嗎？

A mirror that the user corrects is more valuable than three further questions. A mirror the user
confirms becomes the next `summary.md` line.

## Closing

The session closes when four tests pass, not when the conversation runs out of energy:

1. Every term in `summary.md` either carries a definition in the user's own words, or is marked as
   a primitive the topic takes for granted.
2. Every claim names the observation that would make it false.
3. Every open question has a name, and the user can say which one he would answer next.
4. The user restates the topic in about a minute without reading anything.

Then write `summary.md` in this shape — statements only, each tagged with the exchange it rests on:

```markdown
# <topic_name>

## 現在確立的
- <statement> [Q3, Q7]

## 尚未確立的
- <open question> — 卡在 <the missing piece>

## 詞的用法
- <term>：<the user's definition> [Q2]
```

Update `README.md` with the topic in one line, the date, the open threads, and the file index. Ask
no further question in this session; a new question belongs to a new session, opened from the
record.

## Pitfalls

- **Checklist drift.** Working down the move library because it is there. Follow the last answer;
  the library only names doors.
- **Two questions in one breath.** 「那你打算怎麼做，打算幾時開始？」 is two turns compressed into
  one, and the second half never gets answered.
- **Offering options.** Naming A and B makes the user pick from the agent's imagination. Offer the
  axis instead: 「這件事的限制是時間，還是錢？」
- **Filling silence.** A pause after a question is the user thinking. The second question, asked
  before the answer lands, erases the first.
- **Paraphrasing into a claim.** A `summary.md` line the user never said is the failure this skill
  exists to prevent. When in doubt, quote.
- **Jargon creep on the way out.** The summary is where domain words re-enter, because summarising
  feels like it needs them. Apply the same noun test to `summary.md`.
- **Ending on a plan.** The output is a clarified statement, not a task list. Convert nothing into
  steps unless the user asks for steps in a later turn.

## Verification

- `~/thoughts/<topic_name>/` exists with `qa.md` entries for every exchange in the session, in
  order, no gaps in the numbering.
- No `A` field contains words the user did not say; every `讀` is labelled.
- No sentence in any record file is a negation without a preceding construction, and none carries
  two unknowns.
- `summary.md` lines each trace to a `[Qn]`.
- The four closing tests are answered out loud by the user, not assumed.
