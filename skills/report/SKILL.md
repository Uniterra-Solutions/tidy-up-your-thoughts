---
name: report
description: "Use when the process misfired: turn the incident into an anti-pattern."
version: 0.3.1
author: Tsz Kin Lai (LaiTszKin), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [process, retrospective, anti-pattern, self-correction]
    related_skills: []
---

# Report — an incident into a class of prevention

This skill is used when the workflow itself misfired: a skill was followed and the result was wrong, a
step was skipped without anything noticing, a script reported success it did not achieve, or the user
had to correct the agent on something the process should have caught.

The deliverable is not an apology and not a log. It is **one abstract anti-pattern** and **one class of
change** to the process that makes the same class of failure harder next time. The incident is only
evidence; the anti-pattern is the finding.

This is the agent's own incident report. `tidy` writes the report about the user's topic; this writes
the report about the process that was supposed to handle it.

## When to use

- A skill in this plugin, or in `pdd`, produced a wrong or unusable result.
- The user corrects the process rather than the content: 「你應該先…」「這一步不需要」「你怎麼會這樣做」.
- A script's output contradicted reality — a render that reported success with no file, a checker that
  passed a broken artefact.
- The same correction arrives a second time. That is the strongest trigger: the first time is noise,
  the second time is a missing rule.

## When not to use

- The content was wrong because the user changed his mind. That is a revision, not a process defect.
- The mistake was a one-off slip with no guidance behind it and no repeat in sight. Note it in the
  session and move on; writing a rule for every slip produces a process nobody can follow.
- The user wants the deliverable fixed. Fix it, then come back here if the fix exposed a rule.

## Step 1 — the guidance behind the mistake

An incident is not explained by the agent being careless. Carelessness is what the process exists to
absorb. The explanation is a sentence somewhere that made the wrong action look correct, and that
sentence can be found and quoted.

Locate the incident in one of three shapes:

| Shape | What it looks like | What it costs |
| --- | --- | --- |
| **Misleading rule** | a guideline that, read honestly, produces the wrong action | quote it, line and file |
| **Silent gap** | no guideline covers the moment; the agent improvised | name the file where the rule belongs |
| **Conflicting rules** | two guidelines both apply and disagree; the agent picked one | quote both, say which won and why |

Rules for this step:

1. **Quote the guideline verbatim, with file and line.** `skills/refine/SKILL.md:64`. An incident
   reported from memory cannot be checked, and the fix will land in the wrong place.
2. **Reconstruct what the agent believed at the time.** One declarative sentence: 「當時的讀法是
   X，因為 SKILL.md 第 N 行寫 Y。」 The belief is the object of the fix, not the agent's character.
3. **A gap is a finding, not a dead end.** 「沒有指引」 names where a rule should sit and what it must
   say. The absence of an instruction is the most common cause and the easiest to fix.

## Step 2 — the anti-pattern

An anti-pattern is the incident with the specifics removed: repeatable, nameable, and recognisable in
a different task. Write it with six fields, no free prose:

```
### AP-004 · 合併後才驗格式

- 觸發：多個 subagent 的回報需要合成一份產物時
- 錯誤動作：先把六份合成一份，再檢查格式
- 為何看起來合理：合併像整理，檢查像挑錯；整理在前符合直覺
- 正確動作：逐份對照規格驗一次，全部通過才合併
- 可觀察徵兆：合併完成後才出現一輪格式修補
- 來源：2026-11-16 refine 首次實戰
```

The abstraction test: **put the anti-pattern on a different task.** If a completely unrelated workflow
would recognise itself in it, it is abstract enough. If it names a file, a product, or a date outside
the 來源 field, it is still an incident, not a pattern.

Name it by the action, not by the character: 「合併後才驗格式」 describes what happened; 「粗心」 describes
nobody and fixes nothing.

## Step 3 — one class of change

Four classes. Pick exactly one as the primary fix, and record the others as rejected with a reason —
the choosing is the diagnostic work, and a report that proposes all four has not diagnosed anything.

