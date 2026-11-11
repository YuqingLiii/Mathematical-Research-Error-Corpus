"""Separate structural/statistical validation from optional mathematical checks."""
import argparse,json,subprocess,sys
from collections import Counter,defaultdict
from jsonschema import Draft202012Validator
from common import *

def validate():
    validator=Draft202012Validator(read(ROOT/'schemas/record.schema.json'))
    rows=lines(ROOT/'data/records.jsonl');stats=read(ROOT/'data/statistics.json')
    frozen={x['record_id']:x for x in lines(FROZEN/'records.jsonl')}
    assert len(rows)==len(frozen)==65 and len({x['record_id'] for x in rows})==65
    assert {x['record_id'] for x in rows}==set(frozen)
    categories=Counter();subtypes=Counter();duplicates=defaultdict(list);material_count=0;quote_count=0
    for r in rows:
        validator.validate(r);rid=r['record_id'];orig=frozen[rid]
        assert r['summary']==orig['summary'] and r['problem']==orig['problem']
        assert r['original']['excerpt']==orig['original']['excerpt']
        assert r['witness']['evidence']==orig['witness']['evidence']
        assert r['legacy_id']==orig['adjudication']['prior_inventory_key']
        assert digest(resolve(r['provenance']['frozen_record']))==r['provenance']['frozen_record_sha256']
        for m in r['provenance']['materials']:
            assert digest(resolve(m['path']))==m['sha256'],m['path'];material_count+=1
        for binding in r['original']['source_bindings']:
            assert binding['matches']
            for match in binding['matches']:
                p=resolve(match['path']);assert digest(p)==match['sha256']
                a,b=match['packaged_lines'];assert 1<=a<=b
                selected='\n'.join(p.read_text().splitlines()[a-1:b])
                assert normalize(binding['quote']) in normalize(selected),(rid,match['path'])
                quote_count+=1
        cats=[x['category_id'] for x in r['classification']['categories']]
        assert len(set(cats))==len(cats);categories.update(cats)
        st=r['classification']['primary_logic_subtype']
        assert bool(st)==('IV' in cats)
        if st:subtypes[st['primary_subtype']]+=1
        for c in r['witness']['fresh_checks']:
            result=read(resolve(c['result_file']))['checks'][c['index']]
            assert rid in result['records'] and result['passed'] is True
            assert c['description']==result['description'] and c['scope']==result['scope']
        assert resolve(r['witness']['document']).is_file()
        duplicates[normalize(r['original']['excerpt'])].append(rid)
    assert categories=={'I':1,'II':3,'III':15,'IV':45,'V':2}
    assert subtypes=={'IV-1':13,'IV-2':27,'IV-4':3,'IV-7':2}
    assert sum(categories.values())==66
    assert [r['record_id'] for r in rows if len(r['classification']['categories'])>1]==['022']
    excluded=read(ROOT/'data/excluded.json')
    assert len(excluded)==12 and not set(x['record_id'] for x in excluded)&set(frozen)
    assert {x['record_id'] for x in excluded}|set(frozen)=={f'{i:03}' for i in range(1,78)}
    assert len(read(ROOT/'supplemental/external_five_excluded.json'))==5
    targeted=read(ROOT/'supplemental/model_evidence_20261005.json')
    assert {x['record_id'] for x in targeted}=={'018','039','052','060'}
    for x in targeted:
        rid=x['record_id'];r=next(r for r in rows if r['record_id']==rid)
        assert r['model_attribution']['artifact_author_model']==x['artifact_author_model']
        assert r['model_attribution']['fresh_model_identification'] is True
        if rid=='060':
            event=read(FROZEN/'records/060/reconciliation_sources/W11-write-event.json')
            assert event['original_line_sha256']==x['target_event']['raw_line_sha256']
            assert x['preceding_active_turn_context']['line']<x['target_event']['line']
        elif rid=='052':
            values=[e['original_line_sha256'] for p in (FROZEN/'records/052/original').glob('*.visible.json') for e in read(p)['events']]
            assert x['target_event']['raw_line_sha256'] in values
        else:
            hashes={m['sha256'] for m in r['provenance']['materials']}
            assert any('GPT-5.6 Sol, Value: 1' in e.get('verbatim_excerpt','') for e in x['evidence'])
            for e in x['evidence']:
                for key in ['submitted_message_sha256','prompt_sha256','final_answer_sha256','visible_conversation_sha256']:
                    if key in e.get('content',{}):assert e['content'][key] in hashes,(rid,key)
    for x in excluded:assert resolve(x['evidence']).is_file()
    duplicate_groups=[x for x in duplicates.values() if len(x)>1]
    assert not duplicate_groups,duplicate_groups
    expected_index=[{'record_id':r['record_id'],'problem':r['problem'],'summary':r['summary'],'evidence':r['witness']['document']} for r in rows]
    assert read(ROOT/'index.json')==expected_index
    out=subprocess.run([sys.executable,str(FROZEN/'validate.py')],capture_output=True,text=True,check=True)
    assert json.loads(out.stdout)['validation']=='PASS'
    from audit_reasoning import audit as reasoning_audit
    assert reasoning_audit()['status']=='PASS'
    from audit_paper import audit as paper_audit
    paper=paper_audit()
    manifest=read(ROOT/'manifest.json'); listed=set()
    for f in manifest['files']:
        p=resolve(f['path']);assert p.stat().st_size==f['bytes'] and digest(p)==f['sha256'],f['path'];listed.add(f['path'])
    from make_manifest import make
    assert listed=={f['path'] for f in make()['files']},'Manifest coverage differs'
    return {'structural_validation':'PASS','statistical_reproduction':'PASS','paper_mapping':'PASS',
        'records':65,'excluded':12,'problems':12,'category_labels':66,'logic_subtypes':dict(subtypes),
        'material_references_verified':material_count,'source_quote_bindings_verified':quote_count,
        'exact_duplicate_original_quotes':duplicate_groups,'manifest_files_verified':len(listed),
        'mathematics':'Not asserted by structural validation. Use --math and inspect scopes and unresolved limitations.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--math',action='store_true');args=p.parse_args()
    result=validate()
    if args.math:
        from run_witnesses import run
        from additional_witnesses import run as additional
        a,b=run(),additional()
        result['fresh_scoped_check_count']=a['check_count']+b['check_count']
        result['fresh_checks']='PASS; includes one certificate-bookkeeping check; not blanket mathematical certification'
    print(json.dumps(result,ensure_ascii=False,indent=2))
