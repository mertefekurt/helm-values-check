# helm-values-check

> Audit Helm values for insecure defaults and missing production overrides.

## Spec sheet Overview

Audit Helm values for insecure defaults and missing production overrides. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 7

Accepts Helm values text. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 7

```bash
python -m pip install -e ".[dev]"
helm-values-check examples/sample.txt
helm-values-check examples/sample.txt --json --fail-on medium
python -m helm_values_check --help
```

## Rule Surface 7

| Rule | Severity | Meaning |
|---|---:|---|
| `default-password` | high | default password detected |
| `tls-disabled` | medium | TLS is disabled |
| `single-replica` | low | single replica configured |

## Validation Notes 7

```bash
ruff check .
pytest
python -m helm_values_check --help
```

Example risky input:

```text
replicaCount 1 ingress tls false adminPassword changeme
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
