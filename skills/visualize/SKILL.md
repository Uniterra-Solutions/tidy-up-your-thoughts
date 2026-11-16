---
name: visualize
description: "Use when a thought summary must become diagrams the user can see."
version: 0.1.0
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thinking, mermaid, diagram, mindmap, visualization]
    related_skills: [brainstorming]
---

# Visualize — the summary, drawn

`~/thoughts/<topic_name>/summary.md` is prose: statements in a row, each one true, the structure
between them invisible. The reader cannot see which statement is a definition and which is a
consequence, which fork the thinking actually took, where the open question sits.

The work of this skill is to make that structure visible — and to make nothing else visible. A
diagram is a rearrangement of the record. It is not a place to add a judgement, smooth over a gap, or
supply the axis the user never named.

## When to use

- `summary.md` exists and the user asks to see it, or asks for a mind map, a flow chart, a diagram.
- The summary has been read and is too flat to argue with: six statements that look alike but are
  doing six different jobs.
- A closing session of `tidy-up-your-thoughts:brainstorming` produced a summary and a picture would
  settle what is still open.

## When not to use

- There is no `summary.md`. Drawings built on a conversation that was never written down inherit every
  ambiguity the record was supposed to remove — run `brainstorming` first.
- The user wants a diagram of a codebase, an architecture or an API. That has a source of truth
  outside the thought record; use the rendering skills for that and leave this record alone.

## Step 1 — the diagram set

### 1.1 Read, then inventory

Read `summary.md` in full, and `README.md` for the open threads. Read `qa.md` only when a statement's
provenance matters — the summary already carries `[Qn]`.

Then classify every line by the job it does, because the job picks the diagram:

| The line does this | It supplies |
| --- | --- |
| defines a term | vocabulary — which words may appear in labels |
| states a criterion | the diamonds of a decision graph |
| states a consequence | an edge, with a label |
| weighs two things | the axes of a quadrant |
| records a change of mind | a timeline |
| names actors and an order | a sequence |
| names a condition of the thing | a state |
| marks itself open | a dashed node, never a solid one |

### 1.2 Choose, by what the reader must do

Four questions, asked in order. Stop at the first that has an answer.

1. **Does the summary describe a fork?** Conditions with outcomes → `flowchart` with decision
   diamonds. This is the most common case and the most useful picture.
2. **Does it describe a chain?** A claim, a warrant, an observation that breaks the warrant → an
   argument `flowchart`, drawn in that order.
3. **Does it describe a space?** Two criteria pulling against each other → `quadrantChart`.
4. **Does it describe composition, order or condition?** Parts → `mindmap`; actors over time →
   `sequenceDiagram`; the thinking's own history → `timeline`; discrete conditions → `stateDiagram-v2`;
   shares → `pie`.

Two to four diagrams. One diagram answers one question, named in its caption; if a second question
appears while drawing, it gets its own file. Beyond four, the set stops being read and starts being
filed.

`references/mermaid-templates.md` holds one verified template per type, worked on a single sample
topic, plus the syntax that bites in each. Copy the closest template and edit; write no mermaid from
memory.

### 1.3 Author, with the record's own words

Every `.mmd` file opens with the lines it rests on:

```
%% source: summary.md 現在確立的 (判準), 尚未確立的 (第一批客戶的來源)
```

Node text is shortened from the summary, never re-worded into the agent's vocabulary. The
「詞的用法」 section is binding: if the user calls it 「簽約人」, no label says 「決策者」.

Four rules that keep the picture honest:

- **An open question is a dashed node or a dashed diamond**, never a solid one. Solid means the
  summary establishes it.
- **A gap in the diagram is a gap in the summary.** When the drawing needs a node the summary does
  not have, stop and say which question is unanswered — do not invent the node to close the shape.
- **Colour is decoration; shape and line style carry meaning.** Solid versus dashed, diamond versus
  box. A distinction that exists only in a fill colour disappears in print and for a colour-blind
  reader.
- **Every edge out of a decision carries its outcome.** An unlabelled edge is a branch the reader
  cannot follow.

### 1.4 Render, look, then deliver

```
python3 scripts/render.py ~/thoughts/<topic_name>
```

It renders every `diagrams/*.mmd` to `.png` (2× scale, white background) beside a `.svg`, fails a
file whose `%% source:` header is missing, and reports "no output written" as a failure rather than
trusting the exit code. `--check` runs the rules without rendering.

A render proves syntax, not intent. **Look at each PNG** before it leaves: cut-off labels, a node
overlapping an edge, a mind map whose fan is unreadable at 10 characters per node. Fix the source and
re-render; never crop the bitmap.

Then `visual.md` beside the diagrams — captions only, no new content:

