#!/usr/bin/env python3
"""Mirror skills/ into the portable plugin at plugins/tidy-up-your-thoughts/ and keep its manifests in step.

The Hermes plugin (plugin.yaml + __init__.py) keeps reading skills/ at the repo root; this script copies
that tree into plugins/tidy-up-your-thoughts/skills/ so one folder is installable by Claude Code, Codex,
Grok Build and Muse while Hermes keeps reading the root copy.

    python3 scripts/build-agent-plugin.py          # sync + bump versions from plugin.yaml
    python3 scripts/build-agent-plugin.py --check   # CI: exit 1 when the mirror is stale
"""
import filecmp
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills"
PLUGIN = ROOT / "plugins" / "tidy-up-your-thoughts"
SKILLS = sorted(p.parent.name for p in SRC.glob("*/SKILL.md"))
MANIFESTS = [PLUGIN / "plugin.json", PLUGIN / ".codex-plugin" / "plugin.json",
             PLUGIN / ".muse-plugin" / "plugin.json"]


def version() -> str:
    match = re.search(r"^version:\s*(\S+)", (ROOT / "plugin.yaml").read_text(), re.M)
    return match.group(1) if match else "0.0.0"


def sync() -> None:
    out = PLUGIN / "skills"
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SRC, out, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    for path in MANIFESTS:
        manifest = json.loads(path.read_text())
        manifest["version"] = version()
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    muse = PLUGIN / ".muse-plugin" / "plugin.json"
    manifest = json.loads(muse.read_text())
    manifest["capabilities"]["skills"] = [{"id": s, "path": f"skills/{s}/SKILL.md"} for s in SKILLS]
    muse.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def check() -> int:
    problems = []
    for skill in SKILLS:
        src, dst = SRC / skill, PLUGIN / "skills" / skill
        if not dst.exists():
            problems.append(f"missing plugins/tidy-up-your-thoughts/skills/{skill}")
            continue
        cmp = filecmp.dircmp(src, dst)
        if cmp.diff_files or cmp.left_only or cmp.right_only:
            problems.append(f"stale mirror: {skill}")
    listed = [s["id"] for s in json.loads(MANIFESTS[2].read_text())["capabilities"]["skills"]]
    if listed != SKILLS:
        problems.append(f"muse lists {len(listed)} skills, skills/ has {len(SKILLS)}")
    for manifest in MANIFESTS:
        if json.loads(manifest.read_text()).get("version") != version():
            problems.append(f"version drift in {manifest.relative_to(ROOT)}")
    print("\n".join(problems) if problems else f"ok: {len(SKILLS)} skills mirrored")
    return 1 if problems else 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    sync()
    print(f"synced {len(SKILLS)} skills into plugins/tidy-up-your-thoughts (version {version()})")
