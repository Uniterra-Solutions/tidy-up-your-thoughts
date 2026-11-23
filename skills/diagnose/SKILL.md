---
name: diagnose
description: "Use when a text must be shown to be understood, concept by concept."
version: 0.1.0
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thinking, concepts, diagnosis, learning, questioning]
    related_skills: [brainstorming]
---

# Diagnose — a text is understood when a case outside it can be answered

Reading produces the feeling of understanding at a rate that has nothing to do with understanding. The
text's own words stay in the ear; a paragraph can be followed while a term inside it stays unusable.
What separates the two is not agreement but production: a case the text does not contain, handled with
the text's distinctions.

This skill extracts what a text is *for* — three to seven concepts that other sentences lean on — and
tests each one with questions until its status is known. The verdict is not the agent's opinion of the
reader. It is a quotation: the answer either matches the line the material draws or it does not, and
the line is named.

## When to use

- The user has read something — a paper, a chapter, a policy, a spec — and wants to know whether he
  actually understood it.
- Before using a text's vocabulary in his own work: a report, a proposal, an exam.
- A summary exists and reads fluently, which is exactly when the words may be doing the work.
- The user asks to be tested, quizzed, or examined on a text.

## When not to use

- **No text is in hand** — a lecture attended, a video watched, a memory. A verdict then rests on the
  model's recollection of the field, which is the most confidently wrong thing available. Run
  `brainstorming` instead: it clarifies what the user already thinks and needs no source.
- The user wants a summary. Summarising is `tidy`'s work; a summary tests nothing.
- The material is a decision the user must make. That is `brainstorming`, then `refine`.
- One term is unfamiliar and a dictionary settles it. Look it up; there is nothing to diagnose.

## The source gate

**Before the first question, the text exists in the record.** `~/thoughts/<topic_name>/source.md`
holds the material as given — pasted, or copied from a file — with its sections numbered `§1`, `§2`,
and so on. Page numbers go in the section headings when the original had them.

Every verdict names a section and quotes its line verbatim. Two consequences, and they are the whole
point:

1. A verdict that cannot quote is not a verdict. It is the model's memory of the topic, and it is
   dropped rather than softened.
2. The quote is checked against `source.md` before it is written into the record. A paraphrase inside
   quotation marks is a fabrication with a citation attached.

If the user will not or cannot supply the text, say what is missing and stop. Diagnosing from memory
produces a grade that looks exact and cannot be checked by anyone, including the agent.

`<topic_name>` follows `brainstorming`: the text's title shortened to the load-bearing noun phrase,
forty characters at most, in the language the user used. An existing folder is resumed, never
overwritten; read its `README.md` first.

## Phase 1 — extract, three to seven concepts

A concept earns a card when the text's other sentences cannot be stated without it. The test is
mechanical, so run it instead of judging by importance:

- **Remove it.** Delete the term from the text's key sentences. If a sentence stops making a claim, the
  concept is core. If the sentence still stands, the term was decoration.
- **Count the dependants.** A concept that three other sentences lean on is core; one that appears once
  and is never used again is not.
- **Check it can be probed outside the text.** A concept whose only examples come from inside the
  text's own formalism cannot be tested past recitation. Cap its verdict at `partial` and say why.

Three to seven. Past seven the session becomes a quiz, and a quiz produces scores rather than
knowledge. Everything else goes into `concepts.md` under **secondary** — listed, never asked, unless
the core set is finished and the user wants more.

A card is not the agent's explanation of the concept; it is the material's own account, quoted:

```markdown
### C1 Opportunity cost

- **Definition**: the highest value of the next-best alternative given up when a choice is made [§2]
- **Boundary**: "not everything that is given up" [§2]; "not accounting cost" [§3]
- **Depends on**: —
- **Why it is core**: the pricing argument in §4 rests on it; with the term removed, the paragraph has
  no conclusion
- **Probeable**: yes — the text draws two counterexamples of its own
- **Common misconception** (inferred, not in the text): counting anything given up — used to design a
  question only
```

`assets/record-templates.md` holds the complete file shapes.

**A card holds what the text says; `map.md` holds what the user reached.** Status is written in one
place only. A `status` field on a card and a status row in the map are two records of the same thing,
and they will disagree by the third session.

