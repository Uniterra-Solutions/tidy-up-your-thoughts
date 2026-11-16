# Gate discipline — five rules from five incidents

Every skill in this plugin ends in checkers: `check_agents_md.py`, `study_delta.py --verify`,
`render_graphs.py`, `check_history.py`, `find_plans.py`, plus whatever a round writes. A green run is
only evidence while the gate could have gone red for the right reason.

These five rules were extracted from AP-001 to AP-005 in `docs/retro/`. Each names the mechanism, the
observable symptom, and the move that prevents it. Read the four lines of a rule before quoting it; the
rule without its symptom becomes a slogan.

## Rule 1 — A gate's argument names what it resolves against

**Statement.** When a checker takes a root or a base path, the invocation states which artefact that
argument governs. Scope and resolution are different questions and are often answered by one flag.

**Mechanism.** A checker that resolves relative citations uses its root as the base. Point it at a
subdirectory and every citation crossing that boundary fails — the failures are real, reproducible, and
about the caller.

**Symptom.** A batch of files failing with the *same* message, while the thing being checked is visibly
present on disk. Uniform failures mean the harness, not the artefacts.

**Move.** Before the first run on a new tree, ask what the root resolves. Run from the widest root the
citations need, then attribute each error line to the file header above it.

## Rule 2 — When two gates disagree, the rule is wrong, not the artefact

**Statement.** Two checkers demanding incompatible edits to one artefact means ownership of its fields
was never written down. The fix is the ownership sentence, then both gates.

**Mechanism.** Each gate was written against a different property of the artefact: one protects a claim,
the other protects a pointer. Neither is wrong in isolation, and no edit satisfies both while the
boundary between them is undefined.

**Symptom.** An exception clause added so one checker goes quiet, and the number of such clauses grows
with each round. Each clause is evidence that a field has two owners.

**Move.** Write one sentence per gate: which field it owns, and what it must not touch. Then change the
rule and, if needed, the comparison. Never edit the artefact to satisfy the gate whose author is easier
to guess — the guess is what the clause records.

## Rule 3 — "The tool is not available" is a red gate, not a pass

**Statement.** A gate that could not run has not passed. Either provide an entry point that runs in this
environment, or record the gate as not executed and the artefact as unverified through it.

**Mechanism.** Environment failures arrive in the voice of environment facts ("no chromium here"),
which is exactly the voice of a legitimate constraint. Green gates from other checks then cover the gap
by adjacency: three greens and one abstention read as a pass.

**Symptom.** The words "lint only", "not rendered", "unavailable in this environment" in a report, next
to an artefact that was accepted. Or a tool failing for everyone in one environment with a message that
reads as a missing capability.

**Move.** Ship a script that carries the environment's requirement (flags, config, wrapper), and make
"could not run" fail loudly: exit non-zero, name the missing capability, and state which artefact is
therefore unverified.

## Rule 4 — A derived list is a hint; the source it was derived from is the record

**Statement.** Any list a script produces from a larger fact (diff, log, audit output) is a hint. The
brief names the command that produces the larger fact, and requires the discrepancy to be reported.

**Mechanism.** The list is derived from a range, and a range can be short. The consumer cannot tell a
short list from a quiet window, so it concludes nothing happened — the cheapest possible failure, since
it produces no error at all.

**Symptom.** A worker reporting "unchanged" for an item whose stated count is non-zero, or a brief whose
only reading instruction is the list itself.

**Move.** One line in the brief: the hint, then the authoritative command, then "if they disagree,
report and work from the source". Put the command first in the read order, not the list.

## Rule 5 — A deletion sweeps every tracked file type, and protects what other tools read

**Statement.** Before deleting a path, sweep all tracked files for references, and classify the hits:
links to rewrite, tools that read a file inside the path, transcripts to annotate. A file any tool reads
on every run is a production input and does not belong inside the thing being deleted.

**Mechanism.** "Reference" is defined by the consumer, not by the extension. A sweep scoped to the file
type being deleted finds the readers that look like the deleted thing and misses the readers that do not.

**Symptom.** After a deletion, an unrelated checker crashes on a missing file, and the error points at
the checker rather than at the deletion.

**Move.** Sweep without an extension filter, move consumed files to a stable home beside their consumer
before the deletion, rerun the consumer and record its output, then delete.

## Before trusting a green run

1. Which gates ran, and which could not run in this environment?
2. For each gate that ran: what would have made it red, and was that condition covered by a case that
   actually executed?
3. Does any gate's verdict depend on a list that a script derived? If so, where is the source, and do the
   two agree?
4. Do any two gates constrain the same field? If so, where is the ownership sentence?
5. If something is being deleted, what reads it that does not look like a reader?

A run that cannot answer all five is a run with an unknown number of unverified artefacts.
