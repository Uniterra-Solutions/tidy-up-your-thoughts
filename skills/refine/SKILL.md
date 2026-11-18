---
name: refine
description: "Use when an idea must meet its situations: lenses, then answers."
version: 0.2.0
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thinking, red-team, scenarios, subagents, decision]
    related_skills: [brainstorming, visualize]
---

# Refine — the idea meets its situations

`summary.md` is what the user has already thought through. Re-asking it wastes the session, and
admiring it wastes more. What the summary has not met is the world: the counterparty who reacts, the
premise nobody verified, the moment where a failure stops being recoverable.

This skill brings those moments back as **situations** and makes the user answer them. Three steps:
dispatch several lenses, ask about the situations one at a time, write what came out.

The output is the user's decisions under pressure. It is not the agent's verdict on the idea.

## When to use

- `summary.md` exists and holds a direction the user intends to act on.
- The user asks to stress-test, red-team, or "找漏洞" an idea.
- Before a commitment: money, a hire, a public step, a contract.
- `brainstorming` produced a clean summary and the summary sounds convincing — which is exactly when
  it has not been tested.

## When not to use

- No `summary.md`: there is nothing to stress yet. Run `brainstorming` first.
- The user wants the agent's opinion on the idea. That is a conversation, not this skill; this skill
  produces questions for him to answer.
- The decision is already made and is not reversible. Situations only the user can act on are worth
  posing; situations nobody can act on are cruelty with a diagram.

## What a situation is

| | A risk | A situation |
| --- | --- | --- |
| Shape | 「競爭風險很高」 | 對手把同款降到你的六成，你三日內要回覆 |
| Actor | none | 本地最大的同業 |
| Trigger | none | 你公開報價之後 |
| Observation | none | 客戶拿報價來問你為什麼貴 |
| Answerable | no | yes — what do you do |

A situation that cannot be answered by the user in his own words is not finished. Neither is one
whose answer changes nothing.

## Step 1 — dispatch the lenses

1. **Write the idea in one line**, taken from the summary, and give that same line to every lens. Six
   subagents reviewing six slightly different objects produce six reports about different things.
2. **Pick the lenses** from `references/lenses.md`. Default is the first four: `反面鋼人`, `機制`,
   `前提審計`, `失敗模式`. Add one only when the summary earns it — a counterparty earns
   `對手反應`, a date earns `時間與次序`. Six is the ceiling.
3. **Dispatch in parallel, one lens per subagent**, using `assets/subagent-brief.md` verbatim with the
   two placeholders filled. Subagents are read-only, cannot ask the user, and return situation blocks
   only.
4. **Keep every return verbatim** in `~/thoughts/<topic_name>/refine-raw/<NN-lens>.md`. The merge is
   auditable only while the inputs survive; a summary of six reports with no reports behind it is the
   agent's own opinion in six voices.
5. **Verify each situation before it is admitted**, because a subagent's confidence is not evidence:
   - the quoted summary line exists in `summary.md` **verbatim** — if not, the situation rests on an
     invented premise and is dropped;
   - it is not already answered in the summary;
   - it carries an actor and an observable event;
   - it asks rather than advises, and it asks for a decision rather than for a sum — a situation
     whose question is 「成本相差幾多」 is a calculation the agent should have done, not a moment the
     user must handle;
   - it does not re-ask something the summary's 「詞的用法」 already defines.
6. **Merge by decision point.** Several lenses land on the same moment; that is the strongest signal
   in the skill, so record one row and name every lens that found it. The count is the 共識 column and
   it is checked mechanically against the raw files.
7. **Order** by: ① does it threaten a line the summary establishes (yes before no) ② when does it
   arrive (now, this quarter, this year, undated last) ③ convergence count ④ irreversibility.

## Step 2 — ask, one at a time

Ask in the ranked order. Present each situation in three parts, in the user's language:

> **觸發**：你公開報價之後第二日，本地最大的同業把同款降到你的六成。
> **觀察**：客戶拿著兩份報價來問你，為什麼你貴。
> **需要你決定**：你怎麼回覆？

Rules:

- **One situation per turn.** Two at once and the second is answered with the first one's logic.
- **No options, no recommendation.** 「A 還是 B」 makes the user choose from the agent's imagination.
  When he asks what the agent would do, answer him — and label it as the agent's reading, kept out of
  the document. His answer is the record.
- **Record before asking the next.** Append to `qa.md`, numbering continuing from the transcript, with
  the lens and the scenario id in the heading: `### Q17 · refine S04 · 機制`.
- **Silence is thinking.** Do not fill it with a smaller version of the question.
- **A non-answer is an answer.** 「再看看」 is recorded as 未定, not as agreement and not as refusal.
- **Stop when the user stops.** Unasked situations stay in the report as 未答; a report with three
  honest blanks beats a report where the blanks were filled by inference.

