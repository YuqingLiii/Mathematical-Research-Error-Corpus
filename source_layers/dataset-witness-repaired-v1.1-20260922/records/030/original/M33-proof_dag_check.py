"""Validate canonical per-node proof-DAG records.

The validator is deliberately structural.  It never promotes, demotes, or
recomputes a mathematical status.  Under the single-status model
(DAG_PROTOCOL section 1, lead merge 2026-08-08) statuses are hand-written per
node; the old min/max propagation is gone.  Two mechanisms replace it here:

- LINT-COMPLETION (hard error): a CERTIFIED*/PROVED AND-node with a
  load-bearing child below completion tier and no explicit relative-hypothesis
  display in its structured record fails validation.  A CERTIFIED*/PROVED OR node with
  children but no completion-tier child gets a warning (a direct whole-claim
  proof is legal there, so it cannot be a hard error).
- ``--diagnose chain-strength``: an on-demand, read-only bottom-up report of
  how solid the subtree under each node actually is (old-style min/max), for
  humans; it never changes exit status.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from proof_dag_v6 import (
    chain_strength_report as chain_strength_report_v6,
    validate_problem as validate_problem_v6,
    write_generated as write_generated_v6,
)


ROOT = Path(__file__).resolve().parents[1]
PROBLEM_DIRS = {
    "se": "research/se",
    "ksum": "research/ksum",
}
try:
    from private_problem_registry import EXTRA_PROBLEM_DIRS
except ImportError:
    EXTRA_PROBLEM_DIRS = {}
PROBLEM_DIRS.update(EXTRA_PROBLEM_DIRS)
LEGACY_REQUIRED_FIELDS = {
    "id",
    "node_file",
    "aliases",
    "kind",
    "role",
    "status",
    "status_source",
    "disposition",
    "parents",
    "children",
    "related",
}
LEGACY_OPTIONAL_FIELDS = {"composition", "lean", "lean_reason", "reason", "caveat"}
LEGACY_ALLOWED_FIELDS = LEGACY_REQUIRED_FIELDS | LEGACY_OPTIONAL_FIELDS
GROUPED_V4_SCHEMA = {
    "identity": {"id", "node_file", "aliases", "role"},
    "graph": {"kind", "children", "composition", "related"},
    "assessment": {"status", "source", "disposition", "reason", "caveat"},
    "formalization": {"lean", "reason"},
}
STRUCTURED_SCHEMA = {
    "identity": {"id", "aliases", "role"},
    "claim": {"statement"},
    "graph": {
        "kind", "children", "composition", "related", "rationale",
        "dependency_notes"
    },
    "assessment": {"status", "source", "reason", "caveat", "details"},
    "workflow": {"disposition"},
    "artifacts": {"work_record", "evidence", "reviews"},
    "formalization": {"lean", "absence_reason"},
    "open_obligations": None,
    "history": None,
    "notes": None,
}
COMPOSITION_FIELDS = {"arguments", "absence_reason"}
ARGUMENT_FIELDS = {
    "premises", "claim", "proof", "relative_hypotheses", "assessment",
    "workflow", "notes"
}
ARGUMENT_ASSESSMENT_FIELDS = {
    "status", "source", "reason", "caveat"
}
ARGUMENT_WORKFLOW_FIELDS = {"disposition"}
LEGACY_REQUIRED_SECTIONS = {
    "Claim",
    "Role in DAG",
    "Current status",
    "Dependencies",
    "Work record",
    "Evidence",
    "Adversarial reviews",
    "Open obligations",
    "Status history",
}
ALLOWED_KINDS = {None, "OR", "AND", "GOAL", "LEAF"}
STRICT_DECOMPOSITION_PROBLEMS = {"se", "ksum", "circdist"}
ALLOWED_ROLES = {
    "proof", "obstruction", "tool", "outcome", "history", "constraint", "related"
}
ALLOWED_STATUSES = {
    "PROVED",
    "NUMERICAL",
    "CERTIFIED*",
    "CONJECTURED",
    "OPEN",
    "REFUTED",
}
ALLOWED_DISPOSITIONS = {None, "DEAD", "PARKED"}
COMPLETION_TIERS = {"CERTIFIED*", "PROVED"}
LADDER_RANK = {"REFUTED": -1, "OPEN": 0, "CONJECTURED": 1, "NUMERICAL": 2, "CERTIFIED*": 3, "PROVED": 4}
RELATIVE_DISPLAY = re.compile(r"relative hypothes|rel-hypothesis", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def strip_comment(value: str) -> str:
    """Remove an unquoted YAML-style trailing comment."""
    out: list[str] = []
    in_quote = False
    for char in value:
        if char == '"':
            in_quote = not in_quote
        if char == "#" and not in_quote:
            break
        out.append(char)
    return "".join(out).strip()


def parse_scalar(value: str):
    value = strip_comment(value)
    if value == "null":
        return None
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith(("[", "{", '"')):
        return json.loads(value)
    return value


FRONT_KEY = re.compile(
    r'^(\s*)(?:"((?:\\.|[^"\\])*)"|([A-Za-z_][A-Za-z0-9_-]*)):\s*(.*)$'
)


def parse_front_matter(front: str) -> dict:
    """Parse the mapping-only YAML subset used by canonical node records.

    In addition to nested mappings and JSON-style inline lists, this accepts
    literal block scalars (``|``/``|-``).  It deliberately excludes YAML
    aliases, tags, and sequence-of-mapping syntax so the public node contract
    remains small and deterministic without an external YAML dependency.
    """
    root: dict = {}
    mappings: dict[int, dict] = {0: root}
    lines = front.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        match = FRONT_KEY.match(line)
        if not match:
            raise ValueError(f"invalid front matter line: {line!r}")
        indent = len(match.group(1))
        if indent % 2 or indent not in mappings:
            raise ValueError(f"invalid front matter indentation: {line!r}")
        quoted, plain, value = match.group(2), match.group(3), match.group(4)
        key = json.loads(f'"{quoted}"') if quoted is not None else plain
        parent = mappings[indent]
        for depth in [depth for depth in mappings if depth > indent]:
            del mappings[depth]
        scalar = value.strip()
        if scalar in {"|", "|-"}:
            block: list[str] = []
            j = i + 1
            block_indent = indent + 2
            while j < len(lines):
                candidate = lines[j]
                candidate_indent = len(candidate) - len(candidate.lstrip(" "))
                if candidate.strip() and candidate_indent <= indent:
                    break
                if candidate.strip() and candidate_indent < block_indent:
                    raise ValueError(
                        f"invalid block-scalar indentation: {candidate!r}"
                    )
                block.append(candidate[block_indent:] if len(candidate) >= block_indent else "")
                j += 1
            text = "\n".join(block)
            parent[key] = text if scalar == "|-" else text + "\n"
            i = j
            continue
        if scalar == "":
            child: dict = {}
            parent[key] = child
            mappings[indent + 2] = child
        else:
            parent[key] = parse_scalar(value)
        i += 1
    return root


def normalize_grouped(raw: dict) -> dict:
    identity = raw.get("identity", {})
    graph = raw.get("graph", {})
    assessment = raw.get("assessment", {})
    formalization = raw.get("formalization", {})
    return {
        "id": identity.get("id"),
        "node_file": identity.get("node_file"),
        "aliases": identity.get("aliases"),
        "role": identity.get("role"),
        "kind": graph.get("kind"),
        "children": graph.get("children"),
        "composition": graph.get("composition"),
        "related": graph.get("related"),
        "status": assessment.get("status"),
        "status_source": assessment.get("source"),
        "disposition": assessment.get("disposition"),
        "reason": assessment.get("reason"),
        "caveat": assessment.get("caveat"),
        "lean": formalization.get("lean"),
        "lean_reason": formalization.get("reason"),
        "__schema__": "grouped-v4",
        "__raw__": raw,
    }


def normalize_structured(raw: dict) -> dict:
    identity = raw.get("identity", {})
    claim = raw.get("claim", {})
    graph = raw.get("graph", {})
    assessment = raw.get("assessment", {})
    workflow = raw.get("workflow", {})
    formalization = raw.get("formalization", {})
    return {
        "id": identity.get("id"),
        "node_file": None,
        "aliases": identity.get("aliases"),
        "role": identity.get("role"),
        "claim": claim.get("statement"),
        "kind": graph.get("kind"),
        "children": graph.get("children"),
        "composition": graph.get("composition"),
        "related": graph.get("related"),
        "status": assessment.get("status"),
        "status_source": assessment.get("source"),
        "disposition": workflow.get("disposition"),
        "reason": assessment.get("reason"),
        "caveat": assessment.get("caveat"),
        "lean": formalization.get("lean"),
        "lean_reason": formalization.get("absence_reason"),
        "__schema__": "structured-v5",
        "__raw__": raw,
    }


def parse_node(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if path.suffix in {".yaml", ".yml"}:
        raw = parse_front_matter(text)
        return normalize_structured(raw), text
    if not text.startswith("---\n"):
        raise ValueError("missing opening front matter delimiter")
    try:
        front, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("missing closing front matter delimiter") from exc
    raw = parse_front_matter(front)
    if any(group in raw for group in GROUPED_V4_SCHEMA):
        metadata = normalize_grouped(raw)
    else:
        legacy_raw = raw.copy()
        metadata = raw.copy()
        metadata["__schema__"] = "legacy-flat"
        metadata["__raw__"] = legacy_raw
    return metadata, body


def schema_errors(metadata: dict, strict_grouped: bool) -> list[str]:
    """Return structural schema errors before mathematical graph validation."""
    errors: list[str] = []
    raw = metadata.get("__raw__", {})
    schema = metadata.get("__schema__")
    if schema != "structured-v5":
        if strict_grouped:
            return ["KSUM/SE nodes must use the pure-YAML structured-v5 schema"]
        missing = LEGACY_REQUIRED_FIELDS - raw.keys()
        unknown = raw.keys() - LEGACY_ALLOWED_FIELDS
        if missing:
            errors.append(f"missing {sorted(missing)}")
        if unknown:
            errors.append(f"fields outside the legacy schema {sorted(unknown)}")
        return errors

    top_missing = STRUCTURED_SCHEMA.keys() - raw.keys()
    top_unknown = raw.keys() - STRUCTURED_SCHEMA.keys()
    if top_missing:
        errors.append(f"missing top-level groups {sorted(top_missing)}")
    if top_unknown:
        errors.append(f"unknown top-level groups {sorted(top_unknown)}")
    for group, required in STRUCTURED_SCHEMA.items():
        block = raw.get(group)
        if not isinstance(block, dict):
            errors.append(f"{group} must be a mapping")
            continue
        if required is None:
            continue
        missing = required - block.keys()
        unknown = block.keys() - required
        if missing:
            errors.append(f"{group} missing {sorted(missing)}")
        if unknown:
            errors.append(f"{group} has unknown fields {sorted(unknown)}")
    statement = raw.get("claim", {}).get("statement") \
        if isinstance(raw.get("claim"), dict) else None
    if not isinstance(statement, str) or not statement.strip():
        errors.append("claim.statement must be a nonempty string")
    composition = raw.get("graph", {}).get("composition") if isinstance(raw.get("graph"), dict) else None
    if not isinstance(composition, dict):
        errors.append("graph.composition must be a mapping")
        return errors
    missing = COMPOSITION_FIELDS - composition.keys()
    unknown = composition.keys() - COMPOSITION_FIELDS
    if missing:
        errors.append(f"graph.composition missing {sorted(missing)}")
    if unknown:
        errors.append(f"graph.composition has unknown fields {sorted(unknown)}")
    arguments = composition.get("arguments")
    if not isinstance(arguments, dict):
        errors.append("graph.composition.arguments must be a mapping")
        return errors
    for argument_id, argument in arguments.items():
        if not isinstance(argument, dict):
            errors.append(f"composition argument {argument_id!r} must be a mapping")
            continue
        missing = ARGUMENT_FIELDS - argument.keys()
        unknown = argument.keys() - ARGUMENT_FIELDS
        if missing:
            errors.append(f"composition argument {argument_id!r} missing {sorted(missing)}")
        if unknown:
            errors.append(f"composition argument {argument_id!r} has unknown fields {sorted(unknown)}")
        route_assessment = argument.get("assessment")
        if not isinstance(route_assessment, dict):
            errors.append(f"composition argument {argument_id!r}.assessment must be a mapping")
            continue
        missing = ARGUMENT_ASSESSMENT_FIELDS - route_assessment.keys()
        unknown = route_assessment.keys() - ARGUMENT_ASSESSMENT_FIELDS
        if missing:
            errors.append(f"composition argument {argument_id!r}.assessment missing {sorted(missing)}")
        if unknown:
            errors.append(f"composition argument {argument_id!r}.assessment has unknown fields {sorted(unknown)}")
        route_workflow = argument.get("workflow")
        if not isinstance(route_workflow, dict):
            errors.append(f"composition argument {argument_id!r}.workflow must be a mapping")
            continue
        missing = ARGUMENT_WORKFLOW_FIELDS - route_workflow.keys()
        unknown = route_workflow.keys() - ARGUMENT_WORKFLOW_FIELDS
        if missing:
            errors.append(f"composition argument {argument_id!r}.workflow missing {sorted(missing)}")
        if unknown:
            errors.append(f"composition argument {argument_id!r}.workflow has unknown fields {sorted(unknown)}")
    return errors


def mermaid_variables(dag_path: Path) -> set[str]:
    text = dag_path.read_text(encoding="utf-8")
    block = text.split("```mermaid", 1)[1].split("```", 1)[0]
    variables = set()
    for line in block.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("class ", "classDef ", "subgraph ", "flowchart ", "end")):
            continue
        match = re.search(
            r"\b([A-Za-z][A-Za-z0-9]*)\s*(?:\(\[|\[|\()\s*\"", line
        )
        if match:
            variables.add(match.group(1))
    return variables


def find_cycle(children: dict[str, list[str]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    trail: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in visiting:
            start = trail.index(node)
            return trail[start:] + [node]
        if node in visited:
            return None
        visiting.add(node)
        trail.append(node)
        # A node whose file failed to parse is reported separately; do not crash the sweep on it.
        for child in children.get(node, ()):
            cycle = visit(child)
            if cycle:
                return cycle
        trail.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for node in children:
        cycle = visit(node)
        if cycle:
            return cycle
    return None


import hashlib


# Harmonization note (2026-08-01, WHGAP M7-F1/F2 adjudication): this check_lean is the
# ADVISORY v1 layer. For problems that enable it (currently werner-holevo-gap), the
# AUTHORITATIVE DAG_PROTOCOL §7.6 gate is tools/lean_dag_check.py --problem <p>, which
# additionally checks state-vs-content backing (the R11 MAJOR-2 class) and frozen-body
# drift. Severity divergences between the two tools resolve in lean_dag_check's favor.
LEAN_NON_NODE_BASENAMES = {"Interface", "Trust", "SelfTest", "Defs", "Model", "Scratch"}
LEAN_KEYS = {
    "module", "file", "claim", "composition", "state", "rel",
    "build", "claim_hash", "synced",
}


def extract_lean_block(path: Path):
    """Return the node's `lean:` metadata: None (absent), "none" (declared none), or dict."""
    if path.suffix in {".yaml", ".yml"}:
        metadata, _ = parse_node(path)
        lean = metadata.get("lean")
        return "none" if lean is None else lean
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    front = text[4:].split("\n---\n", 1)[0]
    raw = parse_front_matter(front)
    if "formalization" in raw:
        lean = raw.get("formalization", {}).get("lean")
        return "none" if lean is None else lean
    lines = front.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("lean:"):
            value = line[len("lean:"):].strip()
            if value:
                return "none" if value.split("#", 1)[0].strip() in ("none", "null") else value
            block: dict = {}
            for sub in lines[i + 1:]:
                if not sub.startswith((" ", "\t")):
                    break
                sub = sub.strip()
                if ":" not in sub:
                    continue
                key, val = sub.split(":", 1)
                if key.strip() in LEAN_KEYS:
                    try:
                        block[key.strip()] = parse_scalar(val)
                    except (ValueError, json.JSONDecodeError):
                        block[key.strip()] = val.strip()
            return block
    return None


