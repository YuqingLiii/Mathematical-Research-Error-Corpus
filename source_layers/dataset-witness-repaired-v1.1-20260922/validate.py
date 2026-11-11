"""Read-only structural and integrity validation; not mathematical validation."""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import json, re

ROOT=Path(__file__).resolve().parent
def read(name):return json.loads((ROOT/name).read_text())
def digest(path):
    h=sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

stats=read('statistics.json')
positive=read('index.json'); negative=read('excluded.json')
ids=[r['record_id'] for r in positive+negative]
assert len(ids)==len(set(ids))==77
assert set(ids)=={f'{i:03}' for i in range(1,78)}
assert len(positive)==stats['included_errors']
assert len(negative)==stats['excluded_allegations']
assert stats['pending_admission']==0
records=[json.loads(line) for line in (ROOT/'records.jsonl').read_text().splitlines()]
registry=[json.loads(line) for line in (ROOT/'audit/all_77.jsonl').read_text().splitlines()]
assert [r['record_id'] for r in records]==stats['included_ids']
assert [r['record_id'] for r in negative]==stats['excluded_ids']
assert len(registry)==77
assert sum(r['overclaim'] is True for r in records)==stats['overclaim']
assert sum(r['overclaim'] is False for r in records)==stats['other_errors']
assert dict(Counter(r['problem'] for r in records))==stats['problems']
assert dict(Counter(r['collection_context'] for r in records))==stats['collection_contexts']
byid={r['record_id']:r for r in registry}
source_files=0; new_source_windows=0
for entry in positive+negative:
    dossier=ROOT/Path(entry['evidence']).parent
    assert (ROOT/entry['evidence']).is_file()
    r=json.loads((dossier/'record.json').read_text())
    assert r==byid[entry['record_id']]
    if r['admission']=='included':
        assert r in records
        for field in ('excerpt','context','locator'):assert r['original'][field].strip()
        for field in ('explanation','evidence','scope'):assert r['witness'][field].strip()
        assert r['witness']['endorsement']=='accepted_scoped_witness'
        assert not any(x in r['mechanism'] for x in ['待核','待定','pending','unresolved'])
    else:
        assert r['admission']=='excluded' and r['overclaim'] is None
        assert r['witness']['endorsement']=='historical_allegation_not_endorsed'
    assert r['computational_checks']['path_base']=='release_root'
    assert (ROOT/r['computational_checks']['file']).is_file()
    for m in json.loads((dossier/'materials.json').read_text()):
        assert (dossier/m['file']).is_file(),m
        assert digest(dossier/m['file'])==m['sha256'],m['file']
        source_files+=m['kind']=='inherited_sanitized_source'
        new_source_windows+=m['kind']=='reconciliation_source_window'

preserved=read('audit/input_file_preservation.json')
assert len(preserved)==1273
for x in preserved:
    file=ROOT/x['release_file']
    assert file.stat().st_size==x['bytes']
    assert digest(file)==x['sha256']
assert source_files==1195

# Validate links in generated navigation, not links embedded in historical
# source quotes or old third-party documents with their original structure.
navigation=['README.md','INDEX.md','EXCLUDED.md','RECONCILIATION.md']
for name in navigation:
    for link in re.findall(r'\]\(([^)]+)\)',(ROOT/name).read_text()):
        if '://' in link or link.startswith('#'):continue
        assert (ROOT/link.split('#',1)[0]).exists(),(name,link)

checks=read('checks/witness_checks.json')
assert checks and all(c['passed'] is True for c in checks)
assert all(set(c['records'])<=set(ids) for c in checks)

manifest=ROOT/'SHA256SUMS.txt'
verified_files=0
if manifest.exists():
    listed=set()
    for line in manifest.read_text().splitlines():
        sha,name=line.split('  ',1)
        assert name not in listed
        listed.add(name)
        assert digest(ROOT/name)==sha,name
        verified_files+=1
    actual={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p!=manifest}
    assert actual==listed,(sorted(actual-listed),sorted(listed-actual))

print(json.dumps(dict(validation='PASS',historical_registry=77,
    included_errors=len(positive),excluded_allegations=len(negative),pending=0,
    overclaim=stats['overclaim'],other_errors=stats['other_errors'],
    original_material_files_preserved=source_files,input_files_preserved=len(preserved),
    added_source_windows=new_source_windows,archived_local_checks=len(checks),
    manifest_present=manifest.exists(),manifest_files_verified=verified_files,
    interpretation='Structural integrity, provenance accounting, and archived-check bookkeeping; not a fresh certification of all mathematics.'),ensure_ascii=False,indent=2))
