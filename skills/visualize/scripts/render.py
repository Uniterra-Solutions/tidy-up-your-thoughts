#!/usr/bin/env python3
"""Render every diagram of one thought topic, and check the rules the skill can check mechanically.

    python3 render.py ~/thoughts/<topic>            # render diagrams/*.mmd -> .png + .svg
    python3 render.py ~/thoughts/<topic> --check    # rules only, no rendering

Two rules are enforceable without judgement, so they are enforced here rather than hoped for:

1. **Provenance.** Every `.mmd` must open with `%% source:` naming the summary lines it came from.
   A diagram with no source is a diagram the agent invented.
2. **It renders.** mermaid-cli reports syntax errors on stderr and writes no file; a missing PNG
   after a zero exit is the failure mode, so the file is checked, not the exit code.

The rest — does the diagram say what the summary says, is it readable, does it answer one question —
needs eyes. This script cannot see, so it stops where seeing starts.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path

MISSING_SOURCE = "missing `%% source:` header — name the summary lines this diagram came from"
SCALE = "2"


def _diagrams(topic: Path) -> list[Path]:
    d = topic / "diagrams" if (topic / "diagrams").is_dir() else topic
    return sorted(p for p in d.glob("*.mmd"))


def _mmdc() -> list[str] | None:
    if exe := shutil.which("mmdc"):
        return [exe]
    if shutil.which("npx"):
        return ["npx", "-y", "@mermaid-js/mermaid-cli"]
    return None


def _source_header(src: Path) -> str | None:
    for line in src.read_text(encoding="utf-8", errors="replace").splitlines()[:8]:
        if line.strip().startswith("%% source:"):
            return line.split("source:", 1)[1].strip()
        if line.strip() and not line.strip().startswith("%%"):
            break  # the diagram body started: no header above it
    return None


def _render(cmd: list[str], src: Path, out: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        [*cmd, "-i", str(src), "-o", str(out), "-b", "white", "-s", SCALE, "-q"],
        capture_output=True, text=True, timeout=180,
    )
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip().splitlines()
        return False, err[0][:160] if err else f"exit {proc.returncode}"
    if not out.exists() or out.stat().st_size < 1024:
        return False, "no output written (renderer reported success)"
    return True, ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("topic", type=Path)
    ap.add_argument("--check", action="store_true", help="rules only; do not render")
    args = ap.parse_args()

    if not args.topic.is_dir():
        print(f"not a directory: {args.topic}", file=sys.stderr)
        return 2
    sources = _diagrams(args.topic)
    if not sources:
        print(f"no .mmd files under {args.topic}/diagrams")
        return 1

    problems: list[str] = []
    for src in sources:
        if _source_header(src) is None:
            problems.append(f"{src.name}: {MISSING_SOURCE}")

    if args.check:
        for p in problems:
            print(f"FAIL {p}")
        print(f"{len(sources)} diagram(s) checked, {len(problems)} rule failure(s)")
        return 1 if problems else 0

    cmd = _mmdc()
    if cmd is None:
        print("no mmdc and no npx on PATH — cannot render", file=sys.stderr)
        return 2

    failures = 0
    for src in sources:
        png, svg = src.with_suffix(".png"), src.with_suffix(".svg")
        started = time.time()
        ok, err = _render(cmd, src, png)
        ok_svg, err_svg = _render(cmd, src, svg) if ok else (False, err)
        mark = "ok  " if ok and ok_svg else "FAIL"
        size = f"{png.stat().st_size // 1024}K" if png.exists() else "-"
        print(f"{mark} {src.name:<34} {size:>6}  {time.time() - started:4.1f}s")
        if not (ok and ok_svg):
            failures += 1
            print(f"     {err or err_svg}")

    for p in problems:
        print(f"WARN {p}")
    print(f"\n{len(sources)} source(s), {failures} render failure(s), {len(problems)} rule warning(s)")
    print("Look at the PNGs before delivering them: a render proves syntax, not intent.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
