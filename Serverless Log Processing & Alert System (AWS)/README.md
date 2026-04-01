# Serverless Log Processing & Alert System (AWS)

## Overview
This project demonstrates a serverless architecture for processing application logs using AWS services.

When a log file is uploaded to S3, an AWS Lambda function is triggered to analyze the logs and detect errors. If issues are found, notifications are sent via SNS.

## Architecture
- Amazon S3 (log storage)
- AWS Lambda (processing)
- Amazon SNS (alerting)
- CloudWatch (logging)

## Workflow
1. Logs are uploaded to S3
2. S3 triggers Lambda function
3. Lambda processes logs and extracts errors
4. Alerts are sent via SNS
5. Logs are stored in CloudWatch

## Technologies
- AWS Lambda
- Amazon S3
- Amazon SNS
- Python (boto3)

## Project Structure
- `lambda/` → processing logic
- `sample_logs/` → example input
- `scripts/` → setup instructions

## AWS Setup Steps

1. Created an S3 bucket to store log files  
2. Created an SNS topic and subscribed email for alerts  
3. Created an IAM role with permissions for Lambda  
4. Implemented a Lambda function to process logs  
5. Configured S3 trigger to invoke Lambda on upload  
6. Verified system by uploading logs and receiving alerts

## What I Learned
- Event-driven architectures in AWS
- Serverless computing using Lambda
- Automating log analysis workflows
- Integrating AWS services (S3, Lambda, SNS)

## Future Improvements
- Add severity levels (WARNING, CRITICAL)
- Store results in DynamoDB
- Add dashboard for visualization

## Architecture Diagram

```mermaid
graph TD
    A[Application / Logs] -->|Upload Logs| B[S3 Bucket]

    B -->|Trigger Event| C[AWS Lambda Function]

    C --> D[Process Logs]
    D --> E[Extract Errors / Metrics]

    E -->|Send Alert| F[SNS Topic]
    F --> G[Email Notification]

    C --> H[CloudWatch Logs]