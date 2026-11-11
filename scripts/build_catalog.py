"""Deterministically build usable records from bundled, immutable evidence layers."""
from collections import Counter
import json, re
from common import *

def build():
    source_records = lines(FROZEN/'records.jsonl')
    cats = {r['record_id']:r for r in read(LEVEL1/'records_with_categories.json')}
    subtypes = {r['record_id']:r for r in read(SUBTYPES/'records.json')}
    binding_input = {r['record_id']:r for r in read(FROZEN/'audit/excerpt_binding_checks.json')['records']}
    attributions = {r['record_id']:r for r in read(ROOT/'supplemental/historical_attributions.json')}
    fresh_models = {r['record_id']:r for r in read(ROOT/'supplemental/model_evidence_20261005.json')}
    execution = read(ROOT/'audit/witness_execution.json')
    check_sets = [('audit/witness_execution.json', execution['checks']),
                  ('audit/additional_witness_execution.json', read(ROOT/'audit/additional_witness_execution.json')['checks'])]
    problems = list(read(FROZEN/'statistics.json')['problems'])
    problem_ids = {p:f'P{i:02}' for i,p in enumerate(problems,1)}
    paper_names = [problems[0], 'Werner--Holevo zero-capacity boundary', problems[2], problems[3], problems[4],
                   r'Circuit vs.\ effective distance', problems[6], problems[7],
                   'Quantum $k$-sum problem', 'Set equality / collision', problems[10], problems[11]]
    paper_lines = (ROOT/'paper/main.tex').read_text().splitlines()
    problem_rows = []
    for p, name in zip(problems,paper_names):
        hits = [i for i,l in enumerate(paper_lines,1) if '& '+name in l]
        assert len(hits)==1,(p,hits)
        problem_rows.append({'problem_id':problem_ids[p], 'name':p, 'paper_table_name':name,
            'paper_table_line':hits[0], 'record_ids':[r['record_id'] for r in source_records if r['problem']==p]})
    write(ROOT/'data/problems.json', problem_rows)
    records, audits = [], []
    for r in source_records:
        rid = r['record_id']; dossier = FROZEN/'records'/rid
        c = cats[rid]; subtype = subtypes.get(rid)
        assert c['source_record_sha256']==digest(dossier/'record.json'), rid
        assert c['original']==r['original'] and c['witness']==r['witness'], rid
        assert bool(subtype)==any(x['category_id']=='IV' for x in c['categories'])
        if subtype:
            assert subtype['source_record_sha256']==digest(dossier/'record.json'), rid
        sources = []
        for fragment in binding_input[rid]['fragments']:
            matches = []
            for f in fragment['matching_files']:
                path = FROZEN/f
                hit = locate(path.read_text(encoding='utf-8'),fragment['excerpt_fragment'])
                assert hit,(rid,f)
                matches.append({'path':relative(path),'packaged_lines':hit,'sha256':digest(path)})
            assert matches,rid
            sources.append({'quote':fragment['excerpt_fragment'], 'matches':matches})
        h = attributions.get(rid)
        hf = h['historical_fields'] if h else {}
        # 060's repaired source is the task writer, not the receiving solver.
        author = hf.get('artifact_author_model') if rid!='060' else None
        decision = hf.get('decision_model') if rid!='060' else None
        fresh_model = fresh_models.get(rid)
        if fresh_model:
            author=fresh_model['artifact_author_model'];decision=fresh_model['decision_model']
        gaps=[]
        if not author:gaps.append('model_author_not_confirmed_for_current_error')
        if rid=='060' and not fresh_model:gaps.append('historical_model_attribution_needs_rebinding_to_task_writer')
        if not r['historical_events']:gaps.append('no_event_timestamp_in_frozen_record')
        if not r['visible_reasoning']['anchors']:gaps.append('no_linked_visible_reasoning_anchor')
        checks=[{'result_file':f,'index':i,'description':x['description'],'scope':x['scope'],
                 'kind':'certificate_bookkeeping' if x['description']=='Archived rank-certificate internal consistency' else 'local_mathematical_check'}
                for f,xs in check_sets for i,x in enumerate(xs) if rid in x['records']]
        if not checks:gaps.append('full_witness_not_freshly_computed')
        if rid=='066':gaps.append('historical_temporary_assignment_deleted_by_original_reviewer')
        if rid=='050':gaps.append('full_rank_replay_external_matrix_and_group_fixtures_not_bundled')
        if rid=='052':gaps.append('full_contraction_minor_replay_not_run')
        history=read(dossier/'history/source_record.json')
        material_links=[]
        for m in read(dossier/'materials.json'):
            path=dossier/m['file']; assert path.is_file() and digest(path)==m['sha256']
            material_links.append({'path':relative(path),'sha256':m['sha256'],'kind':m['kind']})
        reasoning_membership = ('error_visible' if rid in ['022','025','032','033','035','036','037','038','040','043','075']
            else 'reasoning_output_discrepancy' if rid=='042' else 'not_in_12_record_paper_subset')
        record = {'schema_version':'1.0.0','record_id':rid,'legacy_id':r['adjudication']['prior_inventory_key'],
            'problem_id':problem_ids[r['problem']], 'problem':r['problem'],'admission':'included',
            'collection_context':r['collection_context'],'summary':r['summary'],
            'original':{**r['original'],'source_bindings':sources},
            'witness':{**r['witness'],'document':relative(dossier/'witness.md'),'fresh_checks':checks},
            'classification':{'version':'yoshida-level1-v3-20260923','categories':c['categories'],
                'boundary_note_zh':c['boundary_note_zh'], 'application_note_zh':c['application_note_zh'],
                'primary_logic_subtype':None if not subtype else {k:subtype[k] for k in ['primary_subtype','label_zh','rationale_zh','mapping_status']}},
            'provenance':{'frozen_record':relative(dossier/'record.json'),'frozen_record_sha256':digest(dossier/'record.json'),
                'materials':material_links,'historical_events':r['historical_events'],
                'historical_material_context':relative(dossier/'history/source_record.json')},
            'model_attribution':{'artifact_author_model':author,'decision_model':decision,
                'basis':fresh_model['basis'] if fresh_model else 'historical_source_annotation' if h else 'unavailable_in_imported_annotation',
                'evidence_document':'supplemental/model_evidence_20261005.json' if fresh_model else 'supplemental/historical_attributions.json' if h else None,
                'evidence_record_id':rid if h or fresh_model else None,
                'model_evidence':'See exact source-event metadata or UI excerpt in evidence_document.' if fresh_model else hf.get('model_evidence'),
                'attribution_limit':fresh_model['limitation'] if fresh_model else hf.get('attribution_limit'),
                'fresh_model_identification':bool(fresh_model)},
            'task_context':{'description':r['original']['context'],'basis':'frozen_original_context','full_original_prompt_not_asserted':True},
            'time_evidence':{'original_locator':r['original']['locator'],
                'events':r['historical_events'],'earliest_error_timestamp_not_inferred':True},
            'visible_reasoning':{**r['visible_reasoning'],'paper_subset':reasoning_membership},
            'paper_mapping':{'baseline':'paper/main.tex','problem_table_line':next(x['paper_table_line'] for x in problem_rows if x['name']==r['problem']),
                'category_sections': [{'I':'sec:problem-understanding','II':'sec:concept-knowledge','III':'sec:arithmetic-algebra','IV':'sec:logical-reasoning','V':'sec:error-classification'}[x['category_id']] for x in c['categories']],
                'explicit_examples':{'001':['recordformat'],'018':['ex:matrix-product-order'],'019':['ex:swap-invariance'],'042':['ex:reasoning-range'],'048':['fig:overview(a)'],'050':['ex:projected-kernel'],'060':['ex:omitted-gap-condition'],'075':['ex:reasoning-orbit']}.get(rid,[]),
                'reasoning_evidence':'audit/reasoning_alignment.json' if reasoning_membership!='not_in_12_record_paper_subset' else None},
            'audit':{'audit_date':'2026-10-05','source_binding':'PASS','source_hashes':'PASS',
                'classification_join':'PASS','mathematical_review':'scoped_witness_read_and_compared',
                'full_independent_mathematical_certification':False,'fresh_computational_check_count':len(checks),
                'gaps':gaps,'source_record_verification_limit':r['verification_limit']}}
        records.append(record)
        audits.append({'record_id':rid,'legacy_id':record['legacy_id'],'problem_id':record['problem_id'],
            'categories':[x['category_id'] for x in c['categories']],
            'logic_subtype':None if not subtype else subtype['primary_subtype'],
            'fragment_count':len(sources),'source_file_count':len(material_links),
            'model_author':author,'fresh_check_count':len(checks),'gaps':gaps,
            'review_note':r['adjudication']['rationale_zh'],'witness_scope':r['witness']['scope']})
    (ROOT/'data/records.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
    write(ROOT/'index.json',[{'record_id':r['record_id'],'problem':r['problem'],'summary':r['summary'],'evidence':r['witness']['document']} for r in records])
    write(ROOT/'audit/record_audit.json',audits)
    stats={'records':len(records),'problems':len(problem_rows),
        'category_counts':dict(Counter(x['category_id'] for r in records for x in r['classification']['categories'])),
        'assignments':sum(len(r['classification']['categories']) for r in records),
        'multilabel_records':[r['record_id'] for r in records if len(r['classification']['categories'])>1],
        'logic_subtypes':dict(Counter(r['classification']['primary_logic_subtype']['primary_subtype'] for r in records if r['classification']['primary_logic_subtype'])),
        'linked_visible_reasoning':sum(bool(r['visible_reasoning']['anchors']) for r in records),
        'paper_reasoning_subset':dict(Counter(r['visible_reasoning']['paper_subset'] for r in records)),
        'model_author_null_ids':[r['record_id'] for r in records if r['model_attribution']['artifact_author_model'] is None],
        'records_with_fresh_local_checks':sum(bool(r['witness']['fresh_checks']) for r in records),
        'records_with_fresh_mathematical_checks':sum(any(x['kind']=='local_mathematical_check' for x in r['witness']['fresh_checks']) for r in records),
        'source_files_in_frozen_layer':len([p for p in FROZEN.rglob('*') if p.is_file()]),
        'privacy':'private_only','readiness':'audited_working_corpus_with_explicit_limitations'}
    stats['logic_label_percentage']=round(100*stats['category_counts']['IV']/stats['assignments'],1)
    stats['logic_record_percentage']=round(100*stats['category_counts']['IV']/stats['records'],1)
    write(ROOT/'data/statistics.json',stats)
    excluded=[]
    for r in lines(FROZEN/'audit/all_77.jsonl'):
        if r['admission']=='excluded':
            excluded.append({'record_id':r['record_id'],'legacy_id':r['adjudication']['prior_inventory_key'],
                'problem':r['problem'],'reason_zh':r['adjudication']['rationale_zh'],
                'evidence':relative(FROZEN/'audit/excluded'/r['record_id']/'witness.md')})
    write(ROOT/'data/excluded.json',excluded)
    rows=['# Per-record audit, 2026-10-05','', 'All 65 original/witness pairs were read and compared. PASS below refers to source/format/classification binding. Fresh checks cover only their stated local scopes.','',
          '| ID | Legacy ID | Categories | Logic subtype | Fresh local checks | Gaps / limits |','|---|---|---|---|---:|---|']
    for a in audits:
        rows.append(f"| [{a['record_id']}](../{next(r['witness']['document'] for r in records if r['record_id']==a['record_id'])}) | {a['legacy_id']} | {', '.join(a['categories'])} | {a['logic_subtype'] or 'N/A'} | {a['fresh_check_count']} | {'; '.join(a['gaps']) or 'Full witness certification not asserted'} |")
    (ROOT/'docs/RECORD_AUDIT.md').write_text('\n'.join(rows)+'\n')
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__': build()
