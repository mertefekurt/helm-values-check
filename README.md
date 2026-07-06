# Helm Values Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Helm Values Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-4b5563?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-2563eb?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16a34a?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-dc2626?style=flat-square)

Audit Helm values for insecure defaults and missing production overrides.

## The short version

`helm-values-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `default-password` | high | default password detected |
| `tls-disabled` | medium | TLS is disabled |
| `single-replica` | low | single replica configured |

## Usage

```bash
python -m pip install -e ".[dev]"
helm-values-check examples/sample.txt
helm-values-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m helm_values_check --help
```
