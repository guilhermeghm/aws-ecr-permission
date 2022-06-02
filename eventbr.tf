module "eventbridge_ecr" {
  source  = "terraform-aws-modules/eventbridge/aws"
  version = "v1.14.0"

  create_bus  = false
  create_role = false

  rules = {
    ecr-permission = {
      description = "Event Rule for ECR, trigger a Lambda to add permission in the ECR repository."
      event_pattern = jsonencode({
        "source" : ["aws.ecr"],
        "detail-type" : ["AWS API Call via CloudTrail"],
        "detail" : {
          "eventSource" : ["ecr.amazonaws.com"],
          "eventName" : ["CreateRepository"]
        }
      })
      enabled = true
    }
  }

  targets = {
    ecr-permission = [
      {
        name = "lambda-trigger-ecr"
        arn  = module.lambda_trigger_ecr.lambda_function_arn
      }
    ]
  }
  tags = var.tags
}