| Class | What it changes | Use it when | Cost |
| --- | --- | --- | --- |
| **流程改進** | the process itself: steps, gates, ownership, order | the same failure recurs across tasks, or a step necessarily produces it | highest — restructures the method, needs a version argument |
| **提示改進** | one declarative sentence in the skill that states the correct action | the failure is local to one skill and one sentence prevents it | low |
| **資訊改進** | knowledge written into context: how a tool behaves, what a term means, what the environment is | the agent acted on wrong or missing facts, and its judgement was fine | low |
| **代碼改進** | a script's behaviour: its checks, its output, its failure reporting | the tool reported something untrue, or could have caught it and did not | medium |

Ask in this order, and stop at the first yes:

1. **Can the correct action be stated in one declarative sentence that the agent will read before the
   moment recurs?** If yes → 提示改進. This is the answer in most cases, and reaching past it is usually
   over-engineering.
2. **Was the agent's factual context wrong or missing?** If yes → 資訊改進. Distinguish this honestly
   from 「I had the fact and chose otherwise」, which is a prompt problem.
3. **Did a script assert something untrue, or stay silent where it could have failed loudly?** If yes
   → 代碼改進.
4. **Is this failure structural — repeated across tasks, or produced by the step order itself?** If yes
   → 流程改進, and write the argument: the strongest version of the prompt-only fix, and why it does not
   reach this class of failure.

**流程改進 carries a burden of proof.** Before it is chosen, build the best case for the cheaper fix
and state the observation that defeats it. A process change proposed without that argument is a
preference, and preferences accumulate into a method nobody follows.

## Step 4 — land it, then write it

The improvement is applied in the same session, not queued:

- **提示改進** — edit the skill's `SKILL.md` (or its reference) where the moment occurs, and bump that
  skill's `version`. A rule added without a version bump cannot be told apart from one that was always
  there.
- **資訊改進** — write the fact into the place that will be read at the right time: the skill's
  `references/`, the topic's 詞的定義, or the repo's environment note. State the fact, its source, and
  the date it was checked.
- **代碼改進** — fix the script, then add the case that would have caught it to the script's own
  fixture or to a test. A checker that failed once silently is a checker with a missing case.
- **流程改進** — restructure the steps, update every skill whose flow changed, and write the version
  history entry that explains what moved.

Then write the report, and the regression criterion it ends on:

> **回歸判準**：下次出現同一情境時，什麼可觀察的東西會不同。

Without that sentence the fix cannot be verified, and the next session will re-litigate the incident
from memory.

### Where the report goes

The skill is installed in two plugins and the destination differs by host. Resolve it from your own
`skill_dir`:

| Loaded from | Report | Anti-pattern index | Issue repo |
| --- | --- | --- | --- |
| `tidy-up-your-thoughts:report` | `~/thoughts/<topic_name>/friction/YYYY-MM-DD-<slug>.md` | `~/thoughts/_anti-patterns.md` | `Uniterra-Solutions/tidy-up-your-thoughts` |
| `pdd:report` | `<repo>/docs/retro/YYYY-MM-DD-<slug>.md` | `<repo>/docs/retro/ANTI-PATTERNS.md` | `Uniterra-Solutions/pdd-software-development` |

Both are append-only. The index carries one line per anti-pattern — id, title, date, the class of fix
chosen — so a later session can see whether it is recurring. `AP` ids are never reused or renumbered,
exactly as the study ids are not.

**The issue repo is the repo of the plugin that loaded this skill** — it is public, it is ours, and it is
the one place a later session looks. The product repository an incident happened in is never the
destination: that repository is the artefact, not the home of the process that produced it.

When a topic has no `~/thoughts/` directory because the incident happened outside a topic session,
write to `~/thoughts/_incidents/` and say so in the report.

## Step 5 — publish it as an issue

Publication is where an internal document becomes a public one. Two rules, in this order: **search before
writing**, **scrub before posting**.

