# aws-ecr-permission


<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 4.9.0 |

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
| [aws_iam_policy.lambda_trigger_ecr](https://registry.terraform.io/providers/hashicorp/aws/4.9.0/docs/resources/iam_policy) | resource |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/4.9.0/docs/data-sources/caller_identity) | data source |
| [aws_iam_policy_document.lambda_trigger_ecr](https://registry.terraform.io/providers/hashicorp/aws/4.9.0/docs/data-sources/iam_policy_document) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/4.9.0/docs/data-sources/region) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_org_id"></a> [org\_id](#input\_org\_id) | n/a | `any` | n/a | yes |
| <a name="input_tags"></a> [tags](#input\_tags) | n/a | `any` | `null` | no |

## Outputs

No outputs.
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
