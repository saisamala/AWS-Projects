# Project Name - S3 Event Triggering with Lambda and SNS

## Overview

This project aims to demonstrate how to set up an AWS S3 event trigger that invokes a Lambda function, which in turn sends an email using SNS (Simple Notification Service) topic subscriptions. The workflow is as follows:

1. When a user uploads a file to the specified S3 bucket, an S3 event is triggered.
2. The S3 event is configured to call a Lambda function automatically.
3. The Lambda function sends an email notification using the SNS topic subscriptions.


![s3-event-triggering](https://github.com/saisamala/AWS-Projects/assets/34151152/5ceb7a12-2fc9-4cda-8690-4c323f45f467)


## Setup Instructions

Follow these steps to set up the S3 event triggering project:

1. **Create an S3 Bucket:**
   - Go to the AWS S3 Management Console.
   - Click on "Create Bucket" to create a new S3 bucket.
   - Choose a unique name for your bucket, select the region, and configure other settings as needed.

2. **Create an SNS Topic:**
   - Go to the AWS SNS Management Console.
   - Click on "Create topic" and give your topic a name and display name.
   - After creating the topic, subscribe an email address to it so that notifications can be sent to it.

3. **Create a Lambda Function:**
   - Go to the AWS Lambda Management Console.
   - Click on "Create function" and choose "Author from scratch."
   - Give your function a name, select the runtime (e.g., Node.js, Python, etc.), and configure the execution role.

4. **Create an IAM Role for Lambda:**
   - Go to the AWS IAM Management Console.
   - Click on "Roles" in the left-hand sidebar, then click "Create role."
   - Select "AWS service" as the trusted entity and choose "Lambda" as the service that will use this role.
   - Attach the following policies to the role:
     - For S3 access: "AmazonS3FullAccess" or a more restricted policy that grants the necessary permissions for the specific S3 bucket you are using.
     - For SNS access: "AmazonSNSFullAccess" or a more restricted policy that allows publishing to the specific SNS topic you want to use.
   - Name the role appropriately (e.g., LambdaS3SNSTriggerRole) and create the role.

5. **Configure the Lambda Function:**
   - Back in the AWS Lambda Management Console, find the function you created.
   - Under the "Permissions" tab, click on the "Edit" button to assign the IAM role you created to the Lambda function.
   - Choose "Use an existing role" and select the IAM role you created earlier from the drop-down menu.
   - Save your changes.

6. **Write the Lambda Function Code:**
   - Use the appropriate programming language (e.g., Node.js, Python) to write the Lambda function code that sends an email using the SNS topic. You can use the sample code provided in the README for your chosen language.

7. **Configure S3 Event Trigger for Lambda:**
   - Go back to the AWS S3 Management Console and open your bucket.
   - In "Properties" tab, Under the "Event notifications", click on "Create event notifications".
   - Give your "Event name" and in "Event type" choose "All object create events".
   - Choose the destination as "Lambda function" and choose the previously created Lambda function from the drop-down menu.
   - Save your changes.

8. **Test the Setup:**
   - Upload a file to the S3 bucket you created earlier.
   - The S3 event will trigger the Lambda function, which, in turn, will send an email notification using the configured SNS topic.

## Customization and Extensibility

You can customize and extend this project based on your specific requirements. For example, you can modify the Lambda function to process the uploaded files, perform additional actions, or customize the email message. Additionally, you can explore other AWS services to enhance the functionality, such as using Amazon SES for more advanced email options or integrating with other AWS services.

## Conclusion

Congratulations! You have successfully set up an AWS S3 event triggering project using Lambda and SNS. This project demonstrates how to automate actions based on events in AWS services, and how S3 events can be used to trigger Lambda functions for various purposes, such as sending email notifications.

Feel free to reach out for any questions or support.

Happy coding!