### 5a. Search first; a matching issue gets a comment, not a twin

Dedupe on the anti-pattern, not on the incident. Two incidents with different artefacts but the same
mechanism are one issue, whatever each was called at the time.

`--repo` is always the **issue repo from the table in §4** — the plugin you were loaded from. Both values
are written here so that the destination never has to be inferred from the incident:

```
Uniterra-Solutions/pdd-software-development          # pdd:report
Uniterra-Solutions/tidy-up-your-thoughts             # tidy-up-your-thoughts:report
```

```bash
REPO=Uniterra-Solutions/<your row of §4>
gh issue list --repo "$REPO" --state all --limit 100 \
  --search "in:title,body <the mechanism, in three or four words>"
gh issue list --repo "$REPO" --state all --label anti-pattern --limit 50
```

Read the candidate bodies, not only the titles: an issue is titled by whoever opened it, and the same
mechanism arrives under different names.

| What the search finds | What you do |
| --- | --- |
| A mechanism match | `gh issue comment <n> --body-file <draft>` — the new AP id, the date, and what the new instance adds: a second occurrence, a new symptom, a regression criterion that failed |
| A mechanism match, already **closed** | Comment anyway. A recurrence is the strongest evidence the project can get, and the comment names the regression criterion that did not hold |
| Nothing that matches | `gh issue create --repo "$REPO" --title "[AP-00n] <anti-pattern title>" --body-file <draft>` |

Never open a second issue for a mechanism that already has one, whatever the new instance is called. Never
retitle someone else's issue to fit a new instance. Never reopen a closed issue: the comment carries the
recurrence, and the maintainer decides what the state should become.

Never open an `[AP-…]` issue in the product repository the incident concerned. That list is the product's
own defects; an anti-pattern filed there is invisible to the next session that needs it, and every later
search for the mechanism starts in the wrong tracker.

Record the outcome in the report's 落地 section and in the index row — `#<n>` for a comment,
`<issue repo>#<n>` for a new issue. An issue number that lives only in the session is one nobody will find
from the report.

### 5b. Scrub it: the report keeps the instance, the issue keeps the class

The report on disk is internal: it may name the repository, the branch, the file, the person, the price.
The issue is public — read by strangers, indexed by search engines, mirrored by tooling that watches the
tracker. Publication therefore requires removing everything that identifies the instance: the people, the
organisations, the product, the paths. **The tracker's own repository is not an instance detail** — it is
the destination named in §5a, and naming it is what makes the issue findable.

Remove before the draft leaves the machine:

- **People** — names, handles, initials, and job titles narrow enough to identify one person.
- **Organisations** — employer, client, vendor, funder, counterparty.
- **Projects** — repository names other than the plugin's own (the destination repo is not a leak; the
  product repo the incident happened in is), product names, internal service names,
  ticket prefixes, branch names, commit shas.
- **Paths and hosts** — any absolute path (`/Users/<name>/…`, `/root/…`, `~/<client>/…`), internal
  hostnames, IP and tailnet addresses, internal service ports.
- **Contact and identifiers** — emails, phone numbers, account and contract ids, invoice numbers.
- **Commercial detail** — prices, volumes, margins, and dates that pin an engagement to a fortnight.
- **Quotes long enough to attribute** — a quoted sentence that survives a search engine identifies who
  said it.

Keep, because this is what the issue is for:

- the **mechanism** and its **trigger**, in generic terms — 「a checker that both scopes the scan and
  resolves relative citations with one flag」;
- the **artefact class** — 「a per-directory agent-context file」, not a path inside a private repo;
- the **symptom as observed**, not as narrated — 「nine files reported `does not exist` while the files
  were present」;
- the **class of fix** and the **regression criterion**, which are already written abstractly.

Substitute rather than delete: 「the host repo」, 「a subagent」, 「a checker script」, 「a private
repository」. A scrubbed issue remains a complete lesson. If a sentence no longer makes sense without the
removed name, the sentence was about the instance — delete it rather than weaken the scrub.

