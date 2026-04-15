# Knowledge Pipeline

How knowledge gets into this repository, how it's validated, and how it flows
into the skill.

## Roles

- **Maintainer** (human): owns the repo, approves drafts, makes final calls on
  disagreements, and enforces the license compliance rules.
- **Drafter** (typically Claude or another AI assistant acting on behalf of
  the maintainer): reads sources, drafts knowledge notes, runs self-checks.

## Skill vs. Knowledge — Division of Responsibility

Two different kinds of files, two different jobs:

| | `skills/fundamentals/SKILL.md` | `knowledge/topics/**/*.md` |
|---|---|---|
| **Purpose** | Tells Claude *how* to help | Tells Claude *what* is true |
| **Contents** | Role detection, topic routing, guardrails, response protocol | Concepts, claims with citations, parameter values, benchmarks |
| **Size** | Lean (tens of lines) — loaded every time the skill triggers | As long as the topic needs — loaded on demand |
| **Sourced?** | No — instructions, not claims | Yes — every claim cites `sources.yaml` |
| **Changes** | Rarely | Grows and refines as topics are ingested |

Embedding domain knowledge directly in `SKILL.md` would balloon the context
footprint and bypass source-verification. The skill should be a dispatcher
that reads the right knowledge note on demand.

## Storage Model

The pipeline produces three kinds of artifacts, all version-controlled:

1. **Source manifest** (`knowledge/sources.yaml`) — the single index of every
   source used anywhere in the repo, with licensing and storage rules.
2. **Topic notes** (`knowledge/topics/**/*.md`) — one note per concept, with
   structured frontmatter and fully-cited claims. These are the payload the
   skill references.
3. **Disagreement notes** (`knowledge/disagreements/*.md`) — standalone files
   documenting conflicts between credible sources and how the skill should
   handle them.

All three use templates in `knowledge/_templates/`.

A fourth, transitional directory — `knowledge/_unverified/` — holds
pre-pipeline content that hasn't been sourced yet. It is NOT part of the
approved knowledge base; see its README for rules. Content there is a
starting point for drafters, not a citable reference.

## End-to-End Workflow

### 1. Pick a topic

Choose from `knowledge/BACKLOG.md`. Topics are prioritized by PRD phase and
persona value.

### 2. Identify sources

Consult `knowledge/sources.yaml` for existing tier-1 and tier-2 sources
relevant to the topic. If a needed source is not in the manifest:

- Evaluate its license and set a `storage_policy` (see
  [LICENSE-COMPLIANCE.md](LICENSE-COMPLIANCE.md)).
- Add a new entry using `_templates/source-entry.yaml`.

### 3. Read sources

Respect each source's `storage_policy`:

- `redistribute-ok` / `paraphrase-and-cite`: read fully, quote and paraphrase freely.
- `cite-and-summarize`: read via WebFetch or local browsing, do not save raw
  source text to the repo.
- `cite-only`: read externally, record the citation only. Never save text.
- `quote-fair-use`: short quotations (<15 words) with attribution only.

### 4. Draft the topic note

Copy `_templates/topic-note.md` into the appropriate
`knowledge/topics/<area>/<id>.md`. Fill in frontmatter with
`status: draft`. Every factual claim must cite at least one source by id.

### 5. Detect disagreements

If sources conflict on any claim in the draft:

- Create (or update) a file in `knowledge/disagreements/` using
  `_templates/disagreement-note.md`.
- Link to it from the topic note's "Disagreements" section.
- Include only positions held by tier-1 or tier-2 sources. Tier-3 or
  uncredentialed opinions stay out unless corroborated by tier-1/2.

### 6. Self-check (evidence, not claims)

Before asking for human review, the drafter runs the checklist below and
pastes the verifying evidence into the review request. "I checked X" is not
enough — include the command output, file diff, or search result that proves
the check passed. This reflects the "evidence before assertions" principle
from `superpowers:verification-before-completion`.

- [ ] Every factual claim has a `sources.yaml` id cited.
      *Evidence*: structural review of the note body.
