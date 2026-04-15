---
title: <Topic Title>
id: <kebab-case-id>
topic_area: <terminology|model-structures|networks|surveys|validation|forecasting|extended>
parent: null               # parent topic id, or null for top-level in the area
subtopics: []              # optional list of direct-child topic ids (can be auto-generated)
personas: [analyst, developer, researcher, reviewer]
sources: []                # list of source IDs from knowledge/sources.yaml
last_verified: YYYY-MM-DD
confidence: medium         # low | medium | high
status: draft              # draft | in-review | approved
---

## Summary

One-paragraph plain-language explanation (2-4 sentences). Do not quote from
restricted sources here — synthesize in your own words.

## Key Claims

Each claim below MUST cite at least one source by its `sources.yaml` id.
Prefer tier-1 sources. Flag any claim that rests on a single source.

- **Claim**: Brief statement of the claim.
  - Source: [source-id](URL or section reference)
  - Confidence: high | medium | low

- **Claim**: ...
  - Sources: source-id §X.Y; another-source-id p.NN
  - Confidence: ...

## Persona Notes

Include a short subsection for each persona listed in the frontmatter.
Omit subsections for personas this topic does not serve.

### For Analysts
Practical guidance, procedures, parameter ranges.

### For Developers
Implementation considerations, algorithms, software specifics.

### For Researchers
Methodological nuance, estimation considerations, literature pointers.

### For Reviewers
Reasonableness benchmarks, red flags, validation checks.

## Subtopics

If this topic has child topics (listed in `subtopics` frontmatter), link to
them here with brief descriptions. Keep the parent note short; detail lives
in the subtopics.

- [<Subtopic title>](./path/to/subtopic.md) — one-line description

## Disagreements

If practitioners or sources disagree on aspects of this topic, link to the
relevant file in `knowledge/disagreements/`. Example:

See: [../../disagreements/destination-choice-vs-gravity.md](../../disagreements/destination-choice-vs-gravity.md)

If there are no known disagreements, write: "No significant disagreements
identified among tier-1/2 sources as of <last_verified>."

## References

Human-readable list for this topic. Generated bibliography lives in
`knowledge/REFERENCES.md` — this section is a quick-reference subset.

- [source-id] Publisher. *Title*. Year. URL or DOI.
