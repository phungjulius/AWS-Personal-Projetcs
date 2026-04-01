import json
import boto3

sns = boto3.client('sns')

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):
    errors = []

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        for line in content.splitlines():
            if "ERROR" in line:
                errors.append(line)

    if errors:
        message = "Errors found:\n" + "\n".join(errors[:5])

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Log Alert"
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed')
    }