- [ ] No verbatim text from `cite-only` or `cite-and-summarize` sources beyond
      short fair-use quotation (<15 words).
      *Evidence*: side-by-side compare or search for distinctive source phrases.
- [ ] Parameter ranges, thresholds, and numeric claims verified against at
      least one tier-1 source.
      *Evidence*: the source id and section cited for each number.
- [ ] Any contradictions with other `approved` notes are surfaced (either
      reconciled or escalated to a disagreement note).
- [ ] Persona subsections present for all personas listed in frontmatter.
- [ ] `last_verified` set to today's date.
- [ ] `scripts/check-licenses.py` passes on the new/changed files.
      *Evidence*: paste the exit-zero output, e.g.
      `OK: checked 3 topic note(s), 0 disagreement note(s), 7 source(s).`

### 7. Human review

The maintainer reviews the draft. Possible outcomes:

- **Approve**: flip `status: draft` → `status: approved`, commit.
- **Request changes**: keep `status: draft`, add notes in the PR/issue,
  drafter revises.
- **Escalate**: create or expand a disagreement note; topic note may move
  to `status: in-review` pending resolution.

### 8. Commit

Only `status: approved` notes are referenced by `skills/fundamentals/SKILL.md`.
Commits should include:

- The new/changed topic note
- Any new `sources.yaml` entries
- Any new/updated disagreement notes
- Regenerated `knowledge/REFERENCES.md` (if bibliography script is run)

### 9. Update the skill (periodic)

After a batch of topic notes reaches `approved`, update `SKILL.md` to
reference them. The skill file itself should NOT duplicate knowledge —
it should point to topic notes.

## Handling Re-verification

Topic notes have a `last_verified` date. When a source is updated or a
year passes, the maintainer may flip `status` back to `in-review` and have
a drafter re-verify against the current source.

## Adding New Personas or Topic Areas

New personas require a PRD update first. New topic areas can be added by
creating a new subdirectory under `knowledge/topics/` and updating
`BACKLOG.md`.

## Topic Hierarchy Rules

Topics nest. "Value of Time" is a sub-topic of "Utility Functions," which
is a sub-topic of "Econometric Choice Models." Nesting lets each note stay
small (bounded context footprint) while preserving the relationships
practitioners care about.

### Top-level areas

The top-level areas come from the PRD's "Skill Content Areas" table and
map 1:1 to subdirectories of `knowledge/topics/`:

- `terminology/` — Terminology and Basic Theories
- `model-structures/` — Travel Model Structures (and its subareas)
- `networks/` — Network Data and Structures
- `surveys/` — Surveys
- `validation/` — Validation & Calibration
- `forecasting/` — Forecasting
- `extended/` — Phase 3 extended topics (freight, land-use, AVs, equity, etc.)

Adding a new top-level area requires a PRD update.

### When to use a subdirectory vs. flat files

**Hybrid rule**: create a subdirectory inside a topic area when a topic has
4+ direct children. Otherwise keep files flat within the area.

Example — `model-structures/` uses subdirs for branches with many children:

```
knowledge/topics/model-structures/
  overview.md                       # umbrella note for the area
  strategic-planning.md             # flat — no children
  network-metric-models.md          # flat — few children
  direct-demand-models.md           # flat
  aggregate-demand/                 # subdir — 4-step has 4+ children
    overview.md                     # 4-step umbrella
    trip-generation.md
    trip-distribution.md
    mode-choice.md
    traffic-assignment.md
  microsimulated-demand/            # subdir — ABM has several components
    overview.md
    components.md
    ...
```

### Frontmatter rules for hierarchy

Every topic note declares its place in the hierarchy via frontmatter:

- `topic_area` — the top-level PRD area (required, one of the keys above)
- `parent` — the id of the parent topic, or `null` if this note is
  top-level within its area
- `subtopics` — optional list of direct child topic ids; used for
  generating "Subtopics" sections

