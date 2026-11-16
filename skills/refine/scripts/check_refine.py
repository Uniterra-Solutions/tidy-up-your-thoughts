#!/usr/bin/env python3
"""Check one refine report against the rules that can be checked mechanically.

    python3 check_refine.py ~/thoughts/<topic>

Most ways a refine report can lie are structural, and structure is checkable:

- a row with a verdict and no answer, or 未答 carrying an answer;
- an answer citing a `[Qn]` that qa.md never numbered;
- qa.md with a gap in the numbering;
- a 判定 outside the four allowed words;
- a scenario attributed to a lens whose raw return never contained it (the merge invented a finding);
- a 共識 count that does not equal the number of lenses it names (the convergence was inflated);
- a session in which no raw returns were kept at all (the merge cannot be audited).

What stays unjudged: whether a situation is concrete, whether an answer is really the user's words,
whether the lenses are genuinely distinct. The report says so rather than implying a clean bill.

Exit 1 on any violation, 0 when the structure holds.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERDICTS = {"已定", "部分", "未定", "未答"}
ANSWERED = {"已定", "部分", "未定"}
SCENARIO_ID = re.compile(r"^S\d{2}$")
SCENARIO_HEAD = re.compile(r"^###\s*(S\d{2})\b", re.M)
Q_HEAD = re.compile(r"^###\s*Q(\d+)\b", re.M)
Q_REF = re.compile(r"\[Q(\d+)\]")
LENS_REF = re.compile(r"^(?P<lens>[^:]+):(?P<sid>S\d{2})$")


def _rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("| S"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6:
            rows.append(cells[:6])
    return rows


def _raw_returns(topic: Path) -> dict[str, set[str]]:
    """lens file name -> the S-ids its heading lines contain."""
    out: dict[str, set[str]] = {}
    d = topic / "refine-raw"
    if not d.is_dir():
        return out
    for f in sorted(d.glob("*.md")):
        out[f.stem] = set(SCENARIO_HEAD.findall(f.read_text(encoding="utf-8", errors="replace")))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("topic", type=Path)
    args = ap.parse_args()

    refine, qa = args.topic / "refine.md", args.topic / "qa.md"
    for f in (refine, qa):
        if not f.exists():
            print(f"FAIL missing {f.relative_to(args.topic)}", file=sys.stderr)
            return 1

    text = refine.read_text(encoding="utf-8", errors="replace")
    qa_text = qa.read_text(encoding="utf-8", errors="replace")
    q_numbers = sorted({int(m.group(1)) for m in Q_HEAD.finditer(qa_text)})
    q_set = set(q_numbers)
    raw = _raw_returns(args.topic)

    problems: list[str] = []
    counts = {v: 0 for v in VERDICTS}

    if not raw:
        problems.append("no refine-raw/*.md — the subagent returns must be kept for the merge to be auditable")

    rows = _rows(text)
    if not rows:
        problems.append("no scenario rows (table needs id / 情境 / 鏡頭 / 共識 / 答覆 / 判定)")

    seen: set[str] = set()
    for sid, scenario, lens_cell, consensus, answer, verdict in rows:
        if not SCENARIO_ID.match(sid):
            problems.append(f"{sid}: id must look like S01")
        if sid in seen:
            problems.append(f"{sid}: duplicate id")
        seen.add(sid)
        if not scenario:
            problems.append(f"{sid}: empty 情境")

        refs = [r.strip() for r in lens_cell.split(",") if r.strip()]
        parsed = []
        for ref in refs:
            m = LENS_REF.match(ref)
            if not m:
                problems.append(f"{sid}: lens ref {ref!r} is not <lens>:<Sxx>")
                continue
            parsed.append((m.group("lens"), m.group("sid")))
            hit = [name for name, ids in raw.items() if m.group("lens") in name]
            if not hit:
                problems.append(f"{sid}: no refine-raw file for lens {m.group('lens')!r}")
            elif not any(m.group("sid") in raw[name] for name in hit):
                problems.append(f"{sid}: {m.group('lens')}:{m.group('sid')} is not in that raw return")
        if consensus.isdigit() and parsed and int(consensus) != len(parsed):
            problems.append(f"{sid}: 共識 {consensus} but {len(parsed)} lens ref(s) named")

        if verdict not in VERDICTS:
            problems.append(f"{sid}: 判定 {verdict!r} is not one of {sorted(VERDICTS)}")
            continue
        counts[verdict] += 1
        if verdict in ANSWERED and answer in {"", "—", "-"}:
            problems.append(f"{sid}: verdict {verdict} with no recorded answer")
        if verdict == "未答" and answer not in {"", "—", "-"}:
            problems.append(f"{sid}: verdict 未答 but an answer is recorded")
        for ref in Q_REF.findall(answer):
            if int(ref) not in q_set:
                problems.append(f"{sid}: cites [Q{ref}], which qa.md does not contain")

    gaps = [n for n in range(1, (q_numbers[-1] if q_numbers else 0) + 1) if n not in q_set]
    if gaps:
        problems.append(f"qa.md numbering gaps at Q{', Q'.join(str(g) for g in gaps[:8])}")

    for p in problems:
        print(f"FAIL {p}")

    print(f"\n{len(rows)} scenario(s): " + ", ".join(f"{v} {counts[v]}" for v in sorted(VERDICTS)))
    print(f"qa.md: Q1..Q{q_numbers[-1] if q_numbers else 0}, {len(q_numbers)} exchange(s)")
    print(f"refine-raw: {len(raw)} lens return(s)")
    if counts["未答"]:
        print(f"NOTE {counts['未答']} situation(s) unanswered — they stay unanswered in the report.")
    print("Unjudged: concreteness, whose words the answers are, whether the lenses were distinct.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
