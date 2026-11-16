---
name: tidy
description: "Use when the record must become a report: read all, verify terms, write."
version: 0.1.0
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thinking, report, writing, terminology, synthesis]
    related_skills: [brainstorming, refine, visualize]
---

# Tidy — the record becomes a report

`~/thoughts/<topic_name>/` holds a conversation that already happened: a transcript, a summary, the
situations the idea met, a set of diagrams, a revision log. Every one of those files is written for
the person who was there. A report is written for the reader who was not.

Three steps: read all of it, verify the vocabulary, write one document. The document argues nothing
the record does not already establish, and it keeps every blank exactly as blank as the session left
it.

## When to use

- `summary.md` exists and the user asks for 報告、文件、文章, or "整理成一份可以給人看的東西".
- The discussion is finished and needs to survive outside the folder it happened in.
- A topic has been refined and the answers need to become one argument.

## When not to use

- No `summary.md`: there is no settled text to report. Run `brainstorming`.
- The user wants a plan, a proposal, or a document that persuades someone. That is a different
  deliverable with a different audience, and the discipline here (no advice, no new claims) would
  cripple it.

## Step 1 — read everything, in this order

| File | Read it for | It becomes |
| --- | --- | --- |
| `README.md` | the topic in one line, the dates, the threads still open | the opening paragraph and the closing section |
| `summary.md` | the settled statements, each with `[Qn]`, and the 詞的用法 | the body, in this report's order |
| `qa.md` | the user's exact words, the criteria he stated | citations only — never copied into the body |
| `refine.md`, `refine-raw/` | which situations were settled, on what criterion, which went unanswered | the pressure-test section |
| `diagrams/*.mmd`, `visual.md` | the structure, already drawn | the appendix, embedded or referenced |
| `REVISIONS.md` | what changed and why | mentioned only when a correction changed a conclusion |

Then build the inventory before writing a sentence: one row per statement — **claim, source
(`[Qn]` / `[Sxx]`), section it belongs in**. Every substantive sentence in the report must trace to a
row. A sentence that traces to no row is either a transition (carrying no claim) or it is the agent
thinking out loud, and the second kind does not go in.

## Step 2 — the vocabulary

Two kinds of word appear in a report, and they are governed differently.

- **The user's own terms** — everything listed in the summary's 「詞的用法」. Used as written. Renaming
  「簽約人」 as 「決策單位」 imports a taxonomy he never adopted, and the report then argues in a
  vocabulary he cannot check.
- **Domain terms the report needs** — a legal instrument, a market structure, a technical mechanism.
  Each one is verified before it is used. `references/terminology.md` holds the source hierarchy, the
  record format, and the policy for a term that means different things in different fields.

The bar for a domain term: it is defined in the report where it first appears, and the definition
names where it came from. A term that cannot be sourced is deleted and the phenomenon is described
instead. A term kept for the sound of it is a defect.

Every report carries a 詞的定義 section: term, definition, source (user definition with `[Qn]`, or an
external source with its citation and retrieval date).

## Step 3 — the structure

`~/thoughts/<topic_name>/report.md`, in this order. `assets/report-template.md` is the skeleton.

1. **摘要** — under 150 characters: what the topic is, what state the discussion reached.
2. **主題與範圍** — what the report covers, and what it deliberately leaves out.
3. **現在確立的** — the settled statements, ordered by strength of support.
4. **判準與條件** — the criteria the user stated, and the conditions each conclusion carries.
5. **壓力測試** — the situations from `refine`: what was settled and on what criterion; what was left
   unanswered, named as unanswered.
6. **尚未確立的** — the open questions, and for each, the piece that is missing.
7. **詞的定義** — the terminology table.
8. **附錄** — diagrams, the source index (`[Qn]` list), the revision history when it matters.

**Ordered by strength, not by chronology.** Support strength is: how many independent entries in the
record carry the statement, whether it survived a refine situation, and how wide the claim's scope is.
A statement the user asserted once and never tested sits below one that three exchanges and a
situation converged on — whatever order they were said in.

## The three writing rules

### 1. Every paragraph opens with its topic sentence

The first sentence states what the paragraph claims; the rest is evidence, scope or consequence. The
mechanical test: read only the first sentences, in order, and see whether they form a coherent
outline. If a first sentence needs its paragraph to make sense, it is a transition, not a topic
sentence, and the paragraph has none.