A topic's `parent` must either be `null` or resolve to another approved
(or in-review) topic note in the same `topic_area`.

### Size guidance

If a topic note grows beyond ~200 lines, consider splitting. Signs it
should be split:

- Multiple distinct sub-concepts, each with its own set of claims
- Persona sections that effectively describe different topics
- A reader only needs one subsection to answer most questions

Split by creating child topic notes, moving the detail there, and leaving
the parent with a concise summary plus the `subtopics` list.

## Workflow: Maintaining the Backlog

`knowledge/BACKLOG.md` is the list of topics queued for ingestion. It is NOT
hand-written from intuition — that would make the skill's coverage reflect
the drafter's biases rather than the field's actual structure. The backlog
is derived from two sources, in this order:

### 1. The PRD outline (authoritative)

The "Skill Content Areas" table in `docs/PRD.md` defines the top-level topic
areas (Terminology, Model Structures, Networks, Surveys, Validation,
Forecasting) and which personas each area serves. These areas become the
**sections** of `BACKLOG.md`. Adding a new section requires a PRD update.

### 2. tfresource.org topics (enumeration)

For each PRD area, enumerate candidate topics by cross-referencing
[tfresource.org](https://tfresource.org)'s topic pages. Every topic in the
backlog should cite at least one authoritative source — usually a
tfresource page, an NCHRP/TCRP report, or an FHWA publication. Topics that
have no authoritative source are either:

- **Gaps** to be flagged (`source: gap` in the backlog) and turned into
  research tasks, OR
- **Out of scope** — drop them.

### Regeneration process

When you need to update or rebuild `BACKLOG.md`:

1. Read the Skill Content Areas table in `docs/PRD.md` — these are your
   top-level sections.
2. For each area, list the tfresource topic pages that fall under it
   (see <https://tfresource.org> navigation or its GitHub repo
   [tfresource/tfresource-website](https://github.com/tfresource/tfresource-website)).
3. For each candidate topic, record:
   - Topic title (as practitioners would ask about it)
   - Area (matches the PRD)
   - Primary source (source id from `sources.yaml`, or a specific tfresource page)
   - Priority (P1 = PRD Phase 1, P2 = Phase 2, P3 = Phase 3)
   - Personas served
4. Flag topics that have no tier-1 source as gaps.
5. Commit the regenerated `BACKLOG.md` with a note explaining why it changed.

### Adding a single topic to an existing backlog

If the PRD is stable and you just need to add one topic:

1. Confirm it fits an existing area; if not, stop and update the PRD first.
2. Identify the authoritative source (tier-1 or tier-2) that warrants its inclusion.
3. Append to the appropriate section of `BACKLOG.md` with source citation.
4. If there is no tier-1/2 source for the topic, it does not belong in the
   backlog — either treat it as a research task or exclude it.

## Appendix: Recommended Meta-Skills

The pipeline is tool-agnostic, but drafters working in Claude Code with the
[obra/superpowers](https://github.com/obra/superpowers) plugin installed can
use these named skills to execute each step more rigorously. None are
required; all replace informal habits with battle-tested ones.

| Pipeline step | Recommended skill |
|---------------|-------------------|
| 1. Pick a topic / scope a new area | `superpowers:brainstorming` |
| 4. Draft the topic note | `superpowers:writing-skills` (if also updating SKILL.md) |
| 6. Self-check | `superpowers:verification-before-completion` |
| Extending `check-licenses.py` | `superpowers:test-driven-development` |
| Reviewing a draft you disagree with | `superpowers:receiving-code-review` |
| Parallel ingestion of independent topics | `superpowers:dispatching-parallel-agents` |

When working in a session that has these skills available, invoke them by
name rather than re-implementing their checklists inline.

## What the Pipeline Does NOT Do (yet)

- No automated CI enforcement — `scripts/check-licenses.py` runs locally.
  GitHub Actions enforcement is a Phase 2 addition.
- No automated source refresh — all fetches are manual.
- No external contributor workflow — contribution guidelines for non-maintainers
  are a future expansion.