def frozen_claim_hash(claim: str | None) -> str | None:
    """DAG_PROTOCOL section 7.6 freeze rule: claim.statement LF bytes, stripped."""
    if not isinstance(claim, str):
        return None
    frozen = claim.replace("\r\n", "\n").strip()
    return hashlib.sha256(frozen.encode("utf-8")).hexdigest()


def check_lean(
    problem_root: Path,
    records: dict[str, dict],
    bodies: dict[str, str],
    errors: list[str],
    warnings: list[str],
) -> None:
    """DAG_PROTOCOL section 7.6 checks. v1 rollout: structural non-existence of DECLARED
    objects is an error; orphan modules, OR-route mismatch and undeclared imports are
    warnings (multiple problems share this tool mid-migration).

    PROMOTED TO ERROR 2026-07-31 (statement-fidelity review section 12.2, closeout item C-3):
    check 3a, frozen-Claim hash drift.  A warning that campaign records routinely summarize as
    "validators exit 0" is not a gate: two live section 7.6 anti-drift breaks (KSUM.A2b, KSUM.B1)
    sat undetected behind exit 0 for a day, one of them making a Lean docstring's word "verbatim"
    false.  Drift between a node's `claim.statement` and the `lean.claim_hash` frozen over it now
    FAILS validation.  Check 3b (Lean docstring hash vs node metadata) stays a warning: it compares
    two records of the same freeze rather than a record against the source of truth."""
    lean_root = problem_root / "proof-dag" / "lean"
    prefix = None
    for node_id in records:
        prefix = node_id.split(".", 1)[0]
        break
    lean_meta: dict[str, object] = {}
    for node_id, metadata in records.items():
        node_path = ROOT / metadata["node_file"]
        lean_meta[node_id] = extract_lean_block(node_path)

    # 7.6 check 1: declared module file / Claim / composition theorems exist.
    for node_id, block in lean_meta.items():
        if not isinstance(block, dict):
            continue
        file_field = block.get("file")
        if file_field:
            target = ROOT / str(file_field)
            if not target.exists():
                errors.append(f"{node_id}: lean.file does not exist: {file_field}")
                continue
            if target.is_file():
                lean_text = target.read_text(encoding="utf-8")
                claim = block.get("claim")
                if claim and not re.search(
                    rf"^\s*(?:def|abbrev)\s+{re.escape(str(claim))}\b", lean_text, re.MULTILINE
                ):
                    errors.append(f"{node_id}: declared lean.claim {claim!r} not found in {file_field}")
                comp = block.get("composition")
                comp_names = comp if isinstance(comp, list) else ([comp] if comp else [])
                for name in comp_names:
                    if name and not re.search(
                        rf"^\s*theorem\s+{re.escape(str(name))}\b", lean_text, re.MULTILINE
                    ):
                        errors.append(
                            f"{node_id}: declared lean.composition {name!r} not found in {file_field}"
                        )
                # 7.6 check 3b: hash quoted in the Lean docstring vs node metadata.
                declared_hash = str(block.get("claim_hash") or "").removeprefix("sha256:")
                doc_hashes = re.findall(r"\b[0-9a-f]{64}\b", lean_text[:4000])
                if declared_hash and doc_hashes and declared_hash not in doc_hashes:
                    warnings.append(
                        f"{node_id}: lean docstring hash differs from node lean.claim_hash"
                    )
        # 7.6 check 3a: freeze-rule hash agreement with the node's own Claim section.
        declared_hash = str(block.get("claim_hash") or "").removeprefix("sha256:")
        if declared_hash and len(declared_hash) == 64:
            claim = records[node_id].get("claim")
            if claim is None:
                match = re.search(
                    r"^## Claim\n(.*?)(?=^## )",
                    bodies.get(node_id, ""),
                    flags=re.MULTILINE | re.DOTALL,
                )
                claim = match.group(1).strip("\n") if match else None
            computed = frozen_claim_hash(claim)
            if computed and computed != declared_hash:
                # ERROR since 2026-07-31 (was a warning): see this function's docstring.
                errors.append(
                    f"{node_id}: frozen-Claim hash drift (node claim.statement hashes {computed[:8]}..., "
                    f"lean.claim_hash records {declared_hash[:8]}...) - re-sync the Lean docstring "
                    f"quotation and lean.claim_hash in the same change (DAG_PROTOCOL 7.6 check 3)"
                )
        # 7.6 check 4: OR composition_via_* set vs children.
        meta = records[node_id]
        comp = block.get("composition") if isinstance(block, dict) else None
        if meta["kind"] == "OR" and isinstance(comp, list):
            expected = {f"composition_via_{child.rsplit('.', 1)[-1]}" for child in meta["children"]}
            actual = {str(name) for name in comp}
            if not actual <= expected:
                warnings.append(
                    f"{node_id}: composition_via names not matching any child: {sorted(actual - expected)}"
                )
            for child in meta["children"]:
                name = f"composition_via_{child.rsplit('.', 1)[-1]}"
                if name in actual:
                    continue
                child_block = lean_meta.get(child)
                if child_block == "none" or (
                    isinstance(child_block, dict) and str(child_block.get("state")) == "none"
                ):
                    continue  # route justified by the child's own `lean: none` record
                warnings.append(
                    f"{node_id}: route via {child} has no composition_via theorem and the child "
                    f"carries no lean:none justification"
                )
    if not lean_root.is_dir() or prefix is None:
        return
    # 7.6 check 2: node-shaped Lean modules must have a matching node.
    module_ids: dict[str, Path] = {}
    for lean_file in lean_root.rglob("*.lean"):
        if ".lake" in lean_file.parts:
            continue
        rel = lean_file.relative_to(lean_root)
        parts = list(rel.with_suffix("").parts)
        if parts[0] != prefix or len(parts) == 1:
            continue
        if parts[-1] in LEAN_NON_NODE_BASENAMES or "Support" in parts:
            continue
        dotted = ".".join(parts)
        module_ids[dotted] = lean_file
        if dotted not in records:
            warnings.append(
                f"orphan lean module {rel.as_posix()} (derived id {dotted} matches no node)"
            )
    # 7.6 check 5: node-module imports must be children or declared relative hypotheses.
    for dotted, lean_file in module_ids.items():
        if dotted not in records:
            continue
        meta = records[dotted]
        block = lean_meta.get(dotted)
        rel_text = " ".join(str(r) for r in block.get("rel", [])) if isinstance(block, dict) else ""
        text = lean_file.read_text(encoding="utf-8")
        for match in re.finditer(rf"^import\s+({re.escape(prefix)}\.[A-Za-z0-9_.]+)", text, re.MULTILINE):
            imported = match.group(1)
            if imported not in records:
                continue
            if imported in meta["children"] or imported in rel_text:
                continue
            warnings.append(
                f"{dotted}: imports node module {imported} that is neither a child "
                f"nor declared in lean.rel"
            )


