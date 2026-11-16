#!/usr/bin/env python3
"""Check a draft issue body before it is published. The gate before `gh`.

    python3 check_issue.py draft.md
    python3 check_issue.py draft.md --deny "Acme,alice,private-repo"

An incident report is an internal document and may name the repository, the file, the person and the
price. An issue is public: read by strangers, indexed by search engines, mirrored by everything that
watches the tracker. This script holds the publishable text to the parts of that boundary a machine can
see:

1. **No absolute or home-relative paths.** `/Users/<name>/…`, `/root/…`, `/home/…`, and `~/<something>`
   outside the plugin's own conventions all name an environment or a person.
2. **No contact or network identifiers.** Emails, IPv4 literals, and URLs whose host is not GitHub.
3. **No bare commit shas.** A seven-to-forty character hex token in inline code is a revision of some
   repository, and a private repository's revision is an identifier.
4. **No deny words.** Whatever the author knows is identifying and a script cannot: client names, people,
   repository names, product names. Passed as `--deny`.
5. **A redaction line exists.** `脫敏：…` or `Redaction: …` with content, so the published text says what
   was removed instead of leaving the reader to assume nothing was.
6. **No quote long enough to attribute.** A quoted sentence over 120 characters survives a search engine
   and identifies whoever wrote it.

Exit 1 on any violation. What is not checked: whether a scrubbed sentence is still re-identifiable to
someone who knows the project, and whether the issue duplicates one already open. Those are readings, and
they are the last two things to do before `gh`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ABS_PATH = re.compile(r"(?<![\w~])/(?:Users|root|home|srv|opt|mnt|Volumes)/\S+")
HOME_PATH = re.compile(r"~/[A-Za-z0-9._-]+")
HOME_ALLOW = ("~/thoughts", "~/.hermes", "~/hooks", "~/projects")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]{2,}")
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
URL = re.compile(r"https?://([^\s/>)\]]+)")
SHA_INLINE = re.compile(r"`([0-9a-f]{7,40})`")
QUOTED = re.compile(r"[「“\"]([^」”\"]{121,})[」”\"]")
REDACTION = re.compile(r"^\s*(?:脫敏|Redaction)\s*[:：]\s*(\S.{7,})$", re.M)
ALLOWED_HOSTS = ("github.com", "www.github.com", "raw.githubusercontent.com", "gist.github.com")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("draft", type=Path)
    ap.add_argument("--deny", default="", help="comma-separated identifying words to reject")
    ap.add_argument("--allow-url", action="append", default=[], help="extra hostname to allow")
    args = ap.parse_args()

    if not args.draft.exists():
        print(f"FAIL no such draft: {args.draft}", file=sys.stderr)
        return 1
    text = args.draft.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []

    for m in ABS_PATH.finditer(text):
        problems.append(f"absolute path: {m.group(0)[:70]}")
    for m in HOME_PATH.finditer(text):
        if not m.group(0).startswith(HOME_ALLOW):
            problems.append(f"home-relative path: {m.group(0)}")
    for m in EMAIL.finditer(text):
        problems.append(f"email: {m.group(0)}")
    for m in IPV4.finditer(text):
        problems.append(f"ip address: {m.group(0)}")
    for m in URL.finditer(text):
        host = m.group(1).split(":")[0].lower()
        if host not in ALLOWED_HOSTS and host not in [h.lower() for h in args.allow_url]:
            problems.append(f"url outside github: {m.group(0)[:70]}")
    for m in SHA_INLINE.finditer(text):
        problems.append(f"bare revision in inline code: `{m.group(1)}`")
    for m in QUOTED.finditer(text):
        problems.append(f"quote of {len(m.group(1))} chars — long enough to attribute")

    deny = [w.strip() for w in args.deny.split(",") if w.strip()]
    low = text.lower()
    for w in deny:
        if w.lower() in low:
            problems.append(f"deny word present: {w}")

    if not REDACTION.search(text):
        problems.append("no redaction line: add 「脫敏：<what was removed>」 or 「Redaction: <what was removed>」")

    for p in dict.fromkeys(problems):
        print(f"FAIL {p}")
    print(f"\n{len(text.splitlines())} line(s), {len(deny)} deny word(s), {len(problems)} problem(s)")
    print("Unjudged: whether a scrubbed sentence still identifies the project to someone who knows it,")
    print("and whether an issue for this mechanism is already open. Search, then read, then post.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
