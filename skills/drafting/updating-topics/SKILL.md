---
name: updating-topics
description: Drafter workflow — refresh an existing approved topic note against current sources, add new sources, resolve drift
trigger: When the user asks to update a knowledge note, refresh a topic, re-verify sources, or reconcile a topic against new information.
---

You are a drafter contributing to the travel-analysis-skillset knowledge base.
Your job: take ONE existing approved topic note and produce an updated draft
that reflects current sources, with drift and new disagreements surfaced for
the maintainer's review.

**You never skip steps, never mark a note `approved`, and never fabricate
citations. When sources have changed or disagree, you stop and document it.**

## When to use this skill vs. `ingesting-topics`

- **Ingesting** = the topic has no approved note yet.
- **Updating** = the topic already has `status: approved` in
  `knowledge/topics/` and you want to refresh it.

## Procedure

### 1. Identify and load the topic

- Read the existing note at `knowledge/topics/<area>/<id>.md`.
- Note its current `last_verified` date, cited `sources`, and list of
  Key Claims.
- Note the parent/subtopics structure — respect it unless the update
  reveals structural problems.

### 2. Re-read the cited sources

For each source currently cited:

- Check whether the source has been updated (new edition, revised page, etc.)
  since the note's `last_verified` date.
- Look up the `storage_policy` in `knowledge/sources.yaml`.
- Re-read the relevant sections and capture what's changed.
- Update `last_fetched` in `knowledge/sources.yaml` for each re-read source.

### 3. Search for additional sources

Same as in `ingesting-topics`:

1. References cited by primary sources (may point to new material).
2. Web search for new peer-reviewed papers since the note's `last_verified`.
3. Cross-references in `knowledge/sources.yaml`.
4. New community resources or guidance documents.

### 4. STOP — present new sources to user

**Do NOT silently add sources.** For each source found beyond what's in
`sources.yaml`, present:

- Title, authors, year
- URL or DOI
- What it adds to the topic, especially if it challenges or refines an
  existing claim
- Your credibility assessment

**Ask the user to classify each one:**

| Classification | Action |
|----------------|--------|
| **Trusted and valid** | Add to `sources.yaml` with appropriate `tier` and `storage_policy`; use to strengthen or revise claims. |
| **Not useful** | Skip. |
| **Potentially useful but not gold standard** (tier-3) | Add with `tier: 3`. Only cite when corroborated by a tier-1/2 source. |

Wait for user response before proceeding.

### 5. Diff the note against current sources

Prepare an update diff that addresses:

- **Claims that have changed**: the source now says something different.
  Revise the claim and note the change in your handoff summary.
- **Claims that have been corroborated or weakened**: new sources support
  or challenge what was previously stated. Flag for maintainer attention.
- **New claims worth adding**: the refreshed sources support additional
  points worth including.
- **Stale claims**: the supporting source has been superseded or retracted.
  Remove or mark for removal.
- **New disagreements**: sources now conflict where they didn't before.
  Create or update a file in `knowledge/disagreements/`.

### 6. Apply the diff

- Change the note's `status` from `approved` to `in-review` (or `draft`
  if the changes are substantial).
- Update `last_verified` to today's date.
- Update the `sources` frontmatter list if sources were added or removed.
- Apply the changes to Summary, Key Claims, Persona Notes, Disagreements,
  and References sections.
- If structural problems emerged (note too long, a subtopic should be
  split off), stop and escalate to the maintainer before restructuring.

### 7. Self-check (evidence, not claims)

Paste the actual output of each check into your handoff message.

- [ ] `python3 scripts/check-licenses.py` passes.
- [ ] Every factual claim has a current `sources.yaml` id cited.
- [ ] No verbatim text >15 words from `cite-only` or `cite-and-summarize`
      sources (including in newly-added content).
- [ ] Changed or removed claims are explicitly called out in the handoff.
- [ ] New disagreements are documented in `knowledge/disagreements/`.
- [ ] `last_verified` is today's date.

### 8. Hand off for human review

Write a handoff summary containing:

- Topic updated and its id
- Diff summary: what changed, what was added, what was removed, why
- New sources added and their user-chosen tier (step 4 outcome)
- New disagreements surfaced
- Self-check output
- Recommendation: can the maintainer re-approve, or does the update
  warrant structural discussion?

**Do NOT flip `status` → `approved` yourself.**

## Guardrails

- Never fabricate sources, citations, or parameter values.
- Never silently remove or change a claim — each change must be named
  in the handoff with the source that prompted it.
- Never skip step 4 (source classification).
- Never restructure hierarchy (parent/subtopics) on your own authority.
  If the structure needs to change, escalate to the maintainer.
- Never mark a note `approved`.

## Related

- `docs/knowledge-pipeline.md` — the full pipeline this skill implements
- `skills/drafting/ingesting-topics/SKILL.md` — sibling skill for new topics
