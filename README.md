# tidy-up-your-thoughts

A Hermes plugin that ships its skills as **bundled** skills — same packaging as
[`pdd-software-development`](https://github.com/Uniterra-Solutions/pdd-software-development).

The skill set is deliberately empty right now. The skeleton, the registration
contract and the install path are in place and verified; skills are added one at a
time under `skills/<name>/SKILL.md` and become loadable immediately as
`skill_view("tidy-up-your-thoughts:<name>")`.

## Install

```bash
hermes plugins install Uniterra-Solutions/tidy-up-your-thoughts --enable
```

Or from this local checkout:

```bash
hermes plugins install ~/tidy-up-your-thoughts --enable
```

Disabling the plugin removes its skills from the index and deletes nothing:

```bash
hermes plugins disable tidy-up-your-thoughts
```

## Layout

```
plugin.yaml        manifest: name, version, description, licence
__init__.py        register(ctx) — one register_skill() call per skills/<dir>/SKILL.md
skills/            one directory per skill; empty for now
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
# 1. the module imports and register() enumerates the skills it should
python3 - <<'PY'
import sys, logging; from pathlib import Path
sys.path.insert(0, str(Path.home()/".hermes/hermes-agent"))
from plugins.plugin_loader import load_plugin_module
m = load_plugin_module("hermes_plugins.tidy_up_your_thoughts",
                       Path.home()/"tidy-up-your-thoughts",
                       parents=("hermes_plugins",), logger=logging.getLogger("x"))
class Ctx:
    def register_skill(self, n, p, description=""): print(n, "|", description)
m.register(Ctx())
PY

# 2. the CLI sees the installed plugin and its manifest
hermes plugins list | grep tidy
```

Then, in a **new** session (registered skills are snapshotted at startup), confirm
`skills_list` shows `tidy-up-your-thoughts:<name>`.

## Licence

MIT, Uniterra Solutions Ltd.
