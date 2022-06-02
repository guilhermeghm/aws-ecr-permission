import json, boto3, os, logging

def lambda_handler(event, context):
    # Logging configuration
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.getLogger("boto3").setLevel(logging.WARNING)
    logging.getLogger("botocore").setLevel(logging.WARNING)
    logger.debug('Incoming Event')
    logger.debug(event)

    # Variables
    org_id = os.environ.get('org_id')
    repository_name = event['detail']['requestParameters']['repositoryName']

    logger.info('The respository name is: ' + repository_name)

    # Boto3 client
    ecr_connection = boto3.client('ecr')

    # ECR Policy
    policy = {
        "Version":"2012-10-17",
        "Statement":[
            {
                "Sid":"ECR Org Access",
                "Effect":"Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action":[
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:BatchGetImage",
                    "ecr:GetDownloadUrlForLayer",
                    ],
                "Condition":{
                    "StringLike":{
                    "aws:PrincipalOrgID":org_id
                    },
                }
            }
        ]
    }

    # Applying the policy
    response = ecr_connection.set_repository_policy(
        repositoryName=repository_name,
        policyText=json.dumps(policy),
    )

    logger.info('My response is: ' + str(response))

    return json.dumps(response, default=str)
