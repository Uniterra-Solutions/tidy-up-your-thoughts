#!/usr/bin/env python3
"""Check one incident report against the rules a machine can hold the writer to.

    python3 check_friction.py ~/thoughts/<topic>/friction/2026-11-16-foo.md
    python3 check_friction.py <report> --index ~/thoughts/_anti-patterns.md

Five checks, each of them the mechanical shadow of a rule in the skill:

1. **The cause is quoted.** A report whose explanation is prose has not located a guideline. One
   `path:line` citation is required, or — for a silent gap — a `缺口` line naming the file where the
   missing rule belongs.
2. **The anti-pattern is complete.** Every `### AP-nnn` entry carries all six fields. A missing
   «為何看起來合理» is the usual sign the pattern was asserted rather than analysed.
3. **One class of fix.** Exactly one `**改進類別**：` line, holding one of the four names, plus a
   `**未採用**：` line recording why the other three do not apply. Four fixes means no diagnosis.
4. **Process changes pay for themselves.** If 流程改進 was chosen, a `**為何不用提示**：` line must carry
   the argument against the cheaper fix.
5. **The regression criterion exists and is observable.** A `回歸判準` heading with a body, or an
    inline `回歸判準：` followed by content. An empty heading fails — a rule with a heading and no
    content is the shape this check was written to catch.

With `--index`, the ids in the report must appear in the index with the same titles, and no id may
appear twice. That is the check that keeps the index from drifting away from the reports.

Exit 1 on any violation.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CLASSES = ("流程改進", "提示改進", "資訊改進", "代碼改進")
AP_HEAD = re.compile(r"^###\s*(AP-\d{3})\s*·\s*(.+?)\s*$", re.M)
FIELDS = ("觸發", "錯誤動作", "為何看起來合理", "正確動作", "可觀察徵兆", "來源")
CITATION = re.compile(r"((?:skills/)?[\w./-]+\.(?:md|py|yaml)):(?:L)?(\d+)")
GAP = re.compile(r"缺口")
CLASS_LINE = re.compile(r"^\*\*改進類別\*\*：\s*(.+?)\s*$", re.M)
REJECTED_LINE = re.compile(r"^\*\*未採用\*\*：\s*(.+?)\s*$", re.M)
WHY_NOT_PROMPT = re.compile(r"^\*\*為何不用提示\*\*：\s*(.+?)\s*$", re.M)
REGRESSION_HEAD = re.compile(r"^#{1,6}\s*.*回歸判準.*$", re.M)
REGRESSION_INLINE = re.compile(r"回歸判準[：:]\s*(\S.{7,})")


def _regression(text: str) -> str:
    """The criterion itself: the body under a 回歸判準 heading, or the text after an inline colon.

    Matching the heading alone was the first version's bug: a report with an empty 回歸判準 heading
    passed, which is exactly the failure the check exists to catch.
    """
    head = REGRESSION_HEAD.search(text)
    if head:
        rest = text[head.end():]
        nxt = re.search(r"^#{1,6}\s", rest, re.M)
        body = (rest[: nxt.start()] if nxt else rest).strip()
        if len(body) >= 8:
            return body
    inline = REGRESSION_INLINE.search(text)
    return inline.group(1).strip() if inline else ""


def _ap_blocks(text: str) -> list[tuple[str, str, str]]:
    """(id, title, body) for each AP entry."""
    heads = list(AP_HEAD.finditer(text))
    out = []
    for i, m in enumerate(heads):
        body = text[m.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        out.append((m.group(1), m.group(2), body))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("report", type=Path)
    ap.add_argument("--index", type=Path, help="anti-pattern index to cross-check ids against")
    args = ap.parse_args()

    if not args.report.exists():
        print(f"FAIL no such report: {args.report}", file=sys.stderr)
        return 1
    text = args.report.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []

    if not CITATION.search(text) and not (GAP.search(text) and re.search(r"[\w./-]+\.(md|py)", text)):
        problems.append("no guideline cited: need a path:line reference, or a 缺口 line naming the file")

    blocks = _ap_blocks(text)
    if not blocks:
        problems.append("no AP-nnn entry: the finding is the anti-pattern, not the incident")
    for ap_id, title, body in blocks:
        for field in FIELDS:
            if not re.search(rf"^-\s*\**{field}\**：\s*\S", body, re.M):
                problems.append(f"{ap_id}: field {field} missing or empty")

    classes = CLASS_LINE.findall(text)
    if len(classes) != 1:
        problems.append(f"expected exactly one **改進類別** line, found {len(classes)}")
    elif classes[0] not in CLASSES:
        problems.append(f"改進類別 {classes[0]!r} is not one of {CLASSES}")
    if not REJECTED_LINE.search(text):
        problems.append("no **未採用** line: the three rejected classes and their reasons are the diagnosis")
    if any(c == "流程改進" for c in classes) and not WHY_NOT_PROMPT.search(text):
        problems.append("流程改進 without **為何不用提示**： a process change must defeat the cheaper fix in writing")

    if not _regression(text):
        problems.append("no 回歸判準 with content: the fix cannot be verified without one")

    if args.index:
        if not args.index.exists():
            problems.append(f"index missing: {args.index}")
        else:
            idx = args.index.read_text(encoding="utf-8", errors="replace")
            seen: dict[str, int] = {}
            for m in re.finditer(r"^\|\s*(AP-\d{3})\s*\|\s*(.+?)\s*\|", idx, re.M):
                seen[m.group(1)] = seen.get(m.group(1), 0) + 1
            for ap_id, title, _ in blocks:
                if ap_id not in seen:
                    problems.append(f"{ap_id} is not in the index")
                elif seen[ap_id] > 1:
                    problems.append(f"{ap_id} appears {seen[ap_id]} times in the index")

    for p in problems:
        print(f"FAIL {p}")

    print(f"\n{len(blocks)} anti-pattern(s), class: {classes[0] if classes else '—'}")
    print("Unjudged: whether the citation really caused the mistake, whether the anti-pattern survives")
    print("the different-task test, whether the chosen class is the right one. Read the reasoning.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
