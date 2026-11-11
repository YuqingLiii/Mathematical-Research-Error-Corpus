#!/usr/bin/env python3
"""Reject edits that rewrite or silently bypass existing proof-DAG history."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
NODE_GLOBS = (
    "research/ksum/proof-dag/nodes/*.yaml",
    "research/se/proof-dag/nodes/*.yaml",
)


def git_text(ref: str, path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def load_yaml(text: str, label: str) -> dict:
    try:
        value = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ValueError(f"{label}: invalid YAML: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label}: expected a mapping")
    return value


def current_node_paths() -> list[Path]:
    paths: list[Path] = []
    for pattern in NODE_GLOBS:
        paths.extend(ROOT.glob(pattern))
    return sorted(paths)


def baseline_node_paths(ref: str) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            ref,
            "--",
            "research/ksum/proof-dag/nodes",
            "research/se/proof-dag/nodes",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"cannot read base revision {ref!r}: {result.stderr.strip()}")
    return [ROOT / line for line in result.stdout.splitlines() if line.endswith(".yaml")]


def level(record: dict) -> str | None:
    assessment = record.get("assessment")
    return assessment.get("level") if isinstance(assessment, dict) else None


def route_levels(record: dict) -> dict[str, str | None]:
    routes = record.get("routes")
    if not isinstance(routes, dict):
        return {}
    result: dict[str, str | None] = {}
    for route_id, route in routes.items():
        assessment = route.get("assessment") if isinstance(route, dict) else None
        result[str(route_id)] = (
            assessment.get("level") if isinstance(assessment, dict) else None
        )
    return result


def matching_level_event(
    events: dict,
    new_event_ids: set[str],
    old: str | None,
    new: str | None,
    route_id: str | None = None,
) -> bool:
    for event_id in new_event_ids:
        event = events.get(event_id)
        if not isinstance(event, dict) or event.get("type") != "level-change":
            continue
        if event.get("from") != old or event.get("to") != new:
            continue
        if route_id is None and event.get("route") is None:
            return True
        if route_id is not None and event.get("route") == route_id:
            return True
    return False


def check_file(base_ref: str, path: Path) -> list[str]:
    relative = path.relative_to(ROOT).as_posix()
    old_text = git_text(base_ref, relative)
    if old_text is None:
        return []

    old = load_yaml(old_text, f"{base_ref}:{relative}")
    # The first migration from an older schema establishes the initial event
    # ledger.  Append-only comparison begins once the baseline has that ledger.
    old_events = old.get("events")
    if not isinstance(old_events, dict):
        return []

    if not path.exists():
        return [f"{relative}: deleted a node with an existing event ledger"]

    current = load_yaml(path.read_text(encoding="utf-8"), relative)
    events = current.get("events")
    if not isinstance(events, dict):
        return [f"{relative}: removed the existing event ledger"]

    errors: list[str] = []
    for event_id, old_event in old_events.items():
        if event_id not in events:
            errors.append(f"{relative}: deleted historical event {event_id!r}")
        elif events[event_id] != old_event:
            errors.append(f"{relative}: rewrote historical event {event_id!r}")

    new_event_ids = set(events) - set(old_events)
    old_level, new_level = level(old), level(current)
    if old_level != new_level and not matching_level_event(
        events, new_event_ids, old_level, new_level
    ):
        errors.append(
            f"{relative}: node level changed {old_level!r} -> {new_level!r} "
            "without a new matching level-change event"
        )

    old_routes = route_levels(old)
    new_routes = route_levels(current)
    for route_id in sorted(set(old_routes) - set(new_routes)):
        retired = any(
            event_id in new_event_ids
            and isinstance(event, dict)
            and event.get("type") == "route-retired"
            and event.get("route") == route_id
            for event_id, event in events.items()
        )
        if not retired:
            errors.append(
                f"{relative}: removed route {route_id!r} without a new route-retired event"
            )
    for route_id in sorted(set(old_routes) & set(new_routes)):
        old_route_level = old_routes[route_id]
        new_route_level = new_routes[route_id]
        if old_route_level == new_route_level:
            continue
        if not matching_level_event(
            events,
            new_event_ids,
            old_route_level,
            new_route_level,
            route_id,
        ):
            errors.append(
                f"{relative}: route {route_id!r} changed level "
                f"{old_route_level!r} -> {new_route_level!r} without a new "
                "matching route level-change event"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-ref",
        default="HEAD",
        help="Git revision whose existing events must remain unchanged (default: HEAD)",
    )
    args = parser.parse_args()

    errors: list[str] = []
    try:
        paths = set(current_node_paths()) | set(baseline_node_paths(args.base_ref))
        for path in sorted(paths):
            errors.extend(check_file(args.base_ref, path))
    except ValueError as exc:
        errors.append(str(exc))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Append-only event check OK against {args.base_ref}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
