from __future__ import annotations

from helm_values_check.models import Rule

PROJECT_NAME = 'helm-values-check'
SUMMARY = 'Audit Helm values for insecure defaults and missing production overrides.'
SAMPLE_RISK = 'replicaCount 1 ingress tls false adminPassword changeme'
SAMPLE_CLEAN = 'replicaCount 3 ingress tls true secret existingSecret'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='default-password',
        severity='high',
        pattern='(adminPassword|password)\\s+(changeme|admin|password)',
        message='default password detected',
        recommendation='use a secret reference',
    ),
    Rule(
        code='tls-disabled',
        severity='medium',
        pattern='tls\\s+false',
        message='TLS is disabled',
        recommendation='enable TLS for ingress',
    ),
    Rule(
        code='single-replica',
        severity='low',
        pattern='replicaCount\\s+1',
        message='single replica configured',
        recommendation='confirm availability requirements',
    ),
)
