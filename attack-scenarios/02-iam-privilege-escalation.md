# Scenario 2 — IAM privilege escalation

## Context

What was done and why (e.g. created an IAM user and attached the
`AdministratorAccess` managed policy).

## Attack simulation

Steps taken to reproduce the escalation.

## Detection

Which service surfaced this (CloudTrail event / Security Hub finding),
finding ID, timestamp. Include a screenshot from `screenshots/detections/`.

## Investigation

CloudTrail event details: which API call, which principal, source IP,
user agent, and how the privilege change was confirmed.

## Remediation

Steps taken to revert the change (detach the policy, disable/remove the
user if simulated as a compromised credential).

## Lessons learned

One or two sentences on what this confirms about the detection pipeline.
