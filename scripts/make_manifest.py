"""Hash every tracked deliverable, including evidence and generated audit reports."""
from common import ROOT,digest,write

def make():
    files=[]
    for f in sorted(ROOT.rglob('*')):
        rel=f.relative_to(ROOT)
        if not f.is_file() or str(rel)=='manifest.json' or any(x in {'.git','.venv','__pycache__'} for x in rel.parts):continue
        files.append({'path':str(rel),'bytes':f.stat().st_size,'sha256':digest(f)})
    return {'schema_version':'1.0.0','visibility_requirement':'private',
        'canonical_records':'data/records.jsonl','canonical_classification':'yoshida-level1-v3-20260923',
        'record_count':65,'historical_registry_count':77,'readiness':'audited_working_corpus_with_explicit_limitations',
        'files':files,'manifest_self_excluded':True}

if __name__=='__main__':
    m=make();write(ROOT/'manifest.json',m)
    print('Manifest:',len(m['files']),'files;',sum(x['bytes'] for x in m['files']),'bytes')
