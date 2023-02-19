# Admin Management
# Read the whole table by Scan

# Restful: GET Method

# Return ??? how to return the whole table 
# #TODO


import boto3
import json

def lambda_handler(event, context):
    if event:
        print("This is a GET request for Admin read table")
        client = boto3.client('dynamodb', region_name = 'us-east-1')

        results = client.scan(TableName = 'BankSystem')
        print(results)

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