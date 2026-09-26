variable "aws_region" {
  description = "AWS region where the lab is deployed"
  type        = string
  default     = "eu-west-3"
}

variable "project_name" {
  description = "Name used to tag and prefix all resources"
  type        = string
  default     = "aws-cloud-security-lab"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.10.0.0/16"
}

variable "alert_email" {
  description = "Email address that receives SNS security alerts"
  type        = string
  sensitive   = true
}
