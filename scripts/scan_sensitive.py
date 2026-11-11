"""Offline deterministic scan. Prints locations and digests, never secret values."""
import re,json,sys
from common import ROOT, digest, write

PATTERNS={
    'github_token':r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b',
    'api_key':r'\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}\b',
    'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'aws_key':r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'credential_url':r'https?://[^\s/:]+:[^\s/@]+@',
    'secret_assignment':r'''(?i)(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[=:]\s*["']([A-Za-z0-9_./+\-=]{20,})["']''',
    'email':r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    'user_path':r'(?:/Users/|/home/|C:\\Users\\)[A-Za-z0-9._-]+',
    'private_ip':r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3})\b',
}

def files():
    for f in sorted(ROOT.rglob('*')):
        if f.is_file() and not any(p in {'.git','.venv','__pycache__'} for p in f.relative_to(ROOT).parts):
            yield f

def scan():
    findings=[];count=0
    for f in files():
        if f.name in {'privacy_scan.json','manifest.json'}:continue
        count+=1
        if f.suffix=='.pdf':
            from pypdf import PdfReader
            text='\n'.join(p.extract_text() or '' for p in PdfReader(f).pages)
        else:
            try:text=f.read_text(encoding='utf-8')
            except UnicodeDecodeError:continue
        rel=str(f.relative_to(ROOT))
        for kind,pat in PATTERNS.items():
            for m in re.finditer(pat,text):
                line=text.count('\n',0,m.start())+1
                allowed=(kind=='user_path' and rel=='source_layers/dataset-witness-repaired-v1.1-20260922/records/019/original/M01-WHGAP-P1-019faab6.jsonl.readable.md' and line==1383)
                # Public LaTeX package maintainer email attribution is not a credential.
                disposition='historical_source_path_inert_not_runtime_dependency' if allowed else 'REVIEW_REQUIRED'
                findings.append({'path':rel,'line':line,'kind':kind,'file_sha256':digest(f),'disposition':disposition})
    unresolved=[x for x in findings if x['disposition']=='REVIEW_REQUIRED']
    return {'status':'PASS' if not unresolved else 'REVIEW_REQUIRED','scanned_files':count,
        'findings':findings,'unresolved_findings':len(unresolved),
        'scope':'Recognizable credential, secret-assignment, email, local-user-path and private-IP patterns across UTF-8 files and extracted PDF text. This is a bounded scan, not a proof that every possible secret format is absent. Evidence folders contain research-scoped historical context; original author identity is not expanded from path names.'}

if __name__=='__main__':
    result=scan()
    if '--save' in sys.argv:write(ROOT/'audit/privacy_scan.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['status']=='PASS' else 1)
