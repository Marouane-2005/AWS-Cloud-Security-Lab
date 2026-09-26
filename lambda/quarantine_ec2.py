"""
Quarantine EC2 Lambda function.

Triggered by an EventBridge rule matching high-severity GuardDuty or
Security Hub findings. Identifies the affected EC2 instance and replaces
its security groups with an isolated "quarantine" security group that has
no inbound or outbound rules, containing the instance without stopping it
(preserving volatile evidence for later investigation).

Expected environment variables:
- QUARANTINE_SG_ID: the security group ID to apply when isolating an instance
"""

import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2_client = boto3.client("ec2")

QUARANTINE_SG_ID = os.environ.get("QUARANTINE_SG_ID")


def extract_instance_id(event: dict) -> str | None:
    """Pull the affected EC2 instance ID out of a GuardDuty or Security Hub
    finding, whichever shape the incoming EventBridge event has."""
    detail = event.get("detail", {})

    # GuardDuty finding shape
    resource = detail.get("resource", {})
    instance_details = resource.get("instanceDetails", {})
    if instance_details.get("instanceId"):
        return instance_details["instanceId"]

    # Security Hub finding shape (ASFF)
    findings = detail.get("findings", [])
    for finding in findings:
        for resource in finding.get("Resources", []):
            if resource.get("Type") == "AwsEc2Instance":
                resource_id = resource.get("Id", "")
                # Security Hub ARNs look like: arn:aws:ec2:region:account:instance/i-xxxxx
                if "instance/" in resource_id:
                    return resource_id.split("instance/")[-1]

    return None


def quarantine_instance(instance_id: str) -> None:
    if not QUARANTINE_SG_ID:
        raise RuntimeError("QUARANTINE_SG_ID environment variable is not set")

    logger.info("Quarantining instance %s with security group %s", instance_id, QUARANTINE_SG_ID)

    ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[QUARANTINE_SG_ID],
    )

    ec2_client.create_tags(
        Resources=[instance_id],
        Tags=[{"Key": "security-status", "Value": "quarantined"}],
    )


def handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    instance_id = extract_instance_id(event)
    if not instance_id:
        logger.warning("No EC2 instance ID found in event, nothing to quarantine")
        return {"status": "skipped", "reason": "no_instance_id"}

    quarantine_instance(instance_id)

    return {"status": "quarantined", "instance_id": instance_id}
