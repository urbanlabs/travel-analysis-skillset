# `_unverified/` — Pre-Pipeline Legacy Content

Files in this directory are **not part of the approved knowledge base**.

They exist to preserve useful starting material that pre-dates the knowledge
pipeline (`docs/knowledge-pipeline.md`). The content here was written from
Claude's general training rather than from authoritative sources, so it
cannot be cited or used by the skill.

## Intended flow

1. A topic from `knowledge/BACKLOG.md` is selected for ingestion.
2. A drafter reads the relevant section of `_unverified/*.md` as a *starting point*.
3. Claims are verified against tier-1/2 sources in `knowledge/sources.yaml`.
4. A properly-sourced topic note is created in `knowledge/topics/<area>/`.
5. Once the new note is `status: approved`, the corresponding section of the
   legacy file should be struck through (or removed) to avoid re-using
   stale material.

## Rules

- Nothing in `_unverified/` is loaded by `skills/fundamentals/SKILL.md`.
- `scripts/check-licenses.py` does not scan this directory — it intentionally
  bypasses the pipeline's rigor because the content is pre-pipeline.
- Do **not** add new content here. New knowledge goes through the pipeline.
- When the last legacy file is fully absorbed into sourced topic notes, this
  directory can be removed.
