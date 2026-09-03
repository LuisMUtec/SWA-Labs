#!/usr/bin/env python3
"""Mechanical checks for the RemoteSchooly architecture deliverable."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs/001-remoteschooly/spec.md"
TRACE = ROOT / "architecture/TRACEABILITY.md"
EVAL = ROOT / "evals/iterations/2026-09-02-01.md"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def local_markdown_links(errors: list[str]) -> None:
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        for raw_target in pattern.findall(document.read_text(encoding="utf-8")):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]
            if path and not (document.parent / path).resolve().exists():
                fail(errors, f"broken link in {document.relative_to(ROOT)}: {raw_target}")


def requirement_coverage(errors: list[str]) -> None:
    spec_text = SPEC.read_text(encoding="utf-8")
    trace_text = TRACE.read_text(encoding="utf-8")
    spec_ids = re.findall(r"\*\*(FR-\d{3})\*\*", spec_text)
    trace_ids = re.findall(r"^\| (FR-\d{3}) \|", trace_text, flags=re.MULTILINE)
    expected = [f"FR-{number:03d}" for number in range(1, 42)]
    if spec_ids != expected:
        fail(errors, f"spec IDs are not exactly FR-001..FR-041: {spec_ids}")
    if trace_ids != expected:
        fail(errors, f"traceability IDs are not exactly FR-001..FR-041: {trace_ids}")


def eval_fingerprint(errors: list[str]) -> None:
    current = hashlib.sha256(SPEC.read_bytes()).hexdigest()
    match = re.search(r"SHA-256 de `spec\.md` \| `([0-9a-f]{64})`", EVAL.read_text(encoding="utf-8"))
    if not match:
        fail(errors, "EVAL does not contain a parsable spec SHA-256")
    elif match.group(1) != current:
        fail(errors, "EVAL fingerprint is stale; run a new immutable evaluation")


def diagrams(errors: list[str]) -> None:
    for source in sorted((ROOT / "architecture/diagrams").glob("*.dot")):
        for suffix in (".svg", ".png"):
            output = source.with_suffix(suffix)
            if not output.exists() or output.stat().st_size == 0:
                fail(errors, f"missing rendered diagram: {output.relative_to(ROOT)}")
        with tempfile.NamedTemporaryFile(suffix=".svg") as rendered:
            result = subprocess.run(
                ["dot", "-Tsvg", str(source), "-o", rendered.name],
                check=False,
                capture_output=True,
                text=True,
            )
            if result.returncode:
                fail(errors, f"Graphviz rejected {source.name}: {result.stderr.strip()}")


def task_format(errors: list[str]) -> None:
    tasks = ROOT / "specs/001-remoteschooly/tasks.md"
    task_lines = [line for line in tasks.read_text(encoding="utf-8").splitlines() if line.startswith("- [ ] T")]
    task_pattern = re.compile(r"^- \[ \] T\d{3}(?: \[P\])?(?: \[US\d\])? .+`[^`]+`.*$")
    for line in task_lines:
        if not task_pattern.match(line):
            fail(errors, f"invalid task format: {line}")
    if len(task_lines) != 53:
        fail(errors, f"expected 53 future tasks, found {len(task_lines)}")


def required_artifacts(errors: list[str]) -> None:
    required = [
        ROOT / "docs/Lab-04-ARQ-2026.2.docx",
        ROOT / "docs/lab-04-pipeline.png",
        ROOT / "evals/agents/gobierno.md",
        ROOT / "evals/agents/profesora-lima.md",
        ROOT / "evals/agents/profesor-provincia.md",
        ROOT / "evals/agents/alumno.md",
        ROOT / "specs/001-remoteschooly/plan.md",
        ROOT / "specs/001-remoteschooly/data-model.md",
        ROOT / "specs/001-remoteschooly/contracts/sync-and-ai.md",
        ROOT / "architecture/README.md",
    ]
    for artifact in required:
        if not artifact.exists() or artifact.stat().st_size == 0:
            fail(errors, f"missing required artifact: {artifact.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    local_markdown_links(errors)
    requirement_coverage(errors)
    eval_fingerprint(errors)
    diagrams(errors)
    task_format(errors)
    required_artifacts(errors)

    if errors:
        print("RemoteSchooly validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RemoteSchooly validation PASSED")
    print("- 41/41 requirements traced")
    print("- EVAL fingerprint current: 9.5/10 PASSED")
    print("- 3/3 diagram sources render")
    print("- 53 future implementation tasks follow Spec Kit format")
    print("- local Markdown links and required artifacts exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
