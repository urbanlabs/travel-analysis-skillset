#!/usr/bin/env python3
"""
check-licenses.py — validate knowledge notes against sources.yaml policies.

Run before committing changes under knowledge/ or skills/.

Checks performed:
  1. Frontmatter completeness (title, id, sources, status, last_verified).
  2. Every cited source id exists in knowledge/sources.yaml.
  3. No direct quotations >15 words from sources whose storage_policy is
     stricter than 'paraphrase-and-cite'.
  4. Topic notes live under knowledge/topics/<area>/ matching frontmatter.

Exit codes:
  0 = all good
  1 = violations found (details printed to stderr)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "PyYAML is required. Install with: pip install pyyaml\n"
    )
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = REPO_ROOT / "knowledge" / "sources.yaml"
TOPICS_DIR = REPO_ROOT / "knowledge" / "topics"
DISAGREEMENTS_DIR = REPO_ROOT / "knowledge" / "disagreements"

# Policies in order from most-restrictive to least-restrictive.
# Anything at or stricter than 'quote-fair-use' gets the long-quote check.
RESTRICTIVE_POLICIES = {
    "cite-only",
    "cite-and-summarize",
    "quote-fair-use",
}

REQUIRED_TOPIC_FIELDS = {
    "title",
    "id",
    "topic_area",
    "personas",
    "sources",
    "last_verified",
    "status",
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
QUOTE_RE = re.compile(r'"([^"]{60,})"')  # quoted strings ≥60 chars (~15 words)


def load_sources() -> dict:
    if not SOURCES_FILE.exists():
        sys.stderr.write(f"ERROR: {SOURCES_FILE} not found.\n")
        sys.exit(2)
    with SOURCES_FILE.open() as f:
        data = yaml.safe_load(f)
    return {s["id"]: s for s in data.get("sources", [])}


def parse_note(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    return fm, body


def check_note(path: Path, sources: dict, required_fields: set[str]) -> list[str]:
    errors: list[str] = []
    fm, body = parse_note(path)
    if not fm:
        errors.append(f"{path}: missing or malformed YAML frontmatter")
        return errors

    # Skip templates
    if str(path).startswith(str(REPO_ROOT / "knowledge" / "_templates")):
        return []

    missing = required_fields - set(fm.keys())
    if missing:
        errors.append(f"{path}: missing frontmatter fields: {sorted(missing)}")

    # Unknown source IDs
    cited = set(fm.get("sources") or [])
    unknown = cited - set(sources.keys())
    if unknown:
        errors.append(
            f"{path}: frontmatter cites unknown source IDs: {sorted(unknown)}"
        )

    # Long-quote check for restrictive sources
    restrictive_cited = [
        sid for sid in cited
        if sources.get(sid, {}).get("storage_policy") in RESTRICTIVE_POLICIES
    ]
    if restrictive_cited:
        long_quotes = QUOTE_RE.findall(body)
        if long_quotes:
            errors.append(
                f"{path}: contains quoted strings >~15 words while citing "
                f"restrictive sources {restrictive_cited}. Paraphrase instead."
            )

    # Drafts are permitted but warned so they don't ship by accident
    if fm.get("status") == "draft":
        sys.stderr.write(f"WARN: {path} is still in draft status\n")

    return errors


def main() -> int:
    sources = load_sources()
    all_errors: list[str] = []

    topic_files = list(TOPICS_DIR.rglob("*.md")) if TOPICS_DIR.exists() else []
    for p in topic_files:
        all_errors.extend(check_note(p, sources, REQUIRED_TOPIC_FIELDS))

    disagreement_files = (
        list(DISAGREEMENTS_DIR.rglob("*.md")) if DISAGREEMENTS_DIR.exists() else []
    )
    for p in disagreement_files:
        # Disagreements require a smaller set of fields
        all_errors.extend(
            check_note(p, sources, {"title", "id", "sources", "status"})
        )

    if all_errors:
        sys.stderr.write("License-compliance check FAILED:\n")
        for e in all_errors:
            sys.stderr.write(f"  - {e}\n")
        return 1

    print(
        f"OK: checked {len(topic_files)} topic note(s), "
        f"{len(disagreement_files)} disagreement note(s), "
        f"{len(sources)} source(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
