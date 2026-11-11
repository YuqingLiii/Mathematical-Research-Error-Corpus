#!/usr/bin/env python3
"""Structural and link check for the anonymous review copy. It does not check mathematics."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN = "source_layers/dataset-witness-repaired-v1.1-20260922"


def lines(p):
    return [json.loads(x) for x in (ROOT / p).read_text(encoding="utf-8").splitlines() if x.strip()]


def main():
    errors, notes = [], {}
    excluded = set()
    for row in (ROOT / "provenance/ANONYMOUS_COPY_EXCLUSIONS.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        excluded.add(row.split("\t")[0])
    rows = lines("data/records.jsonl")
    ids = [r["record_id"] for r in rows]
    if len(rows) != 65 or len(set(ids)) != 65:
        errors.append(f"expected 65 unique records, found {len(rows)} / {len(set(ids))}")
    problems = json.loads((ROOT / "data/problems.json").read_text(encoding="utf-8"))
    mapped = [i for p in problems for i in p["record_ids"]]
    if len(problems) != 12:
        errors.append(f"expected 12 problems, found {len(problems)}")
    if sorted(mapped) != sorted(ids):
        errors.append("problem mapping does not cover exactly the 65 record IDs")
    by_problem = {p["problem_id"]: p["name"] for p in problems}
    for r in rows:
        if by_problem.get(r["problem_id"]) != r["problem"]:
            errors.append(f"{r['record_id']}: problem name differs from data/problems.json")
    excl = json.loads((ROOT / "data/excluded.json").read_text(encoding="utf-8"))
    if {x["record_id"] for x in excl} | set(ids) != {f"{i:03}" for i in range(1, 78)} or set(ids) & {x["record_id"] for x in excl}:
        errors.append("accepted + excluded IDs do not partition 001..077")
    index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    expect = [{"record_id": r["record_id"], "problem": r["problem"], "summary": r["summary"], "evidence": r["witness"]["document"]} for r in rows]
    if index != expect:
        errors.append("index.json differs from data/records.jsonl")
    try:
        from jsonschema import Draft202012Validator
        v = Draft202012Validator(json.loads((ROOT / "schemas/record.schema.json").read_text(encoding="utf-8")))
        bad = [r["record_id"] for r in rows if not v.is_valid(r)]
        if bad:
            errors.append(f"schema violations: {bad}")
        notes["schema"] = "checked"
    except ImportError:
        notes["schema"] = "skipped (jsonschema not installed)"
    present = omitted = 0
    missing = []

    def ref(path, label):
        nonlocal present, omitted
        p = path.split("#")[0]
        if (ROOT / p).exists():
            present += 1
        elif p in excluded or any(p.startswith(e.rstrip("/") + "/") for e in excluded):
            omitted += 1
        else:
            missing.append(f"{label}: {p}")

    for r in rows:
        rid = r["record_id"]
        ref(r["witness"]["document"], rid)
        ref(r["provenance"]["frozen_record"], rid)
        for m in r["provenance"]["materials"]:
            ref(m["path"], rid)
        for b in r["original"]["source_bindings"]:
            for m in b["matches"]:
                ref(m["path"], rid)
        for c in r["witness"]["fresh_checks"]:
            ref(c["result_file"], rid)
        if r["model_attribution"].get("evidence_document"):
            ref(r["model_attribution"]["evidence_document"], rid)
    for x in excl:
        ref(x["evidence"], x["record_id"])
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    md_links = 0
    for md in [ROOT / "README.md", *(ROOT / "docs").glob("*.md"), *(ROOT / FROZEN).glob("*.md"), *(ROOT / FROZEN / "records").glob("*/witness.md")]:
        for target in link.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            md_links += 1
            rel = (md.parent / target.split("#")[0]).resolve()
            try:
                rel_s = rel.relative_to(ROOT.resolve()).as_posix()
            except ValueError:
                missing.append(f"{md.relative_to(ROOT)}: link leaves repository: {target}")
                continue
            ref(rel_s, md.relative_to(ROOT).as_posix())
    if missing:
        errors.append(f"{len(missing)} unresolved references, e.g. {missing[:5]}")
    ident = re.compile(r"/Users/[A-Za-z0-9._-]+|[A-Za-z]:\\\\Users\\\\|chatgpt\.com/(?:c|share)/|claude\.ai/(?:chat|share)/|sk-ant-[A-Za-z0-9]|ghp_[A-Za-z0-9]{20}|-----BEGIN [A-Z ]*PRIVATE KEY-----\n|(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]{1,63}\.(?:com|org|edu|net|io)\b")
    hits = []
    for f in ROOT.rglob("*"):
        # skip this checker and the corpus scanner: both only define search patterns
        if f.is_file() and f.resolve() != Path(__file__).resolve() and f.name != "scan_sensitive.py":
            try:
                t = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if ident.search(t):
                hits.append(f.relative_to(ROOT).as_posix())
    if hits:
        errors.append(f"identity/credential patterns in {hits[:10]}")
    result = {"records": len(rows), "problems": len(problems), "excluded_allegations": len(excl),
              "references_present": present, "references_to_omitted_files": omitted,
              "markdown_links_checked": md_links, **notes, "errors": errors,
              "status": "PASS" if not errors else "FAIL"}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
