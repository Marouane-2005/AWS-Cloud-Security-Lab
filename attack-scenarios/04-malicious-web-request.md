# Scenario 4 — Malicious web request (SQLi/XSS)

## Context

What was done and why (e.g. sent a basic SQL injection payload in a query
string to the ALB's public URL).

## Attack simulation

Payload used and how it was sent (e.g. `curl` with a crafted query string).

## Detection

Which AWS WAF managed rule matched (e.g. Core Rule Set, Known Bad Inputs),
timestamp. Include a screenshot from `screenshots/detections/`.

## Investigation

WAF logs reviewed (via CloudWatch Logs or the S3 log destination): request
details, matched rule, action taken (block/count).

## Remediation

Confirm the request was blocked as expected; adjust the Web ACL rule set
or add a custom rule if a gap was found.

## Lessons learned

One or two sentences on what this confirms about the application-layer
detection coverage.