def check_problem(problem: str, verify_git: bool = False) -> tuple[list[str], list[str], int]:
    problem_root = ROOT / PROBLEM_DIRS[problem]
    if problem in STRICT_DECOMPOSITION_PROBLEMS:
        return validate_problem_v6(ROOT, problem_root, problem, verify_git=verify_git)
    base = problem_root / "proof-dag"
    nodes_dir = base / "nodes"
    dag_name = f"{problem.upper()}_PROOF_DAG.md"
    dag_path = problem_root / "notes" / dag_name
    errors: list[str] = []
    warnings: list[str] = []
    records: dict[str, dict] = {}
    bodies: dict[str, str] = {}
    aliases: dict[str, str] = {}

    if not nodes_dir.is_dir():
        return [f"{problem}: missing {nodes_dir.relative_to(ROOT)}"], [], 0

    node_suffix = ".yaml" if problem in STRICT_DECOMPOSITION_PROBLEMS else ".md"
    for path in sorted(nodes_dir.glob(f"*{node_suffix}")):
        try:
            metadata, body = parse_node(path)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        record_schema_errors = schema_errors(
            metadata, strict_grouped=problem in STRICT_DECOMPOSITION_PROBLEMS
        )
        if record_schema_errors:
            errors.extend(
                f"{path.relative_to(ROOT)}: {message}"
                for message in record_schema_errors
            )
            continue
        node_id = metadata["id"]
        if node_id in records:
            errors.append(f"{node_id}: duplicate id")
        records[node_id] = metadata
        bodies[node_id] = body
        if path.name != f"{node_id}{node_suffix}":
            errors.append(f"{node_id}: filename is {path.name!r}")
        expected_node_file = path.relative_to(ROOT).as_posix()
        if metadata.get("node_file") is not None and metadata["node_file"] != expected_node_file:
            errors.append(
                f"{node_id}: node_file is {metadata['node_file']!r}, "
                f"expected {expected_node_file!r}"
            )
        metadata["node_file"] = expected_node_file
        if metadata["kind"] not in ALLOWED_KINDS:
            errors.append(f"{node_id}: invalid kind {metadata['kind']!r}")
        if metadata["role"] not in ALLOWED_ROLES:
            errors.append(f"{node_id}: invalid role {metadata['role']!r}")
        for field in ("aliases", "children", "related"):
            if not isinstance(metadata[field], list):
                errors.append(f"{node_id}: {field} must be a list")
        if problem in STRICT_DECOMPOSITION_PROBLEMS:
            kind = metadata["kind"]
            children = metadata["children"]
            if kind in {"GOAL", "LEAF"}:
                errors.append(
                    f"{node_id}: deprecated kind {kind!r}; use OR/AND decomposition "
                    "semantics, or null when children is empty"
                )
            if children and kind not in {"OR", "AND"}:
                errors.append(
                    f"{node_id}: nodes with children require kind OR or AND"
                )
            if not children and kind is not None:
                errors.append(
                    f"{node_id}: nodes without children require kind null"
                )
            composition = metadata["composition"]
            arguments = composition.get("arguments", {})
            if not children and arguments:
                errors.append(
                    f"{node_id}: nodes without children require composition.arguments: {{}}"
                )
            if children and not arguments:
                errors.append(
                    f"{node_id}: nodes with children require composition arguments"
                )
            if children and kind == "AND":
                if set(arguments) != {"joint"}:
                    errors.append(
                        f"{node_id}: AND composition must contain exactly the 'joint' argument"
                    )
                elif arguments["joint"].get("premises") != children:
                    errors.append(
                        f"{node_id}: joint argument premises must equal graph.children"
                    )
            if children and kind == "OR":
                for child in children:
                    route = arguments.get(child)
                    if route is None:
                        errors.append(f"{node_id}: missing OR route argument for {child}")
                    elif route.get("premises") != [child]:
                        errors.append(
                            f"{node_id}: OR route {child} must have premises: [{child!r}]"
                        )
                for route_id in sorted(set(arguments) - set(children)):
                    route = arguments[route_id]
                    route_status = route.get("assessment", {}).get("status")
                    if route_status != "RETIRED-EDGE" or route.get("premises") != []:
                        errors.append(
                            f"{node_id}: non-child argument {route_id!r} must be a "
                            "RETIRED-EDGE record with no active premises"
                        )
            for argument_id, argument in arguments.items():
                route_assessment = argument.get("assessment", {})
                route_workflow = argument.get("workflow", {})
                route_status = route_assessment.get("status")
                if route_status not in ALLOWED_STATUSES | {"RETIRED-EDGE"}:
                    errors.append(
                        f"{node_id}: composition argument {argument_id!r} has invalid "
                        f"status {route_status!r}"
                    )
                if route_workflow.get("disposition") not in ALLOWED_DISPOSITIONS:
                    errors.append(
                        f"{node_id}: composition argument {argument_id!r} has invalid "
                        f"disposition {route_workflow.get('disposition')!r}"
                    )
                if route_status in COMPLETION_TIERS | {"REFUTED", "RETIRED-EDGE"} \
                        and not route_assessment.get("source"):
                    errors.append(
                        f"{node_id}: composition argument {argument_id!r} at {route_status} "
                        "requires assessment.source"
                    )
        if metadata["status"] not in ALLOWED_STATUSES:
            errors.append(f"{node_id}: invalid status {metadata['status']!r}")
        if metadata["disposition"] not in ALLOWED_DISPOSITIONS:
            errors.append(
                f"{node_id}: invalid disposition {metadata['disposition']!r}"
            )
        for alias in metadata["aliases"]:
            if alias in aliases:
                errors.append(
                    f"{node_id}: alias {alias!r} also belongs to {aliases[alias]}"
                )
            aliases[alias] = node_id

        if path.suffix == ".md":
            sections = set(re.findall(r"^## (.+)$", body, flags=re.MULTILINE))
            missing_sections = LEGACY_REQUIRED_SECTIONS - sections
            if missing_sections:
                errors.append(
                    f"{node_id}: missing sections {sorted(missing_sections)}"
                )

        for target in MARKDOWN_LINK.findall(body):
            if "://" in target or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).resolve().exists():
                errors.append(f"{node_id}: broken local link {target!r}")

    # Build the reverse index on demand from the sole stored structural edge
    # list.  It is intentionally not written back into node metadata.
    derived_reverse_dependencies = {node_id: [] for node_id in records}
    for node_id, metadata in records.items():
        for field in ("children", "related"):
            for target in metadata[field]:
                if target not in records:
                    errors.append(f"{node_id}: unknown {field} target {target}")
        for child in metadata["children"]:
            if child in derived_reverse_dependencies:
                derived_reverse_dependencies[child].append(node_id)

    if records:
        cycle = find_cycle(
            {node_id: metadata["children"] for node_id, metadata in records.items()}
        )
        if cycle:
            errors.append("propagating graph cycle: " + " -> ".join(cycle))

    # LINT-COMPLETION (DAG_PROTOCOL section 1, single-status model 2026-08-08).
    for node_id, metadata in records.items():
        if metadata["status"] not in COMPLETION_TIERS or not metadata["children"]:
            continue
        child_statuses = {c: records.get(c, {}).get("status") for c in metadata["children"]}
        if metadata["kind"] == "AND":
            below = sorted(c for c, s in child_statuses.items() if s not in COMPLETION_TIERS)
            if below and not RELATIVE_DISPLAY.search(bodies.get(node_id, "")):
                errors.append(
                    f"{node_id}: LINT-COMPLETION: {metadata['status']} AND-node with load-bearing "
                    f"children below completion tier {below} and no relative-hypothesis display"
                )
        elif metadata["kind"] == "OR":
            if not any(s in COMPLETION_TIERS for s in child_statuses.values()):
                warnings.append(
                    f"{node_id}: {metadata['status']} {metadata['kind']}-node has no "
                    f"completion-tier route child - verify it holds a direct whole-claim review"
                )

    mermaid = mermaid_variables(dag_path)
    missing_aliases = mermaid - aliases.keys()
    extra_aliases = aliases.keys() - mermaid
    if missing_aliases:
        errors.append(f"{problem}: Mermaid nodes without files: {sorted(missing_aliases)}")
    if extra_aliases:
        errors.append(f"{problem}: node aliases absent from Mermaid: {sorted(extra_aliases)}")

    check_lean(problem_root, records, bodies, errors, warnings)

    index = (base / "NODE_INDEX.md").read_text(encoding="utf-8")
    for node_id in records:
        row_pattern = re.compile(
            rf"^\|\s*`[^`]+`\s*\|\s*`{re.escape(node_id)}`\s*\|",
            re.MULTILINE,
        )
        if len(row_pattern.findall(index)) != 1:
            errors.append(f"{node_id}: NODE_INDEX table-row count is not one")

    return errors, warnings, len(records)


