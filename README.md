# Module ECR Permission

This module is useful to add permission to an ECR repository created via cross-region replication.

Currently, the cross-region can replicate the images, but not the repository policy, this module uses Event Bridge to monitor the creation of a new ECR repository and uses a lambda to add a new policy to it.

This module will apply a policy that allows any account inside the AWS Organizations to access it.

<br />

## Features

Add permission to allow any account inside an AWS Organization to get the image from an ECR repository.

<br />

### Terraform providers used:
- [AWS](https://registry.terraform.io/providers/hashicorp/aws/4.16.0)

### Terraform resources used:
- [CloudWatch Metric Alarm](https://registry.terraform.io/providers/hashicorp/aws/3.74.0/docs/resources/cloudwatch_metric_alarm)
- [Datadog monitor](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/monitor)
- [IAM policy](https://registry.terraform.io/providers/hashicorp/aws/3.74.0/docs/resources/iam_policy)
- [Subscribing to SNS topics](https://registry.terraform.io/providers/hashicorp/aws/3.74.0/docs/resources/sns_topic_subscription)
- [Policy for SQS Queue](https://registry.terraform.io/providers/hashicorp/aws/3.74.0/docs/resources/sqs_queue_policy)
- [SQS Queue](https://registry.terraform.io/providers/hashicorp/aws/3.74.0/docs/resources/sqs_queue)



# Terraform Docs

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 4.16.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 4.9.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_eventbridge_ecr"></a> [eventbridge\_ecr](#module\_eventbridge\_ecr) | terraform-aws-modules/eventbridge/aws | v1.14.0 |
| <a name="module_lambda_trigger_ecr"></a> [lambda\_trigger\_ecr](#module\_lambda\_trigger\_ecr) | terraform-aws-modules/lambda/aws | 3.2.1 |

## Resources

| Name | Type |
|------|------|
| [aws_iam_policy.lambda_trigger_ecr](https://registry.terraform.io/providers/hashicorp/aws/4.16.0/docs/resources/iam_policy) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/4.16.0/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.lambda_trigger_ecr](https://registry.terraform.io/providers/hashicorp/aws/4.16.0/docs/data-sources/iam_policy_document) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/4.16.0/docs/data-sources/region) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_org_id"></a> [org\_id](#input\_org\_id) | n/a | `any` | n/a | yes |
| <a name="input_tags"></a> [tags](#input\_tags) | n/a | `any` | `null` | no |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
