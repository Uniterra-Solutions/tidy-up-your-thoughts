"""Tidy Up Your Thoughts — bundled Hermes skills for thinking hygiene.

Each directory under ``skills/`` that contains a ``SKILL.md`` is registered with
``ctx.register_skill()``, which makes it loadable as
``skill_view("tidy-up-your-thoughts:<name>")``.

Registered skills are read-only: they are never copied into ``~/.hermes/skills/``
and cannot be edited (or curated) there. Disabling the plugin removes them from
the index without deleting anything.
"""

from pathlib import Path

_SKILLS_DIR = Path(__file__).parent / "skills"


def _description(skill_md: Path) -> str:
    """The frontmatter ``description:`` — the line the model matches on in <available_skills>.

    ``ctx.register_skill`` only forwards a description it is handed, so read the
    frontmatter here rather than shipping blank index entries.
    """
    try:
        text = skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    head = text[3:end] if end != -1 else text[3:]
    for line in head.splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip().lower() == "description":
            return value.strip().strip('"').strip("'")
    return ""


def register(ctx):
    """Register every bundled skill directory under the plugin's namespace."""
    if not _SKILLS_DIR.is_dir():
        return
    for child in sorted(_SKILLS_DIR.iterdir()):
        skill_md = child / "SKILL.md"
        if child.is_dir() and skill_md.exists():
            # The name becomes "<plugin>:<child.name>".
            ctx.register_skill(child.name, skill_md, description=_description(skill_md))
