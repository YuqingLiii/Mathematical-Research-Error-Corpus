#!/usr/bin/env python3
"""Legacy whole-repository Holevo boundary diagnostic.

This checker is deliberately non-load-bearing for focused adversarial-review packages: it assumes
the complete canonical three-project trees and therefore reports missing-root errors on a scoped
27-claim dossier. Focused packages advertise and use their bundled ``check_focused_scope.py``
instead. Keep this script only for full-repository boundary checks.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]

PROJECTS = {
    "holevo-additivity-equality": {
        "root": "HAEQ.goal",
        "prefix": "HAEQ.",
        "verdict": "artifacts/BOSS_QUESTION_1_VERDICT_20260830.md",
    },
    "holevo-counterexample-prevalence": {
        "root": "HCPREV.goal",
        "prefix": "HCPREV.",
        "verdict": "artifacts/BOSS_QUESTION_2_VERDICT_20260830.md",
    },
    "holevo-extensive-violation": {
        "root": "HEXT.goal",
        "prefix": "HEXT.",
        "verdict": "artifacts/BOSS_QUESTION_3_VERDICT_20260830.md",
    },
}

FORBIDDEN_CANONICAL = re.compile(
    r"(?:\bWHGAP\b|werner-holevo-capacity-threshold|werner-holevo-gap)",
    re.IGNORECASE,
)


def check_project(name: str, spec: dict[str, str]) -> list[str]:
    errors: list[str] = []
    project = ROOT / name
    project_file = project / "proof-dag/PROJECT.yaml"
    verdict = project / spec["verdict"]

    if not project_file.is_file():
        return [f"{name}: missing proof-dag/PROJECT.yaml"]
    if not verdict.is_file():
        errors.append(f"{name}: missing boss verdict {spec['verdict']}")

    try:
        metadata = yaml.safe_load(project_file.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        return errors + [f"{name}: cannot parse PROJECT.yaml: {exc}"]

    if metadata.get("roots") != [spec["root"]]:
        errors.append(
            f"{name}: roots must be exactly [{spec['root']!r}], got {metadata.get('roots')!r}"
        )

    node_dir = project / "proof-dag/nodes"
    nodes = sorted(node_dir.glob("*.yaml"))
    if not nodes:
        errors.append(f"{name}: no canonical node files")
        return errors

    for node_path in nodes:
        text = node_path.read_text(encoding="utf-8")
        try:
            node = yaml.safe_load(text) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{node_path.relative_to(ROOT)}: cannot parse YAML: {exc}")
            continue
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id.startswith(spec["prefix"]):
            errors.append(
                f"{node_path.relative_to(ROOT)}: id {node_id!r} must use prefix {spec['prefix']!r}"
            )
        match = FORBIDDEN_CANONICAL.search(text)
        if match:
            errors.append(
                f"{node_path.relative_to(ROOT)}: forbidden WHGAP dependency token {match.group(0)!r}"
            )

    return errors


def main() -> int:
    errors: list[str] = []
    index = ROOT / "HOLEVO_ADDITIVITY_THREE_QUESTION_INDEX.md"
    if not index.is_file():
        errors.append("missing HOLEVO_ADDITIVITY_THREE_QUESTION_INDEX.md")

    for name, spec in PROJECTS.items():
        errors.extend(check_project(name, spec))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    node_count = sum(
        len(list((ROOT / name / "proof-dag/nodes").glob("*.yaml"))) for name in PROJECTS
    )
    print(
        "Holevo scope boundary OK: "
        f"{len(PROJECTS)} independent projects, {node_count} canonical nodes, "
        "no WHGAP dependency in canonical YAML"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
