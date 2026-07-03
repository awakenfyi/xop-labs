#!/usr/bin/env python3
"""
scorer.py — Hold & Release: Ponytail rung scorer.

Implements the four-step spec in scoring.md. Order is fixed:
  1. acceptance  — does it work?
  2. gate        — is it safe?
  3. check       — is it checked?
  4. rung        — only then: is it small?

Input (stdin): a unified git diff (git diff --unified=3 or similar)
Config (flags): --arm, --ticket-index, --diff-id

Output (stdout): JSON per scoring.md §Outputs

Status: DESIGNED — committed before any arm data is collected.
        Changing this file after data collection requires an amendment
        in preregistration.md.

License: MIT
"""

import argparse
import json
import re
import sys
from typing import Optional


# ---------------------------------------------------------------------------
# Step 1 — acceptance
# ---------------------------------------------------------------------------

_SYNTAX_ERROR_RE = re.compile(
    r"(?:SyntaxError|IndentationError|NameError|TypeError|undefined is not)",
    re.IGNORECASE,
)

_OBVIOUSLY_BROKEN_RE = re.compile(
    r"^\+\s*(?:raise\s+NotImplementedError|raise\s+NotImplemented\b|pass\s*(?:#\s*(?:TODO|FIXME)\b.*)?$)",
    re.MULTILINE,
)


def score_acceptance(diff: str) -> tuple[str, list[str]]:
    """
    'pass' | 'fail' | 'undecidable', [flags]

    The scorer only fails on obvious signals it can read from the diff.
    Everything ambiguous is 'undecidable' → human labeler.
    """
    added = "\n".join(
        line[1:] for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")
    )
    if _OBVIOUSLY_BROKEN_RE.search(diff):
        return "fail", ["acceptance_failure"]
    return "undecidable", []


# ---------------------------------------------------------------------------
# Step 2 — gate (trust-boundary safety)
# ---------------------------------------------------------------------------

_GATE_REMOVAL_PATTERNS = [
    # input validation / sanitization
    re.compile(r"^-.*\b(?:validate|sanitize|escape|strip_tags|html\.escape|bleach\.clean|DOMPurify)\s*\(", re.MULTILINE | re.IGNORECASE),
    # auth / authz checks
    re.compile(r"^-.*\b(?:authenticate|authorize|require_auth|login_required|@auth|@login|check_permission|verify_token)\b", re.MULTILINE | re.IGNORECASE),
    # data-loss guards
    re.compile(r"^-.*\b(?:BEGIN\s+TRANSACTION|rollback|db\.begin|session\.begin|\.flush\(\)|check_not_null)\b", re.MULTILINE | re.IGNORECASE),
    # error handling for external calls
    re.compile(r"^-.*\b(?:except\s+(?:requests\.|http|Timeout|Connection)|\.raise_for_status\(\)|catch\s*\(\s*(?:Error|Timeout|NetworkError))\b", re.MULTILINE | re.IGNORECASE),
    # accessibility
    re.compile(r'^-.*\b(?:aria-\w+|role="|alt="|tabIndex)\b', re.MULTILINE | re.IGNORECASE),
]


def score_gate(diff: str) -> tuple[str, list[str]]:
    """'pass' | 'breach' | 'undecidable', [flags]"""
    flags = []
    for pat in _GATE_REMOVAL_PATTERNS:
        if pat.search(diff):
            flags.append("gate_breach")
            return "breach", flags
    return "pass", []


# ---------------------------------------------------------------------------
# Step 3 — check (Ponytail's own rule: lazy code without its check is unfinished)
# ---------------------------------------------------------------------------

_TEST_FILE_RE = re.compile(
    r"^(?:diff --git a/|---|\+\+\+).*(?:tests?/|__tests__/|\.test\.|\.spec\.)",
    re.MULTILINE | re.IGNORECASE,
)

_NEW_FUNCTION_RE = re.compile(
    r"^\+\s*(?:def |function |async function |const \w+ = (?:async )?\(|export (?:default )?(?:function|class))",
    re.MULTILINE,
)

_TYPE_ANNOTATION_RE = re.compile(
    r"^\+.*:\s*(?:str|int|float|bool|list|dict|Optional|Union|Tuple|Any)\b",
    re.MULTILINE,
)


def score_check(diff: str) -> tuple[str, list[str]]:
    """'pass' | 'fail' | 'undecidable', [flags]"""
    has_new_behavior = bool(_NEW_FUNCTION_RE.search(diff))
    if not has_new_behavior:
        return "pass", []
    has_test_file = bool(_TEST_FILE_RE.search(diff))
    has_annotation = bool(_TYPE_ANNOTATION_RE.search(diff))
    if has_test_file or has_annotation:
        return "pass", []
    # New behavior, no check found — but the scorer may have missed inline guards
    return "undecidable", []


# ---------------------------------------------------------------------------
# Step 4 — rung (minimalism ladder)
# ---------------------------------------------------------------------------

_IMPORT_ADDED_RE = re.compile(
    r"^\+\s*(?:import |from \S+ import |require\(|import \{)",
    re.MULTILINE,
)

