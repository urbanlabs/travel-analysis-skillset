# License Compliance Rules

This repository aggregates references to many sources, some of which are under
restrictive licenses. These rules ensure we never store content outside its
permitted usage.

## Storage Policies

Every source in `knowledge/sources.yaml` has a `storage_policy` that governs
how its content may appear in this repository.

### `redistribute-ok`

Source content may be copied into this repo (including verbatim). Required:
attribution and any share-alike obligations.

**Use for**: Content under CC BY, CC BY-SA, CC0, BSD, MIT, or explicit
permission from the rights holder.

### `paraphrase-and-cite`

Source may be read, paraphrased, and quoted at normal scholarly lengths, with
clear attribution. Short direct quotations are allowed.

**Use for**: US government public-domain works (with contractor caveats),
open-access academic works without share-alike requirements.

### `quote-fair-use`

Short direct quotations (under ~15 words) with attribution are allowed.
Longer passages must be paraphrased.

**Use for**: Copyrighted sources where limited fair-use quotation is the norm
(standard scholarly practice for secondary discussion).

### `cite-and-summarize`

No verbatim content may be stored in the repo. Drafters may read the source
externally (via WebFetch or browser) and synthesize claims in their own words,
always citing the source. Very short quotations (<15 words) are discouraged
but permissible with attribution.

**Use for**: Sources where the license is unclear or restrictive but the
content is widely referenced in practice (e.g., tfresource.org).

### `cite-only`

The source may only be referenced by title/URL/section. No text from the
source may be stored. Summaries in our own words are permitted but should be
terse and clearly marked as our synthesis.

**Use for**: Paywalled works with explicit all-rights-reserved notices
(e.g., NCHRP reports).

## Per-Source Rules (Current Manifest)

| Source ID | License | Storage Policy |
|-----------|---------|----------------|
| `tfresource` | proprietary-unclear (NAS © 2020) | `cite-and-summarize` |
| `nchrp-716` | all-rights-reserved | `cite-only` |
| `fhwa-tmv-manual` | US-gov-public-domain | `paraphrase-and-cite` |
| `fta-new-starts` | US-gov-public-domain | `paraphrase-and-cite` |
| `nhts` | US-gov-public-domain | `paraphrase-and-cite` |
| `activitysim-docs` | BSD-3 code, docs unclear | `cite-and-summarize` |
| `tmip` | US-gov-public-domain | `paraphrase-and-cite` |

## Compliance Checks

### Automated (`scripts/check-licenses.py`)

Run before every commit that touches `knowledge/` or `skills/`. The script:

1. Parses frontmatter of every topic and disagreement note
2. Verifies every cited `sources` id exists in `sources.yaml`
3. For each citation, confirms the note's content complies with the source's
   `storage_policy`
4. Flags quoted strings >15 words from any source with policy stricter than
   `paraphrase-and-cite`
5. Warns on missing `last_verified`, `status`, or `personas` frontmatter

Exit non-zero on any violation.

### Manual Review

The maintainer spot-checks on approval:

- Does the paraphrase actually stay in our own words, or is it a close
  rewrite of the source?
- Are figures/tables copied from any source? If so, does the source permit it,
  and is attribution present?
- Do we have a permission record for any case that requires it?

## Adding a New Source

1. Evaluate the license. When in doubt, choose the more restrictive
   `storage_policy`.
2. Add the entry to `knowledge/sources.yaml` using
   `knowledge/_templates/source-entry.yaml`.
3. If the license is ambiguous and the source is important (tier-1 candidate),
   consider reaching out to the publisher for clarification and recording the
   response in the `notes` field.

## Recording Permissions

If explicit permission is obtained to exceed the default storage policy for a
source, record it in the `notes` field of the source entry with:

- Date of permission
- Who granted it
- Any conditions attached
- Where the correspondence is archived (e.g., a private email folder)

Do NOT paste the correspondence into the repo.

## Escalation

If there's any doubt about whether a planned use is compliant, default to the
more restrictive interpretation and ask the maintainer before committing.