Classify each answer while recording it:

| 判定 | Meaning |
| --- | --- |
| 已定 | the answer carries an observable criterion — something that would show it holds |
| 部分 | a direction, no criterion yet |
| 未定 | the user explicitly deferred it |
| 未答 | never asked, or the session ended first |

## Step 3 — write the report

`~/thoughts/<topic_name>/refine.md`:

```markdown
# <topic_name> — refine 2026-11-17

一句話：<the idea in one line>

## 鏡頭

| 鏡頭 | 回傳情境 | 空回報的理由 |
| --- | --- | --- |
| 反面鋼人 | 4 | — |
| 機制 | 3 | — |

## 情境與答覆

| id | 情境 | 鏡頭 | 共識 | 你的答覆 | 判定 |
| --- | --- | --- | --- | --- | --- |
| S01 | 第一批客戶全是你認識的人 | 反面鋼人:S02, 前提審計:S05 | 2 | 「三個月內要找兩個不認識的買家」[Q15] | 已定 |
| S02 | 對手降到六成 | 對手反應:S01 | 1 | — | 未答 |

情境中的具體數字、人名與對手報價均為假設，不是紀錄中的事實。

## 這次 refine 改變了什麼

- summary.md 第 3 條：原句以 ~~…~~ 標記，改為「…」[Q17]

## 仍然未定的

- S02：對手降價的回覆方式，卡在還沒有任何定價授權的紀錄

## 沒有被問到的

- `失敗模式` 回傳 0 條：summary 裡的失敗都不具不可逆性
```

Then the upstream effects, in this order:

1. **Amend `summary.md`** where an answer changed the thought — append-only, struck through with
   `→ 由 Q<n> 取代`, exactly as `brainstorming` requires. Never rewrite the old line.
2. **Mark the diagrams stale** if the summary moved: `visual.md` gets a line naming which diagrams the
   change invalidates, and `visualize` step 2 regenerates them. A picture that still shows the old
   summary is the most persuasive wrong thing in the folder.
3. **Update `README.md`**: the open threads the refine closed, and the ones it opened.
4. **Read the report against the Verification list** in one pass, top to bottom — the verdicts, the `[Qn]`
   references and the consensus counts are what that list is for.

## Rules of the report

- **No verdict on the idea.** 「這個方向成立」 is the agent rating what the user answered. Report the
  state: which situations are settled, on what criterion, and which are not.
- **No plan.** The report holds what was decided under pressure; turning it into steps is a later,
  separate task the user may ask for.
- **No invented answers.** An empty cell means the user has not answered. Filling it with a plausible
  position is the single worst failure this skill can commit, because the document then argues in his
  name.
- **Declarative sentences**, same discipline as `brainstorming`: a negative claim first builds the
  strongest version of what it refutes, then names the observation that breaks it.

## Pitfalls

- **Six lenses, one report.** If the raw returns repeat each other, the dispatch was wrong: lenses
  overlap because their questions were paraphrases. Merge honestly and note it; do not present the
  same finding six times as six findings.
- **Situations that are really advice.** 「你應該先做小規模測試」 is a recommendation wearing a
  scenario's clothes. The test: does it end in a question the user answers?
- **The comfortable situation.** A lens that returns only things the user has already handled looks
  productive and tests nothing. Check every admitted situation against the summary for "already
  answered".
- **Interview fatigue.** Twelve situations is a questionnaire. Order them and stop when the user's
  answers stop being specific; the rest go in the report as 未答.
- **Silent merge.** A row whose 共識 count cannot be traced to raw files is a fabricated convergence.
  The checker exists for this.
- **A calculation dressed as a question.** 「第三位導師的時薪除以時數之後，每小時成本相差幾多？」
  hands the user arithmetic. The agent computes, then asks what he does about the answer.
- **Refine as validation ritual.** If every situation is answered with 「已經想過」, the lenses were
  aimed at the summary instead of past it. Go back to `brainstorming` for a sharper one.

## Verification

- [ ] `refine-raw/` holds one verbatim return per dispatched lens.
- [ ] Every quoted summary line in the report exists in `summary.md` verbatim.
- [ ] Every row's 共識 count equals the lenses it names, and each names a real `Sxx` in that lens's return.
- [ ] Every 已定 row carries an observable criterion and a `[Qn]` that exists in `qa.md`.
- [ ] 未答 rows carry no answer.
- [ ] Every verdict cell, `[Qn]` reference, consensus count and `qa.md` numbering was checked against the
      report itself, not against an earlier draft.
- [ ] `summary.md`, `visual.md` and `README.md` were updated if an answer moved the thought.
