import boto3

def lambda_handler(event, context):
    # Extract the bucket name and object key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']


    # Email message to be sent
    email_message = f"A new file has been uploaded to S3:\n\nBucket: {bucket}\nObject Key: {key}"

    # Configure the AWS SDK to use the appropriate region
    
    sns_topic_arn = 'arn:aws:sns:us-east-1:202225588774:s3-event-trigger'
    sns_client = boto3.client('sns')

    # Publish the email notification to the specified SNS topic
    
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Subject='New S3 File Upload',
        Message=email_message
    )

    return {
        'statusCode': 200,
        'body': 'Email notification sent successfully!',
    }

