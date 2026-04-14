# Knowledge Pipeline

How knowledge gets into this repository, how it's validated, and how it flows
into the skill.

## Roles

- **Maintainer** (human): owns the repo, approves drafts, makes final calls on
  disagreements, and enforces the license compliance rules.
- **Drafter** (typically Claude or another AI assistant acting on behalf of
  the maintainer): reads sources, drafts knowledge notes, runs self-checks.

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