The `Common misconception` line is the one field the text may not supply. It comes from the agent's
reading of the material, or from one read-only subagent given `source.md` and the concept name and
nothing else — no transcript, no user answers. The isolation is the point: a challenger that can see
what the user already said produces flattering misreadings, and the questions built on them test
nothing. Either way the field is labelled `inferred` and never enters a verdict.

## Phase 2 — cut, then show the list

Three checks, in this order. Each failure has one remedy:

| Check | Fails when | Remedy |
| --- | --- | --- |
| Is it in the text? | the definition cannot be quoted | delete the card — the concept came from the field, not the material |
| Is it load-bearing? | removing it leaves every key sentence standing | demote to secondary |
| Can it be probed outside the text? | every example is formal notation | keep, cap the verdict at `partial` |

Then show the list — ids, names, one line each, and what was cut with the reason — and let the user
add, remove, or reorder. His list wins. A concept he names that the text does not support becomes a
secondary concept with the reason recorded next to it.

## Phase 3 — ask, one concept at a time

Order: prerequisites first, then core before secondary, then the concept whose status is least known.
**A concept whose prerequisite is not `clear` is not asked.** An answer to it cannot be interpreted —
there is no way to tell whether the error sits in the concept or in the thing it rests on — so it is
recorded `blocked` and the prerequisite is asked instead. Skipping this step produces confident verdicts
on unreadable evidence.

Four probe types, in this order, stopping as soon as the status is known:

| Type | The question | What it establishes |
| --- | --- | --- |
| `open` | "Say what X means in your own words, without using the text's sentences." | whether a statement exists at all |
| `boundary` | "Which of these two is X, and why?" | whether the line is drawn, not just the term known |
| `counterexample` | "Does this case count as X?" — a case the text does not contain | whether the boundary is usable |
| `transfer` | a case from *outside* the material, in the user's own domain | whether it transfers |

**An answer to the open question can never reach `clear`.** It establishes that a statement exists, not
that one holds. `clear` costs a case the text does not contain; the verdict table below enforces it.

**One question per turn, one concept per question.** A turn carrying two questions receives an answer
to the easier one and loses the harder one silently.

`references/probe-types.md` holds the construction rules, each type's failure mode, and the worked
rewrites. Read it when a question lands flat, not before every question.

### The one exception to "no options"

The plugin bans offering options, because a choice between the agent's A and B replaces the user's
thinking. Diagnosis has a single legitimate exception, in the `unclear` state only: two readings, one
true and one false, both drawn from the material's own boundary — "Is this one X, or is that one X?
Why?" The question is a test item, not a recommendation, and the *why* is what is graded. Never offer
two plausible readings and accept the choice on its own.

## Phase 4 — judge, then say one thing

The judge compares the answer to the quoted line, not to a feeling about the answer. Four verdicts and
one state that is not a verdict:

| Verdict | Test | What the user hears |
| --- | --- | --- |
| `clear` | the distinction the quoted line turns on, **and** a case outside the text handled | the quoted line, named as what his answer matches — then the next concept |
| `partial` | the right term, one dimension missing (usually the boundary) | the part that matches, quoted; the missing dimension, named; one question that isolates it |
| `misconception` | the answer contradicts a specific line | that line, quoted; the counterexample it fails on; one question built on that counterexample |
| `unclear` | the answer does not commit — restates the term, hedges, changes the subject | a lower rung: an analogy, or the two-reading question above |
| `blocked` | the prerequisite is not yet `clear` | which concept must come first; no verdict on this one |

Rules for the sentence the user reads:

- **Praise the move, not the person.** "You put 'given up' at the centre, and that matches §2's
  definition" is a verdict; "Good answer!" is a mood that teaches nothing.
- **One correction per turn.** Two corrections and the second is lost; the turn also becomes a lecture,
  which is the failure this skill exists to avoid.
- **The quote does the work.** Where the answer is wrong, the line from `source.md` is the whole
  correction. Do not re-explain the concept in the agent's own words — that reintroduces exactly the
  paraphrase the gate exists to prevent.
