import json, boto3, os, logging, sys


def lambda_handler(event, context):
    # Logging configuration
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.getLogger("boto3").setLevel(logging.WARNING)
    logging.getLogger("botocore").setLevel(logging.WARNING)
    logger.debug('Incoming Event')
    logger.debug(event)

    # Function variables
    backup_vault_name = event['detail']['destinationBackupVaultArn'].split(':')[6]
    lifecycle_value = 'CalculatedLifecycle'
    logger.info('Backup source account: ' + event['account'])
    logger.info('Recovery Point ARN to be copied: ' + event['detail']['destinationRecoveryPointArn'])

    # Environment variables
    destination_region = os.environ.get('destination_region')
    destination_vault = str(os.environ.get('destination_vault'))
    logger.info('Sending backup to the following AWS Region: ' + destination_region)
    role_name = os.environ.get('role_name')

    # Boto3 client
    backup_connection = boto3.client('backup')

    # Boto3 call to retrieve recovery point retention/lifecycle value
    recovery_point = backup_connection.describe_recovery_point(
        BackupVaultName=backup_vault_name,
        RecoveryPointArn=event['detail']['destinationRecoveryPointArn']
    )
    logger.debug('Recovery Point Information')
    logger.debug(recovery_point)

    # If value is found, it will be passed to the start copy job boto3 call
    try:
        if lifecycle_value in recovery_point:
            response = backup_connection.start_copy_job(
                RecoveryPointArn=event['detail']['destinationRecoveryPointArn'],
                SourceBackupVaultName=backup_vault_name,
                DestinationBackupVaultArn=destination_vault,
                IamRoleArn=role_name,
                Lifecycle={'DeleteAfterDays': int(recovery_point['Lifecycle']['DeleteAfterDays'])}
            )

        # Else, value has not been defined and will not be defined in start copy job boto3 call
        else:
            response = backup_connection.start_copy_job(
                RecoveryPointArn=event['detail']['destinationRecoveryPointArn'],
                SourceBackupVaultName=backup_vault_name,
                DestinationBackupVaultArn=destination_vault,
                IamRoleArn=role_name
            )
    except Exception as e:
        logger.error(str(e))
        sys.exit('Exiting as response was not returned...')

    logger.info('AWS Backup Copy Job ID: ' + response['CopyJobId'])
    return json.dumps(response, default=str)
