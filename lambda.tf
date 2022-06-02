data "aws_iam_policy_document" "lambda_trigger_ecr" {
  version = "2012-10-17"
  statement {
    effect = "Allow"
    actions = [
      "ecr:SetRepositoryPolicy",
      "ecr:GetRepositoryPolicy",
    ]
    resources = ["arn:aws:ecr:*:*:repository/*"]
  }
}

resource "aws_iam_policy" "lambda_trigger_ecr" {
  name        = "lambda_aws_trigger_ecr"
  path        = "/"
  description = "IAM policy to allow Lambda to set ECR permissions."
  policy      = data.aws_iam_policy_document.lambda_trigger_ecr.json
  tags        = var.tags
}

module "lambda_trigger_ecr" {
  source             = "terraform-aws-modules/lambda/aws"
  version            = "3.2.1"
  function_name      = "lambda_aws_trigger_ecr"
  description        = "Lambda to add permissions to a new ECR repository."
  handler            = "lambda_ecr.lambda_handler"
  runtime            = "python3.9"
  attach_policies    = true
  publish            = true
  number_of_policies = 1
  policies           = [aws_iam_policy.lambda_trigger_ecr.arn]

  environment_variables = {
    org_id = var.org_id
  }

  allowed_triggers = {
    ECR = {
      principal  = "events.amazonaws.com"
      source_arn = format("arn:aws:events:%s:%s:rule/ecr-permission-rule", data.aws_region.current.name, data.aws_caller_identity.current.account_id)
    }
  }

  source_path = format("%s/code", path.module)

  tags = var.tags
}