```markdown
# <topic_name> 的圖

## 01-decisions.png — 這件事在什麼條件下分岔
兩條路徑的分界是簽約人；未確立的部分以虛線表示。
來源：summary.md 尚未確立的

## 02-structure.png — 這件事由幾塊組成
來源：summary.md 現在確立的、詞的用法

## 未畫出的
- 交付責任的分工：summary 只提到它存在，沒有說誰承擔。
```

Deliver the PNGs as `MEDIA:/absolute/path.png`, one caption line each, in the user's language.
Identifiers and file names stay in English.

## Step 2 — corrections

A correction is the normal second half of this work, not a failure of the first. What matters is
that the corrected version and the record end up saying the same thing, and that the correction
itself survives in writing.

### 2.1 Fix the level, not just the pixels

Every correction is one of two kinds. Which one it is decides what gets edited.

| The user's correction | Its object | Edit |
| --- | --- | --- |
| 「這兩個應該並排」「用詞換成我說的」「拆成兩張」 | the drawing | the `.mmd`, then re-render |
| 「不是這樣，我當時說的是…」「這條我沒說過」「少了 X」 | the thought | `summary.md` (and `qa.md`) first, then every diagram that inherits it |

A drawing correction stops at the `.mmd`. A thought correction goes **upstream first**: the summary
is amended, and the diagrams are regenerated from the amended summary. Patching a diagram to match a
verbal correction while the summary still says the old thing leaves two sources of truth, and the
stale one is the one that gets read next month.

When the kind is unclear, ask which — one question, the same discipline as `brainstorming`.

### 2.2 Amend the summary without erasing it

`summary.md` follows the record's append-only rule: the superseded line is struck through with
`→ 由 Q<new> 取代` and the corrected statement is added with its own provenance. `qa.md` gets the new
exchange as a new `Q`/`A` pair. The correction becomes history the diagram can cite, not a silent
overwrite.

If the user's correction reveals a term whose meaning has changed, amend the 「詞的用法」 entry too —
labels across every diagram then change together, which is the point of keeping vocabulary in one
place.

### 2.3 Record the correction

`diagrams/REVISIONS.md`, append-only, one entry per correction:

```markdown
## 2026-11-17T09:12

**用戶原話**：「簽約人不是財務部門，是行政」
**層級**：想法（summary.md 尚未確立的）
**影響**：summary.md 第 2 節、01-decisions.mmd、02-structure.mmd
**重繪**：01-decisions.png、02-structure.png
```

The quoted sentence is the user's, verbatim; a paraphrase here repeats the mistake the correction was
fixing. Regenerate the same file names — the revision log holds the history, so no `v2` clutter
accumulates unless the user asks to compare two versions side by side, in which case both are kept
and both are named in the caption.

### 2.4 Re-verify after every correction

- `scripts/render.py <topic>` exits 0, and the changed PNG is newer than the changed `.mmd`.
- The PNG is looked at again — a label shortened to fix an overlap can lose the word that made it mean
  anything.
- Nothing in any diagram now contradicts `summary.md`; when the summary moved, grep the labels for the
  old vocabulary.

## Pitfalls

- **Drawing the conversation instead of the summary.** The summary is the settled text; `qa.md` is
  the debris. A diagram built from the debris shows paths the user abandoned as if they were open.
- **Turning an open question into a node.** The shape closes, the thought does not. Dashed, always.
- **Supplying the second axis.** A quadrant needs two criteria the summary holds; a plausible invented
  axis is a judgement the user never made, drawn in his name.
- **Point coordinates presented as fact.** Placement inside a quadrant is the agent's reading — say so
  in the caption, or use the chart only when the order is stated in the summary.
- **One diagram for everything.** Four questions in one graph produce a picture nobody reads; the
  reader's eye needs one question per frame.
- **Correcting the PNG.** Every fix is a `.mmd` edit plus a render. A hand-adjusted image cannot be
  regenerated and silently diverges on the next pass.
- **Silent revision.** A changed diagram with no `REVISIONS.md` entry loses the reason, and the next
  session re-litigates a settled point.

## Verification

- [ ] Each `.mmd` starts with `%% source:` naming the summary lines it uses.
- [ ] `scripts/render.py <topic>` reports 0 render failures and 0 rule warnings.
- [ ] Every PNG was looked at; no cut-off labels, no overlapping edges, no unreadable fan.
- [ ] Every label's wording exists in the summary, and the terms follow 「詞的用法」.
- [ ] Every open question in the summary appears dashed, or in 「未畫出的」 with a reason.
- [ ] `visual.md` lists each diagram with one caption and the section it came from.
- [ ] After a correction: summary amended (not overwritten), diagrams regenerated, `REVISIONS.md`
      appended with the user's own words.
