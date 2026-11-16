# tidy-up-your-thoughts

A Hermes plugin that ships its skills as **bundled** skills — same packaging as
[`pdd-software-development`](https://github.com/Uniterra-Solutions/pdd-software-development):
the skills live in the plugin registry, never in `~/.hermes/skills/`, and cannot be
edited by `skill_manage` or the curator.

## Skills

| Qualified name | What it does |
| --- | --- |
| `tidy-up-your-thoughts:brainstorming` | Socratic questioning that keeps every question at the abstract layer an outsider could answer, mirrors each answer back for correction, and writes the whole exchange to `~/thoughts/<topic_name>/` as a declarative record (`qa.md`, `summary.md`, `README.md`) — negation only after the steelman it refutes has been built in full |

## Install

```bash
hermes plugins install Uniterra-Solutions/tidy-up-your-thoughts --enable
```

While developing from this checkout, link it in instead — `hermes plugins install`
takes a catalog name, a git URL or `owner/repo`, and refuses a bare local path:

```bash
ln -sfn ~/tidy-up-your-thoughts "$HERMES_HOME/plugins/tidy-up-your-thoughts"
hermes plugins enable tidy-up-your-thoughts
```

Disabling removes the skills from the index and deletes nothing:

```bash
hermes plugins disable tidy-up-your-thoughts
```

## Layout

```
plugin.yaml                    manifest: name, version, description, licence
__init__.py                    register(ctx) — one register_skill() per skills/<dir>/SKILL.md
skills/brainstorming/
├── SKILL.md                   the workflow and the three laws
└── references/
    ├── question-patterns.md   fourteen Socratic moves, with failure modes
    └── writing-rules.md       declarative voice, the negation protocol, the closing lint
```

## Adding a skill

1. Create `skills/<name>/SKILL.md`.
2. Frontmatter must carry at least `name` and `description`:

   ```yaml
   ---
   name: <name>
   description: "Use when <trigger>. <what it does>."
   version: 0.1.0
   author: Tsz Kin Lai (LaiTszKin), Hermes Agent
   license: MIT
   platforms: [linux, macos, windows]
   metadata:
     hermes:
       tags: [thinking, <topic>]
   ---
   ```

   `description` is the only line the model matches on in `<available_skills>`;
   `__init__.py` reads it out of the frontmatter and forwards it to
   `ctx.register_skill`, so a wrong description means a skill nobody loads.
3. Supporting material goes beside it, never in a flat pile:
   `references/<topic>.md`, `assets/<template>`, `scripts/<tool>`.
4. Bump `version` in `plugin.yaml` and commit. A running gateway keeps the old
   registration until it restarts.

## What "bundled" buys you

- The skills live in the plugin registry, **not** in `~/.hermes/skills/`. They are
  read-only: `skill_manage`, the curator and background review passes cannot edit
  them.
- They still appear in `skills_list` and in the system prompt's
  `<available_skills>` index while the plugin is enabled, under their qualified
  names.
- The qualified name is what resolves unambiguously; a bare `skill_view("name")`
  can still hit an on-disk skill of the same name.

## Verifying a change

```bash
# 1. manifest, register() run in isolation, security scan — the cheap gate
hermes plugins validate .

# 2. what the live plugin manager actually registered (use the interpreter that
#    carries Hermes's own dependency closure; a plain python3 dies on ruamel)
VP=$(ls -d ~/.hermes/installs/*/environments/*/venv/bin/python3 | head -1)
env -u PYTHONPATH "$VP" - <<'PY'
import sys; from pathlib import Path
sys.path.insert(0, str(Path.home()/".hermes/hermes-agent"))
from hermes_cli.plugins import get_plugin_manager
pm = get_plugin_manager(); pm.discover_and_load()
print(sorted(pm._plugins))
for name, meta in sorted(pm._plugin_skills.items()):
    print(name, "|", meta.get("description", "")[:70])
PY
```

Then, in a **new** session (registered skills are snapshotted at startup), confirm
`skills_list` shows `tidy-up-your-thoughts:brainstorming`.

## Licence

MIT, Uniterra Solutions Ltd.