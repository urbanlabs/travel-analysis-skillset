---
name: ingesting-topics
description: Drafter workflow — take a topic from BACKLOG.md through to a properly-sourced draft note ready for human review
trigger: When the user asks to ingest a topic, draft a new knowledge note, work through an item from knowledge/BACKLOG.md, or bring a topic into the knowledge base.
---

You are a drafter contributing to the travel-analysis-skillset knowledge base.
Your job: take ONE topic from `knowledge/BACKLOG.md` and produce a
properly-sourced draft topic note that passes all checks and is ready for
human review.

**You never skip steps, never mark a note `approved`, and never fabricate
citations. When sources disagree, you stop and document the disagreement.**

## Procedure

### 1. Select and scope the topic

- Read `knowledge/BACKLOG.md` and confirm the topic with the user.
- Note the backlog entry's `Id`, `Parent`, designated `Source`, and `Personas`.
- Confirm the topic doesn't already have an approved note in
  `knowledge/topics/`. If one exists, stop and suggest the `updating-topics`
  skill instead.

### 2. Read the designated sources

For each source listed in the backlog entry:

- Look up its `storage_policy` in `knowledge/sources.yaml`.
- Respect the policy (`cite-only` → no verbatim text; `cite-and-summarize`
  → paraphrase only; `paraphrase-and-cite` → quote sparingly; etc.).
- Fetch the source content via WebFetch or local reading as appropriate.
- Note the specific sections or URLs that inform the topic.

### 3. Search for additional relevant sources

Before drafting, expand the source net:

1. **Check references cited BY the primary source**: what does the tfresource
   page or FHWA manual point to? Note promising references.
2. **Web search** for peer-reviewed papers on the topic (prefer last 5 years).
3. **Check `knowledge/sources.yaml`** for existing entries that mention the
   topic — they may have useful treatment not captured in the primary source.
4. **Check `knowledge/_unverified/legacy-skill-content.md`** for any starting
   draft material on the topic. Treat as a prompt, never as a citation.

### 4. STOP — present additional sources to user

**Do NOT silently ingest new sources.** For each additional source found
(beyond what's already in `sources.yaml`), present to the user:

- Title, authors, year
- URL or DOI
- One-line description of what it adds to the topic
- Your assessment of its credibility (affiliation, venue, recency)

**Ask the user to classify each one:**

| Classification | Action |
|----------------|--------|
| **Trusted and valid** (tier-1 or tier-2) | Add to `sources.yaml` with appropriate `tier` and `storage_policy`; cite freely in the draft. |
| **Not useful** | Skip. Do not add to `sources.yaml`. |
| **Potentially useful but not gold standard** (tier-3) | Add to `sources.yaml` with `tier: 3`. Only cite when corroborated by a tier-1/2 source, never alone. |

Wait for user response before proceeding. If the user wants more info on a
source, fetch it and summarize, then re-present.

### 5. Draft the topic note

- Copy `knowledge/_templates/topic-note.md` into the correct location per
  the hierarchy rules in `docs/knowledge-pipeline.md`.
  - `topic_area` matches the BACKLOG section.
  - `parent` matches the backlog entry's Parent column.
  - File lives in `knowledge/topics/<area>/<id>.md`, or under a subdirectory
    if its parent has 4+ children (e.g., `aggregate-demand/trip-distribution.md`).
- Fill in all required frontmatter: `title`, `id`, `topic_area`, `parent`,
  `personas`, `sources`, `last_verified` (today), `confidence`, `status: draft`.
- Write the Summary (one paragraph, paraphrased — no verbatim restricted text).
- Write Key Claims with citations for every factual assertion. Prefer
  tier-1 sources. Flag claims resting on a single source.
- Write Persona subsections for each persona in the frontmatter.
- Keep the note focused. If it exceeds ~200 lines, split it — create child
  topic notes and leave the parent with a concise summary + `subtopics` list.

### 6. Detect and document disagreements

If sources conflict on any claim:

- Create (or update) a file in `knowledge/disagreements/` using
  `knowledge/_templates/disagreement-note.md`.
- Link to it from the topic note's "Disagreements" section.
- Only include positions held by tier-1 or tier-2 sources. Exclude tier-3
  unless corroborated.

### 7. Self-check (evidence, not claims)

Paste the actual output of each check into your handoff message. Do not
say "I checked X" — show it.

- [ ] `python3 scripts/check-licenses.py` passes. Paste output.
- [ ] Every factual claim has a `sources.yaml` id cited. Confirm by
      scanning the Key Claims section.
- [ ] No verbatim text >15 words from `cite-only` or `cite-and-summarize`
      sources. Confirm by search or compare.
- [ ] Parameter ranges, thresholds, and numeric claims are each backed by
      a tier-1 citation.
- [ ] Any contradictions with other approved notes are surfaced or
      escalated to a disagreement note.
- [ ] `last_verified` is today's date.
- [ ] If new sources were added, `sources.yaml` reflects the user's
      classification decisions from step 4.

### 8. Hand off for human review

Write a handoff summary containing:

- Topic ingested and its id
- Path to the new draft note
- List of sources used, with any new additions and their user-chosen tier
- Disagreements surfaced (if any)
- Self-check output (step 7)
- Known gaps or open questions

**Do NOT flip `status: draft` → `status: approved`.** That's the
maintainer's call after review.

## Guardrails

- Never fabricate a source, citation, or parameter value.
- Never copy verbatim from a `cite-only` source.
- Never skip step 4 (source classification). Even "obviously good" sources
  need the user's explicit call.
- Never treat `knowledge/_unverified/` content as citable.
- Never mark a note `approved` on your own authority.

## Related

- `docs/knowledge-pipeline.md` — the full pipeline this skill implements
- `docs/LICENSE-COMPLIANCE.md` — storage_policy definitions
- `skills/drafting/updating-topics/SKILL.md` — sibling skill for refreshing
  existing approved notes
