# Scenario 3 — Network port scanning

## Context

What was done and why (e.g. ran an external port scan against the public
EC2 instance's IP address).

## Attack simulation

Tool used (e.g. `nmap`), command run, source of the scan.

## Detection

GuardDuty finding type (`Recon:EC2/PortProbeUnprotectedPort` or similar),
severity, timestamp. Include a screenshot from `screenshots/detections/`.

## Investigation

VPC Flow Logs reviewed to confirm the scan pattern (source IP, ports
probed, rejected connections).

## Remediation

Steps taken (confirm no port was actually left open, tighten security
group if needed).

## Automated response

If this scenario was used to test the EventBridge -> SNS/Lambda pipeline
(Phase 5), document here: alert received, instance quarantined, screenshot
from `screenshots/incident-response/`.

## Lessons learned

One or two sentences on what this confirms about the detection pipeline.
