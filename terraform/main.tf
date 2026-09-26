terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Modules are wired up progressively as each phase of the roadmap is built.
# Phase 1:
# module "networking" {
#   source = "./networking"
# }

# Phase 1:
# module "iam" {
#   source = "./iam"
# }

# Phase 2:
# module "compute" {
#   source = "./compute"
# }

# Phase 3:
# module "logging" {
#   source = "./logging"
# }

# Phase 3:
# module "security" {
#   source = "./security"
# }

# Phase 5:
# module "incident_response" {
#   source = "./incident-response"
# }
