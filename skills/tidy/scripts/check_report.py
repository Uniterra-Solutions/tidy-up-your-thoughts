#!/usr/bin/env python3
"""Lint one report against the rules that survive being read by a machine.

    python3 check_report.py ~/thoughts/<topic>
    python3 check_report.py ~/thoughts/<topic> --outline   # just the topic sentences

What is checked, and why it is worth checking this way:

1. **A negative sentence may sit only inside a rebuttal.** Rule 3 of `tidy` is narrow on purpose:
   description is affirmative, and negation appears only where a counter-argument is being met. The
   lint finds the sentences carrying a negator and reports any that sit outside a section whose
   heading contains 反駁 (or between `<!-- rebuttal:start -->` and `<!-- rebuttal:end -->`). Idioms
   that contain a negator without negating (不同, 不僅, 未來 …) are skipped, and so are sentences
   describing the record's own state (尚未確立, 紀錄中 …), because stating that evidence is absent is
   affirmative about the evidence. Both lists, and the count of each, are printed so neither can grow
   quietly.
2. **No advice.** 應該 / 必須 / 建議 / 值得 are the report telling the user what to do; the report
   describes. Quoted spans (「…」) are exempt, since the user's own words may contain them.
3. **Citations resolve.** Every `[Qn]` exists in `qa.md`, every `[Sxx]` exists in `refine.md`.
4. **The topic sentences stand alone.** Printing the first sentence of every prose paragraph in order
   shows whether the report holds together as an outline; a first sentence over 60 characters is
   reported, because a topic sentence that needs the rest of the paragraph is not one.
5. **A terminology section exists.** Rule 2 of the skill has no mechanical test for accuracy, but a
   report with no 詞的定義 section has skipped the step entirely, and that is visible.

Exit 1 on any violation, 0 when the report is clean. Judgement — is the sentence true, is the
paragraph about its topic sentence, is the term defined correctly — stays with the reader.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NEGATORS = re.compile(r"(不是|並非|而非|否則|不能|不會|不可以|沒有|缺乏|不|沒|未|無)")
NEGATIVE_IDIOMS = ("不同", "不僅", "不但", "未來", "無論", "非常", "無疑", "不如", "不得不", "不由得")
# Statements about what the record holds, not about the world. 「尚未確立」 states the state of the
# evidence; 「客戶不會接受」 states a fact about a customer. Only the first kind is affirmative in
# content, and the report cannot describe an open question without it — its own section is 「尚未確立的」.
RECORD_STATE = ("尚未確立", "未確立", "尚未", "紀錄中", "條目中", "為零", "空白", "缺的是")
ADVICE = ("應該", "必須", "建議", "值得", "務必", "切忌")
QUOTED = re.compile(r"「[^」]*」")
CITATION = re.compile(r"\[(Q\d+|S\d{2})\]")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
SENTENCE_SPLIT = re.compile(r"(?<=[。！？!?])")
LIST_LINE = re.compile(r"^\s*([-*+]|\d+[.)])\s")
TABLE_LINE = re.compile(r"^\s*\|")

TOPIC_LIMIT = 60


def _sections(lines: list[str]) -> list[tuple[int, str]]:
    """(line index, heading text) for every heading, so a line can be located in a section."""
    out: list[tuple[int, str]] = []
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if m:
            out.append((i, m.group(2).strip()))
    return out


def _in_rebuttal(idx: int, heads: list[tuple[int, str]], flags: list[bool]) -> bool:
    if flags[idx]:
        return True
    current = ""
    for i, text in heads:
        if i <= idx:
            current = text
        else:
            break
    return "反駁" in current


def _rebuttal_flags(lines: list[str]) -> list[bool]:
    flags, inside = [], False
    for ln in lines:
        if "rebuttal:start" in ln:
            inside = True
        flags.append(inside)
        if "rebuttal:end" in ln:
            inside = False
    return flags


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("topic", type=Path)
    ap.add_argument("--outline", action="store_true", help="print topic sentences and stop")
    args = ap.parse_args()

    report = args.topic / "report.md"
    if not report.exists():
        print(f"FAIL no report.md in {args.topic}", file=sys.stderr)
        return 1
    qa = (args.topic / "qa.md")
    refine = (args.topic / "refine.md")

    text = report.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    heads = _sections(lines)
    flags = _rebuttal_flags(lines)

    q_ids = set(re.findall(r"^###\s*Q(\d+)\b", qa.read_text(encoding="utf-8", errors="replace"), re.M)) if qa.exists() else set()
    s_ids = set(re.findall(r"^\|\s*(S\d{2})\s*\|", refine.read_text(encoding="utf-8", errors="replace"), re.M)) if refine.exists() else set()

    problems: list[str] = []
    paraphrases = 0
    negatives_outside = 0
    record_state = 0
    outline: list[str] = []

    paragraph: list[str] = []

    def flush(par: list[str]) -> None:
        nonlocal paraphrases
        if not par:
            return
        body = " ".join(par).strip()
        if not body or body.startswith("|"):
            return
        first = SENTENCE_SPLIT.split(body)[0].strip()
        if first:
            outline.append(first)
            if len(first) > TOPIC_LIMIT:
                paraphrases += 1
                problems.append(f"topic sentence {len(first)} chars (limit {TOPIC_LIMIT}): {first[:50]}…")

    for idx, ln in enumerate(lines):
        stripped = ln.strip()
        if not stripped or HEADING.match(ln) or LIST_LINE.match(ln) or TABLE_LINE.match(ln) or stripped.startswith(("<!--", "```")):
            flush(paragraph)
            paragraph = []
            continue
        paragraph.append(stripped)

        if any(word in stripped for word in ADVICE):
            bare = QUOTED.sub("", stripped)
            if any(word in bare for word in ADVICE):
                problems.append(f"advice wording outside a quote: {stripped[:60]}")

        if _in_rebuttal(idx, heads, flags):
            continue
        for sentence in SENTENCE_SPLIT.split(stripped):
            if not sentence.strip():
                continue
            bare = QUOTED.sub("", sentence)
            if any(idiom in bare for idiom in NEGATIVE_IDIOMS):
                continue
            if any(phrase in bare for phrase in RECORD_STATE):
                record_state += 1
                continue
            if NEGATORS.search(bare):
                negatives_outside += 1
                problems.append(f"negative outside a rebuttal: {sentence.strip()[:60]}")
    flush(paragraph)

    for ref in CITATION.findall(text):
        if ref.startswith("Q") and ref[1:] not in q_ids:
            problems.append(f"cites [{ref}], absent from qa.md")
        if ref.startswith("S") and ref not in s_ids:
            problems.append(f"cites [{ref}], absent from refine.md")

    if "詞的定義" not in text and "術語" not in text:
        problems.append("no 詞的定義 / 術語 section — the terminology step was skipped")

    if args.outline:
        print("Topic sentences, in order:\n")
        for i, s in enumerate(outline, 1):
            print(f"{i:2}. {s}")
        print(f"\n{len(outline)} paragraph(s).")
        return 0

    for p in problems:
        print(f"FAIL {p}")

    print(f"\n{len(outline)} paragraph(s), {len(lines)} line(s), {len(text)} chars")
    print(f"negative sentences outside a rebuttal: {negatives_outside}")
    print(f"record-state statements (affirmative about the evidence): {record_state}")
    print(f"topic sentences over {TOPIC_LIMIT} chars: {paraphrases}")
    print(f"skip list for negator idioms: {', '.join(NEGATIVE_IDIOMS)}")
    print(f"skip list for record-state phrasing: {', '.join(RECORD_STATE)}")
    print("Unjudged: whether a sentence is true, whether a paragraph holds to its topic sentence,")
    print("whether a term is defined correctly. Run with --outline and read the spine.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
