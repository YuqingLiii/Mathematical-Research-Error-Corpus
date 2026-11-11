"""Re-run reviewed frozen checks without writing into the frozen dataset.

The only compatibility transformation replaces integer x.bit_count() with
bin(x).count('1') on Python 3.9. All operands in this checker are nonnegative.
Original code and archived result hashes remain untouched.
"""
import ast, contextlib, io, json, sys
from common import ROOT, FROZEN, digest, write

def run():
    source = FROZEN/'checks/check_witnesses.py'
    tree = ast.parse(source.read_text(), filename=str(source))
    replaced = []
    class Compatibility(ast.NodeTransformer):
        def visit_Call(self, node):
            self.generic_visit(node)
            if (isinstance(node.func, ast.Attribute) and node.func.attr == 'bit_count'
                    and not node.args and not node.keywords and sys.version_info < (3, 10)):
                replaced.append(node.lineno)
                return ast.copy_location(ast.Call(
                    func=ast.Attribute(value=ast.Call(func=ast.Name(id='bin', ctx=ast.Load()),
                        args=[node.func.value], keywords=[]), attr='count', ctx=ast.Load()),
                    args=[ast.Constant('1')], keywords=[]), node)
            return node
    tree = ast.fix_missing_locations(Compatibility().visit(tree))
    ns = {'__file__': str(source), '__name__': '__audit_checker__'}
    prior = sys.argv
    try:
        sys.argv = [str(source)]
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(tree, str(source), 'exec'), ns)
    finally:
        sys.argv = prior
    checks = ns['results']
    archived = json.loads((FROZEN/'checks/witness_checks.json').read_text())
    assert len(checks) == len(archived) == 42, 'A fixture-dependent check may have been skipped'
    assert [(c['records'], c['description']) for c in checks] == [(c['records'], c['description']) for c in archived]
    positive = {r['record_id'] for r in json.loads((FROZEN/'index.json').read_text())}
    touched = {r for c in checks for r in c['records']}
    import sympy
    return {'status': 'PASS', 'python': sys.version.split()[0], 'sympy': sympy.__version__,
        'script_sha256': digest(source), 'compatibility_bit_count_lines': replaced,
        'checks': checks, 'check_count': len(checks),
        'included_records_touched': sorted(touched & positive),
        'excluded_records_touched': sorted(touched-positive),
        'included_records_without_fresh_computational_check': sorted(positive-touched),
        'interpretation': 'Local scoped computations only; neither all 65 full witnesses nor all archived large runs were re-executed.'}

if __name__ == '__main__':
    result = run()
    if '--save' in sys.argv:
        write(ROOT/'audit/witness_execution.json', result)
    print(json.dumps({k:v for k,v in result.items() if k != 'checks'}, indent=2))