Then let the check be the gate:

```
python3 scripts/check_issue.py <draft.md> --deny "<client>,<repo>,<person>"
```

It fails on absolute home paths, emails, IPv4 literals, non-GitHub URLs, bare commit shas, and any word
passed to `--deny`; it requires the body to carry a redaction line (`脫敏：…` or `Redaction: …`) so the
published text states what was removed. Passing is not the same as being un-re-identifiable — that is a
reading, and the reading is the last thing before `gh`.

The comment path is public too: the same rules apply to a comment body.

## Pitfalls

- **The apology.** 「這次我沒有先確認」 explains nothing and prevents nothing. The subject of the
  sentence is a guideline, or it is the wrong sentence.
- **The incident dressed as a pattern.** 「忘了把 plugin.yaml 的版本由 0.4.1 升到 0.4.2」 is not an
  anti-pattern; 「修改技能內容後未同步版本號」 is one.
- **Four fixes at once.** Proposing prompt, information, code and process changes for one incident
  means the cause was never located. Pick one, and state why the other three do not reach it.
- **The process change as reflex.** Restructuring the whole workflow for a single slip trades a small
  error for a large one. The prompt fix is the default; the process fix must defeat it in writing.
- **Knowledge mislabelled as judgement.** 「我不知道 CLI 會這樣」 and 「我知道，但我選了另一條路」 produce
  different fixes. Guessing which one it was guarantees the fix lands in the wrong class.
- **The fix left as a task.** 「下一步：更新 SKILL.md」 is the report failing at its own job. Edit the
  file in this session.
- **The issue that is a paste of the report.** The report is internal and may name the repository, the
  branch and the person; the issue is public. A body carrying a path, a handle or a price has not been
  published, it has leaked.
- **The duplicate opened because the search used the incident's words.** Searching for the file, the
  product or the client finds nothing; searching for the mechanism in three words finds the issue that has
  been open for months. Search the pattern, not the story.
- **The recurrence filed as a new issue.** A second occurrence of an existing mechanism is evidence, and
  evidence belongs in the thread it supports. A new issue splits the history and resets the count to one.
- **The scrub that kept the quote.** A quoted sentence long enough to search for is an identifier. Keep the
  claim, drop the sentence, or paraphrase it into the mechanism.
- **Posting before checking.** `gh` is the step after the scrub and the search, never the step that
  discovers there was already an issue.
- **The index that never grows.** An anti-pattern written into an index nobody reads has the same
  effect as none. Add a line to the index and point the next session at it.

## Verification

- [ ] The report quotes at least one guideline with file and line, or names the file where a missing
      rule belongs.
- [ ] The anti-pattern has all six fields and passes the different-task test.
- [ ] Exactly one improvement class is chosen; the other three are recorded as rejected with reasons.
- [ ] A 流程改進 carries the argument against the cheaper prompt fix.
- [ ] The improvement is already in the files, with the skill version bumped.
- [ ] The regression criterion names something observable.
- [ ] The anti-pattern is appended to the host's index with a fresh id.
- [ ] `scripts/check_friction.py <report path>` exits 0.
- [ ] The tracker was searched for the mechanism before writing; a match received a comment on the
      existing issue, and the report names `#<n>` or `<issue repo>#<n>`.
- [ ] The issue sits in the §4 issue repo of the plugin that loaded this skill — never in the product
      repository the incident happened in.
- [ ] The draft passed `scripts/check_issue.py <draft> --deny "<identifying words>"`, and carries its
      redaction line.
- [ ] No person, organisation, project, path, host, identifier or price from the instance appears in the
      public text.

## References

- `references/gate-discipline.md` — five rules for the checkers these skills run, extracted from AP-001 to
  AP-005. Read it before trusting a green run, and before filing an incident as "a script said it passed".
- `assets/report-template.md` — the skeleton, with what each section is for.
- `scripts/check_friction.py` — the mechanical shadow of this skill's rules.