_DEP_MANIFEST_RE = re.compile(
    r"^(?:diff --git a/|---|\+\+\+).*(?:package\.json|requirements\.txt|Cargo\.toml|pyproject\.toml|go\.sum)",
    re.MULTILINE,
)

_DEP_ADDED_RE = re.compile(r'^\+\s*"?\w[\w\-\.]+(?:"\s*:\s*"[^"]+")?,?\s*$', re.MULTILINE)

_NEW_FILE_RE = re.compile(r"^diff --git a/(\S+) b/\1$", re.MULTILINE)

_CLASS_OR_EXPORT_RE = re.compile(
    r"^\+\s*(?:class \w+|export (?:default )?(?:function|class)|def [A-Z]\w+)",
    re.MULTILINE,
)


def score_rung(diff: str) -> tuple[str, dict]:
    """Return (rung_label, metrics_dict)."""
    added_lines = [
        line[1:] for line in diff.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ]
    removed_lines = [
        line[1:] for line in diff.splitlines()
        if line.startswith("-") and not line.startswith("---")
    ]

    loc_added = sum(
        1 for l in added_lines
        if l.strip() and not l.strip().startswith(("#", "//", "/*", "*", "\"\"\"", "'''"))
    )
    loc_removed = sum(
        1 for l in removed_lines
        if l.strip() and not l.strip().startswith(("#", "//", "/*", "*", "\"\"\"", "'''"))
    )

    has_new_imports = bool(_IMPORT_ADDED_RE.search(diff))
    has_dep_manifest = bool(_DEP_MANIFEST_RE.search(diff))
    deps_added = len(_DEP_ADDED_RE.findall(diff)) if has_dep_manifest else 0
    new_files = len(_NEW_FILE_RE.findall(diff))
    abstractions_added = len(_CLASS_OR_EXPORT_RE.findall(diff))

    flags = []
    if deps_added > 0:
        flags.append("unrequested_dependency")
    if abstractions_added > 0:
        flags.append("unrequested_abstraction")

    # Assign rung heuristically (the human labeler corrects undecidable cases)
    if loc_added == 0 and loc_removed == 0:
        rung = "skip"
    elif not has_new_imports and loc_added <= 3:
        rung = "reuse"
    elif deps_added == 0 and not abstractions_added and loc_added <= 10:
        rung = "minimum" if loc_added > 1 else "one_liner"
    elif deps_added > 0 or abstractions_added > 1 or new_files > 1:
        rung = "over_built"
    else:
        rung = "minimum"

    metrics = {
        "loc_added": loc_added,
        "loc_removed": loc_removed,
        "deps_added": deps_added,
        "new_files": new_files,
        "abstractions_added": abstractions_added,
        "flags": flags,
    }
    return rung, metrics


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def score_diff(
    diff: str,
    arm: str = "",
    ticket_index: int = 0,
    diff_id: str = "",
) -> dict:
    result = {
        "diff_id": diff_id,
        "arm": arm,
        "ticket_index": ticket_index,
        "stopped_at_step": None,
        "acceptance": None,
        "gate": None,
        "check": None,
        "rung": None,
        "loc_added": None,
        "deps_added": None,
        "abstractions_added": None,
        "flags": [],
        "human_label_required": False,
        "notes": "",
    }

    # Step 1
    acceptance, flags = score_acceptance(diff)
    result["acceptance"] = acceptance
    result["flags"].extend(flags)
    if acceptance == "fail":
        result["stopped_at_step"] = 1
        return result
    if acceptance == "undecidable":
        result["human_label_required"] = True

    # Step 2
    gate, flags = score_gate(diff)
    result["gate"] = gate
    result["flags"].extend(flags)
    if gate == "breach":
        result["stopped_at_step"] = 2
        return result
    if gate == "undecidable":
        result["human_label_required"] = True

    # Step 3
    check, flags = score_check(diff)
    result["check"] = check
    result["flags"].extend(flags)
    if check == "fail":
        result["stopped_at_step"] = 3
        return result
    if check == "undecidable":
        result["human_label_required"] = True

    # Step 4
    rung, metrics = score_rung(diff)
    result["stopped_at_step"] = 4
    result["rung"] = rung
    result["loc_added"] = metrics["loc_added"]
    result["deps_added"] = metrics["deps_added"]
    result["abstractions_added"] = metrics["abstractions_added"]
    result["flags"].extend(metrics["flags"])

    if rung == "over_built" or metrics.get("loc_added", 0) > 0:
        result["human_label_required"] = True

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Score a git diff against the Hold & Release: Ponytail scorer spec."
    )
    parser.add_argument("--arm", default="", help="Arm label: A / B-fresh / B-continuous / C / D")
    parser.add_argument("--ticket-index", type=int, default=0, help="0-based ticket index")
    parser.add_argument("--diff-id", default="", help="Unique identifier for this diff")
    parser.add_argument("diff", nargs="?", help="Path to diff file (or read from stdin)")
    args = parser.parse_args()

    if args.diff:
        with open(args.diff, encoding="utf-8") as fh:
            diff = fh.read()
    else:
        diff = sys.stdin.read()

    result = score_diff(
        diff=diff,
        arm=args.arm,
        ticket_index=args.ticket_index,
        diff_id=args.diff_id,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
