"""
Tests for scripts/check-licenses.py.

These tests use a temporary repo layout so the script can be exercised in
isolation from the actual knowledge/ content.

Run from repo root:
    python -m pytest scripts/tests -q
"""

from __future__ import annotations

import importlib.util
import sys
import textwrap
from pathlib import Path

import pytest

# Load check-licenses.py as a module even though it has a hyphen in the name.
SCRIPT_PATH = Path(__file__).resolve().parents[1] / "check-licenses.py"
spec = importlib.util.spec_from_file_location("check_licenses", SCRIPT_PATH)
check_licenses = importlib.util.module_from_spec(spec)
sys.modules["check_licenses"] = check_licenses
spec.loader.exec_module(check_licenses)


@pytest.fixture
def fake_repo(tmp_path, monkeypatch):
    """Build a minimal repo layout and point the script at it."""
    (tmp_path / "knowledge" / "topics" / "model-structures").mkdir(parents=True)
    (tmp_path / "knowledge" / "disagreements").mkdir(parents=True)
    (tmp_path / "knowledge" / "_templates").mkdir(parents=True)

    sources_yaml = tmp_path / "knowledge" / "sources.yaml"
    sources_yaml.write_text(textwrap.dedent("""\
        sources:
          - id: open-source
            title: Open Source
            license: cc-by-4.0
            storage_policy: redistribute-ok
          - id: restricted-source
            title: Restricted Source
            license: all-rights-reserved
            storage_policy: cite-only
          - id: gov-source
            title: Government Source
            license: us-gov-public-domain
            storage_policy: paraphrase-and-cite
    """))

    monkeypatch.setattr(check_licenses, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(check_licenses, "SOURCES_FILE", sources_yaml)
    monkeypatch.setattr(
        check_licenses, "TOPICS_DIR", tmp_path / "knowledge" / "topics"
    )
    monkeypatch.setattr(
        check_licenses,
        "DISAGREEMENTS_DIR",
        tmp_path / "knowledge" / "disagreements",
    )
    return tmp_path


def _write_note(repo: Path, relative: str, frontmatter: str, body: str) -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = textwrap.dedent(frontmatter).strip()
    path.write_text(f"---\n{fm}\n---\n{body}")


# --- Negative cases: script must reject these ---

def test_missing_frontmatter_fields_fails(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/bad.md",
        """
        title: Bad Note
        id: bad
        """,
        "Body with no sources.",
    )
    assert check_licenses.main() == 1


def test_unknown_source_id_fails(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/bad.md",
        """
        title: Bad Note
        id: bad
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [does-not-exist]
        last_verified: 2026-04-14
        status: approved
        """,
        "Body cites a non-existent source.",
    )
    assert check_licenses.main() == 1


def test_long_quote_from_restricted_source_fails(fake_repo):
    # 20-word quoted passage while citing a cite-only source
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/bad.md",
        """
        title: Bad Note
        id: bad
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [restricted-source]
        last_verified: 2026-04-14
        status: approved
        """,
        'The report states: "This is a long quotation copied verbatim from a '
        'restricted source that exceeds the fair use word count threshold."',
    )
    assert check_licenses.main() == 1


def test_unknown_parent_fails(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/orphan.md",
        """
        title: Orphan Note
        id: orphan
        topic_area: model-structures
        parent: does-not-exist
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Body text.",
    )
    assert check_licenses.main() == 1


def test_parent_in_different_area_fails(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/parent-topic.md",
        """
        title: Parent Topic
        id: parent-topic
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Parent body.",
    )
    _write_note(
        fake_repo,
        "knowledge/topics/surveys/child.md",
        """
        title: Child Note
        id: child
        topic_area: surveys
        parent: parent-topic
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Child body.",
    )
    assert check_licenses.main() == 1


def test_invalid_topic_area_fails(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/bad-area.md",
        """
        title: Bad Area
        id: bad-area
        topic_area: made-up-area
        parent: null
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Body.",
    )
    assert check_licenses.main() == 1


# --- Positive cases: script must accept these ---

def test_well_formed_note_passes(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/good.md",
        """
        title: Good Note
        id: good
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Body paraphrases the government source [gov-source] without long quotes.",
    )
    assert check_licenses.main() == 0


def test_parent_child_pair_passes(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/parent.md",
        """
        title: Parent
        id: parent-id
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Parent body.",
    )
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/child.md",
        """
        title: Child
        id: child-id
        topic_area: model-structures
        parent: parent-id
        personas: [analyst]
        sources: [gov-source]
        last_verified: 2026-04-14
        status: approved
        """,
        "Child body.",
    )
    assert check_licenses.main() == 0


def test_long_quote_allowed_for_redistribute_ok_source(fake_repo):
    _write_note(
        fake_repo,
        "knowledge/topics/model-structures/good.md",
        """
        title: Good Note
        id: good
        topic_area: model-structures
        parent: null
        personas: [analyst]
        sources: [open-source]
        last_verified: 2026-04-14
        status: approved
        """,
        'A long quote from the open CC-BY source: "This long passage of text '
        'is permitted because the source allows redistribution under CC-BY."',
    )
    assert check_licenses.main() == 0


def test_empty_knowledge_dir_passes(fake_repo):
    # No notes at all — script should succeed
    assert check_licenses.main() == 0


def test_templates_are_skipped(fake_repo):
    # Templates have placeholder frontmatter and should be ignored
    _write_note(
        fake_repo,
        "knowledge/_templates/topic-note.md",
        """
        title: <Topic Title>
        id: <kebab-case-id>
        """,
        "Template body with placeholders.",
    )
    # Template is in _templates/, not topics/ — so it won't be scanned.
    # But a template placed in topics/ by mistake would fail; that's desired.
    assert check_licenses.main() == 0
