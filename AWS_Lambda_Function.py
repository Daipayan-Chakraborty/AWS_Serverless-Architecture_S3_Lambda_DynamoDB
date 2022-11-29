import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
student_table = dynamodb.Table('students')

def lambda_handler(event, context):
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    file_object = s3_client.get_object(Bucket=source_bucket_name, Key=file_name)
    print('file_object :', file_object)
    file_content = file_object['Body'].read().decode("utf-8")
    print('file_content :', file_content)
    students = file_content.split("\n")
    print("students :", students)

    for i in students:
        data = i.split(",")
        if len(data) > 1:
            print(data[0])
            print(data[1])
            print(data[2])
            student_table.put_item(
                Item={
                    "id": data[0],
                    "name": data[1],
                    "marks": data[2]
                }
            )
