# Reproducible local checks

Use Python 3.10 or later with SymPy. From the release root:

```sh
python3 checks/check_witnesses.py
```

Default execution is read-only. `--write-results` explicitly regenerates the
results file and will intentionally invalidate a frozen checksum manifest.
`witness_checks.json` is the recorded result. Every check states its scope;
some establish an exclusion or a limited algebraic property rather than a
positive error. Passing all checks does not certify entire historical proofs
or imply that all large enumerations have been repeated.