- **Fails:** 「另外，關於定價，我們也討論了很多。」 — announces a subject without claiming anything.
- **Holds:** 「定價權目前集中在創辦人一人手上，紀錄中沒有書面規則。」 — a claim the paragraph then
  supports.

### 2. Declarative sentences

The report states what is. No imperatives (「應該」「必須」), no rhetorical questions, no first person
plural. Nominal phrasing carries the subject, passive voice appears where the actor is unknown, and
consecutive sentences rotate their shape so the page does not read as a list.

### 3. Negation only inside a rebuttal

This is the narrow version of the rule, and the narrowness is the point. Description is affirmative.
A negative sentence appears in one place only: meeting a counter-argument, and then only after that
argument has been built in full, in declarative sentences, as its strongest defender would build it.

A rebuttal block has three parts, in this order:

1. **The counter-argument, complete.** Its premises, its evidence, its inference, its conclusion — as
   an argument, not as a caricature. If it cannot be stated this fully, it cannot be refuted, and the
   right move is to describe the disagreement instead.
2. **The observation that breaks it.** A dated entry, a figure from the record, a case in the world.
   Named, so the refutation can be checked.
3. **What follows, at the scope the observation supports.** A refutation that generalises past its own
   evidence is a new unsupported claim.

Outside such a block, a negative thought is rewritten as an affirmative one:

| Written as a negation | Written as what is the case |
| --- | --- |
| 這個方向不可行。 | 這個方向成立所需的前提是第一批客戶的來源；紀錄中這一點仍是空白 [Q8]。 |
| 客戶不會接受這個價格。 | 客戶在 Q12 表示可接受的上限是每月 Z；報價在其上。 |
| 這不是技術問題，是治理問題。 | 這個問題的位置在治理：一份合約的主體由誰簽，決定責任落在哪一方 [Q6]。 |
| 沒有證據顯示需求存在。 | 紀錄中關於需求的條目為零；與需求相關的陳述全部來自推測。 |

Mark the block so a reader and the lint can both find it: a heading containing 反駁, or
`<!-- rebuttal:start -->` … `<!-- rebuttal:end -->`. `scripts/check_report.py` fails every negative
sentence that sits outside one.

## The report never does these

- **Give advice.** 「應該先做 X」 belongs to a conversation, not to a report. If the user asks for
  recommendations, they go in a separate section labelled as the agent's proposal — never mixed into
  what the record establishes.
- **Fill a blank.** An unanswered situation stays unanswered, with its id, so the reader knows what
  was not decided rather than what the writer assumed.
- **Add a claim.** No conclusion enters the report that the inventory cannot trace to `[Qn]` or
  `[Sxx]`.
- **Speak as the user.** An inference of the agent's is labelled as one, or omitted.

## Pitfalls

- **The transcript pasted in.** A report is not `qa.md` with headings. The transcript is evidence; the
  appendix may cite it, the body summarises what it establishes.
- **Paragraphs that open with 首先 / 此外 / 另一方面.** These are sequence markers, not claims. They
  are also the clearest symptom that the section has no argument, only items.
- **Negation used as argument.** 「沒有理由相信」 does the work of a refutation without paying for it.
  Build the argument, then break it, or say what is the case.
- **Terminology as decoration.** A term that is not needed to state a fact makes the sentence harder
  to check. Delete it and describe the thing.
- **Chronological order.** The reader does not need the order of the conversation; they need the
  order of support.
- **The plan in disguise.** 「下一步」 phrased as tasks turns a report into a project brief. The open
  questions section names what is missing, not what to do about it.

## Verification

- [ ] `scripts/check_report.py <topic>` exits 0: no negative sentence outside a rebuttal, no advice
      wording, every citation resolves, a 詞的定義 section exists.
- [ ] `scripts/check_report.py <topic> --outline` read top to bottom: the first sentences form an
      outline on their own.
- [ ] Every substantive sentence traces to an inventory row.
- [ ] Every domain term is defined where it first appears and sourced in 詞的定義.
- [ ] Every unanswered situation in `refine.md` is still unanswered here, with its id.
- [ ] Diagrams referenced in the appendix exist on disk and match the current `summary.md`.