- **One state line, then one question.** `C3 · partial · boundary` is enough. Role monologues (LEFT /
  RIGHT / JUDGE) leak into the reply and triple its length without adding a fact to the record.
- **His words are kept.** The answer goes into `qa.md` verbatim; the verdict is a separate field,
  labelled as the agent's reading.

## Phase 5 — stop, and write the map

A concept stops when it is `clear`, or when two questions have been asked and a third is not earned. **A
third question is earned by movement** — the second answer was `partial`, not `misconception`.
Persistence past that point produces a questionnaire, and the extra rounds measure the agent's patience
rather than the user's understanding.

The session stops when any of these holds:

- every core concept is `clear`;
- every core concept has reached its cap, whatever the status;
- the user says stop;
- what remains is secondary.

Then write `map.md` from the transcript, not from memory of the conversation:

```markdown
# <topic_name> — mastery map 2026-11-23

Source: source.md, §1–§9
Tested: 5 core concepts, 2 clear

| id | concept | depends on | status | evidence |
| --- | --- | --- | --- | --- |
| C1 | opportunity cost | — | clear | [Q4], [Q7] |
| C3 | marginal cost | C1 | partial | [Q9] |
| C5 | sunk cost | C3 | blocked | — |

## Clear, and on what
- C1: Q7 handled a case the text does not contain (the cost of switching tutor), and the boundary
  matches §2 [Q7]

## Still unclear
- C3: the boundary holds only in the increasing range; every example he gave was increasing; 2 questions
  asked

## Blocked
- C5: waits on C3 — asked now, a wrong answer could not be attributed

## Suggested review
- §5, second paragraph (C3's boundary), then a new diagnose session testing only C3 and C5
```

No percentage, no score, no grade for the person. The map states what is established, on what
evidence, and what is not — the same discipline as `summary.md`, with the source standing where the
user's own claim stands.

## Closing

Update `README.md` with the topic, the date, the open threads and the file index, exactly as
`brainstorming` does. Ask no further question in this session; a new concept, or a re-test, is a new
session opened from `map.md`.

## Pitfalls

- **The concept explosion.** Twelve cards feel thorough and produce twelve half-tested terms. Three to
  seven; the rest are listed and not asked.
- **A verdict without a quote.** The most expensive failure here, because the grade looks exact. If the
  line cannot be found, the answer is not graded: record `ungraded` and say so.
- **Recitation read as understanding.** A correct-sounding answer assembled from the text's own
  sentences establishes recall. It becomes `clear` only when a case outside the text is handled.
- **The quiz.** A run of closed questions with one-word answers measures attention and nothing else.
  Every core concept needs at least one `transfer`.
- **Correcting twice.** The second correction is not heard, and the turn becomes a lecture.
- **The third-round habit.** A third question asked because the concept "should" be clear by now.
  Rounds are spent by design, not by hope.
- **Grading the person.** "You got that wrong" is about him; "this sentence does not match §2's
  'next-best alternative'" is about the text. The second can be checked by a third party; the first
  cannot.
- **Diagnosing past a blank.** A prerequisite left unclear and a verdict given anyway produce a map
  that is wrong in a way the user cannot see.

## Verification

- [ ] `source.md` exists, sectioned `§1..§n`, and every quoted line in `concepts.md`, `qa.md` and
      `map.md` appears in it verbatim.
- [ ] `concepts.md` holds three to seven core cards, each with a quoted definition and either a quoted
      boundary or the recorded reason the text draws none; every cut card names the check it failed.
- [ ] No card's definition was written by the agent; a card with no quote was deleted, not filled in.
- [ ] `qa.md` numbering continues from the folder's last entry, with no gaps, and every `A` field is the
      user's wording.
- [ ] Every verdict in `qa.md` carries the section it quotes; `ungraded` appears wherever the line could
      not be found.
- [ ] Every `clear` row in `map.md` rests on an exchange where the user handled a case the text does not
      contain.
- [ ] No concept was graded while its prerequisite was below `clear`; those rows read `blocked`.
- [ ] `map.md` carries no score, percentage or grade of the person.
- [ ] `README.md` lists `source.md`, `concepts.md`, `map.md`, `qa.md` and the open threads.
