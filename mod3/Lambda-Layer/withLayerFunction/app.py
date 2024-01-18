import json
import boto3
import botocore


def lambda_handler(event, context):
    # TODO implement
    print(f'boto3 version: {boto3.__version__}')
    print(f'botocore version: {botocore.__version__}')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
