# Record templates — four files, one folder

`~/thoughts/<topic_name>/` is shared with `brainstorming`, `refine` and `tidy`. A diagnose session
adds `source.md`, `concepts.md` and `map.md`, and continues `qa.md` from its last number. Nothing is
overwritten; a second session on the same text resumes the folder and appends.

---

## source.md — the material, sectioned

```markdown
# <topic_name> — source

Source: <title, author, where it came from>
Recorded: 2026-11-23
Section numbers follow the original's own subdivisions, not line numbers here.

## §1 <section title>

<text verbatim>

## §2 <section title>

<text verbatim>
```

Rules:

- **Verbatim.** No tidying, no trimming of the middle, no translation. A quote checked against a
  cleaned-up source proves nothing about what the author wrote.
- **Sections are the citation unit.** If the original has none, cut one every few paragraphs and name
  the cut by its first words. `§4` must point at a passage a reader can find in one look.
- **A second text is a second folder.** Two sources in one `source.md` make `§n` ambiguous and every
  verdict unverifiable.
- If the user pastes only an excerpt, `source.md` says so at the top and every verdict is scoped to the
  excerpt. A verdict about a paragraph that is not in the record is the memory failure this folder
  exists to prevent.

---

## concepts.md — the cards, extracted then cut

```markdown
# <topic_name> — concept cards

Source: source.md (§1–§9); 5 extracted as core, 2 secondary

## Core

### C1 Opportunity cost

- **Definition**: the highest value of the next-best alternative given up when a choice is made [§2]
- **Boundary**: "not everything that is given up" [§2]; "not accounting cost" [§3]
- **Depends on**: —
- **Why it is core**: the pricing argument in §4 rests on it; with the term removed, the paragraph has
  no conclusion
- **Probeable**: yes — the text draws two counterexamples of its own
- **Common misconception** (inferred, not in the text): counting anything given up — used to design a
  question only

### C2 ...

## Secondary

| id | concept | why it is not core |
| --- | --- | --- |
| S1 | indifference curve | appears once; nothing later refers to it |
| S2 | envelope theorem | defined only inside the mathematical appendix, so no probe outside the text is possible |

## Deleted

| candidate | check it failed |
| --- | --- |
| transaction cost | definition cannot be quoted — the text uses the term without defining it |
```

Rules:

- **No status field.** The card is the text's account of the concept. State lives in `map.md`, where it
  is one row per concept and one `[Qn]` per row; a status here would be a second record of the same
  fact, and the two disagree by the third session.
- **Every quoted field points at a section.** A definition with no `[§n]` is the agent's, and the card
  is deleted in phase 2 rather than completed from memory.
- **`Common misconception` is labelled inferred unless the text names it.** It exists to design a
  question; it never enters a verdict, because a misconception the user did not display is not evidence
  about him.
- **`Probeable` is written before the first question.** It is what stops a later session from grading
  recitation as understanding and calling it the user's fault.
- **Cut cards keep their reason.** A deleted concept with no recorded check is a decision nobody can
  review, and the next session re-adds it.

---

## qa.md — the verdict is a field, not a sentence

Continues the folder's numbering. Same `Q` / `A` fields as `brainstorming`, plus two:

```markdown
### Q9 · 2026-11-23T14:20 · C3 · boundary

**Q**: You add a flight; it costs 50,000 more and brings 40,000 more in fares. Is that 50,000 a
marginal cost?
**A**: (the user's wording, verbatim)
**Verdict**: partial — recognised "the cost that only appears because of the extra flight", but the
boundary covers only the increasing range (this is the agent's reading, not the user's words)
**Quote**: "marginal cost rises once output passes a certain point" [§4]
```

- **`Verdict` is always labelled as the agent's reading.** It is the one field the user did not write,
  and three weeks later an unlabelled verdict reads as something he said.
- **`Quote` is mandatory for `clear` / `partial` / `misconception`.** `ungraded` is a legitimate value
  and means the line could not be found; it is never replaced by a plausible one.
- **`blocked` carries no `Quote`,** because no judgement was made. It names the prerequisite instead:
  `Verdict: blocked — waits on C2 reaching clear (this is the agent's reading, not the user's words)`.
- **A corrected answer is a new entry.** The old one is struck through with `→ superseded by Q14`,
  never rewritten. A verdict that changed its mind is worth more in the record than a verdict that was
  always right.

---

## map.md — what is established, and on what

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
- C3: the boundary holds only in the increasing range; every example he gave was increasing; 2
  questions asked

## Blocked
- C5: waits on C3 — asked now, a wrong answer could not be attributed

## Suggested review
- §5, second paragraph (C3's boundary), then a new diagnose session testing only C3 and C5
```

Rules:

- **A status with no `[Qn]` is `untested`,** whatever the prose around it says.
- **`clear` requires a `transfer`.** If the exchange behind it was a definition or a boundary question,
  the row is `partial` regardless of how good the answer sounded.
- **No score.** "Mastery: 78%" invents a denominator; the count of concepts by status is already exact.
- **`Suggested review` names a section, not a topic.** "Review marginal cost" sends him back to the whole
  text; "§5, second paragraph" sends him to the line that failed.

---

## README.md — one line per file

```markdown
# <topic_name>

Source: <title> (source.md, §1–§9)
Opened: 2026-11-23   Last: 2026-11-23
Open: C3's boundary; C5 untested

| file | holds |
| --- | --- |
| source.md | the text, §1–§9 |
| concepts.md | 5 core, 2 secondary, 2 deleted |
| qa.md | Q1–Q12 |
| map.md | mastery map, 2026-11-23 |
```
