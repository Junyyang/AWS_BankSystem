# Admin Management
# Sort the item User by Attribute
# event contains "SortedBy", "Ascending"

# Restful API: POST method


import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
    if event:
        print("This is a POST request for Admin read table")

        sortedByAttri = event["SortedBy"]
        indexdict = {
            'Age': 'Age',
            'Job_title': 'JobTitle',
            'Employer': 'Employer',
            'City': 'City'
        }
        if sortedByAttri in ['Age', 'Job_title', 'Employer', 'City']:
            sortIndex = "SortBy" + indexdict[sortedByAttri]
        else:
            response = {
                'statusCode': 404,
                'body': "Not valid sorted attribute"
                }
            return response
        
        ascendStatus = event["Ascending"]

        dynamodb = boto3.resource(
            'dynamodb', 
            region_name='us-east-1')
        table = dynamodb.Table('BussinessCard')

        results = table.query(
            IndexName=sortIndex,
            Select = 'ALL_PROJECTED_ATTRIBUTES',
            KeyConditionExpression=Key('GSI1PK').eq('USER'),
            ScanIndexForward = ascendStatus
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