def chain_strength_report(problem: str) -> None:
    """On-demand read-only diagnostic (DAG_PROTOCOL section 1, single-status model):
    old-style bottom-up subtree support.  A node with no children has its own ladder rank;
    chain(AND) = min over child chains; chain(OR) = max over non-REFUTED child
    chains (a REFUTED route is dead, not evidence against the claim).  Prints every
    internal node whose hand-written status outranks its subtree support.  That is
    LEGAL under the single-status model (e.g. NUMERICAL on direct whole-claim gates
    while children are OPEN) - this report exists so a human can see where the
    chain is thinner than the label, not to fail anything."""
    problem_root = ROOT / PROBLEM_DIRS[problem]
    if problem in STRICT_DECOMPOSITION_PROBLEMS:
        chain_strength_report_v6(problem_root, problem)
        return
    nodes_dir = problem_root / "proof-dag" / "nodes"
    records: dict[str, dict] = {}
    node_suffix = ".yaml" if problem in STRICT_DECOMPOSITION_PROBLEMS else ".md"
    for path in sorted(nodes_dir.glob(f"*{node_suffix}")):
        try:
            metadata, _ = parse_node(path)
            records[metadata["id"]] = metadata
        except (ValueError, json.JSONDecodeError):
            continue
    memo: dict[str, int] = {}

    def chain(nid: str, stack: tuple = ()) -> int:
        if nid in memo:
            return memo[nid]
        meta = records.get(nid)
        if meta is None or nid in stack:
            return LADDER_RANK["OPEN"]
        children = meta["children"]
        if not children:
            memo[nid] = LADDER_RANK.get(meta["status"], 0)
            return memo[nid]
        ranks = [chain(c, stack + (nid,)) for c in children]
        if meta["kind"] == "AND":
            support = min(ranks)
        else:
            live = [r for r in ranks if r >= 0]
            support = max(live) if live else -1
        memo[nid] = support
        return support

    inv = {v: k for k, v in LADDER_RANK.items()}
    rows = []
    for nid, meta in records.items():
        if not meta["children"]:
            continue
        own = LADDER_RANK.get(meta["status"], 0)
        support = chain(nid)
        if own > support:
            rows.append((nid, meta["status"], inv.get(support, str(support))))
    print(f"[chain-strength] {problem}: {len(rows)} internal node(s) whose status outranks subtree support")
    for nid, status, support in sorted(rows):
        print(f"  {nid}: status {status}, subtree support {support}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", choices=tuple(PROBLEM_DIRS) + ("all",), default="all")
    parser.add_argument("--diagnose", choices=("chain-strength",), default=None,
                        help="print the read-only chain-strength report after validation")
    parser.add_argument("--write-generated", action="store_true",
                        help="regenerate v6 NODE_INDEX.md and GRAPH.mmd before validation")
    parser.add_argument("--verify-git", action="store_true",
                        help="resolve every git:<commit>:<path> source with git cat-file")
    args = parser.parse_args()
    problems = tuple(PROBLEM_DIRS) if args.problem == "all" else (args.problem,)
    if args.write_generated:
        for problem in problems:
            if problem in STRICT_DECOMPOSITION_PROBLEMS:
                write_generated_v6(ROOT / PROBLEM_DIRS[problem], problem)
    all_errors: list[str] = []
    all_warnings: list[str] = []
    total = 0
    for problem in problems:
        errors, warnings, count = check_problem(problem, verify_git=args.verify_git)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        total += count
        if not errors:
            print(f"{problem}: {count} node files structurally valid")
    for warning in all_warnings:
        print(f"WARNING: {warning}")
    if args.diagnose == "chain-strength":
        for problem in problems:
            chain_strength_report(problem)
    if all_errors:
        print("Proof-DAG validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1
    print(f"Proof-DAG validation OK: {total} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
