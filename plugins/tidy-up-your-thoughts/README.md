# Tidy Up Your Thoughts

Six skills that take an unstructured pile to a written conclusion. `brainstorming` asks Socratic questions and
records every exchange; `refine` stress-tests the idea with four read-only lenses and one situation at a time;
`visualize` draws the summary as mermaid diagrams and folds corrections back into the summary rather than the
picture; `tidy` writes `report.md` for a reader who was not there; `diagnose` extracts three to seven
load-bearing concepts from a supplied text and probes them one at a time, every verdict quoting the line it
rests on; `report` turns an incident in the process into one anti-pattern and one class of fix.

## Install

This folder is a portable Agent Plugins 1.0 package, so several hosts read it directly:

- **Claude Code** — `/plugin marketplace add Uniterra-Solutions/tidy-up-your-thoughts`, then
  `/plugin install tidy-up-your-thoughts@tidy-up-your-thoughts`.
- **Codex** — `codex plugin marketplace add Uniterra-Solutions/tidy-up-your-thoughts`, then
  `codex plugin add tidy-up-your-thoughts@tidy-up-your-thoughts`.
- **Grok Build** — `grok plugin marketplace add Uniterra-Solutions/tidy-up-your-thoughts`, then
  `grok plugin install tidy-up-your-thoughts --trust`.
- **Muse** — `muse plugins marketplace add tidy-up-your-thoughts Uniterra-Solutions/tidy-up-your-thoughts`,
  then `muse plugins install tidy-up-your-thoughts@tidy-up-your-thoughts` and `muse plugins approve
  tidy-up-your-thoughts`.

The repository README covers each route in full, including the Hermes Agent plugin install and how the four
manifests relate. Skills arrive namespaced as `tidy-up-your-thoughts:<skill>` on every host.
