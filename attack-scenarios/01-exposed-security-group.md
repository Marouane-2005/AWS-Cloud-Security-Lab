# Scenario 1 — Exposed security group

## Context

What was done and why (e.g. opened port 22 on the public EC2 security group
to `0.0.0.0/0`).

## Attack simulation

Steps taken to reproduce the misconfiguration.

## Detection

Which service surfaced this (AWS Config rule / Security Hub CIS control),
finding ID, timestamp. Include a screenshot from `screenshots/detections/`.

## Investigation

Logs reviewed (CloudTrail event for the security group change, who made it,
from which IP/role) and how they were cross-referenced.

## Remediation

Steps taken to close the exposure (restrict the security group rule).

## Lessons learned

One or two sentences on what this confirms about the detection pipeline.
