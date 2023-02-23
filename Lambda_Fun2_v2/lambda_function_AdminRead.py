# Admin Management
# Read all the items

# Restful: GET Method


import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    if event:
        print("This is a GET request for Admin read table")
        dynamodb = boto3.resource(
            'dynamodb', 
            region_name='us-east-1')
        table = dynamodb.Table('BussinessCard')

        results = table.query(
            IndexName="Readall",
            Select = 'ALL_PROJECTED_ATTRIBUTES',
            KeyConditionExpression=Key('PK').eq('USER'),
            ScanIndexForward = True
        )
        print(results['Items'])

        if results["Items"]:
            response = {
                'statusCode': 200,
                'body': json.dumps(results["Items"])
                }
        else:
            response = {
                'statusCode': 404,
                'body': "No Existing Table"
                }
        return response