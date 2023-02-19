# Admin Management
# Delete table for Bussiness Card

# Restful: GET Method


import boto3

def lambda_handler(event, context):
    if event:
        print("This is a GET request")
        client = boto3.client('dynamodb', region_name = 'us-east-1')

        results = client.delete_table(
            TableName='BankSystem',
            )
        print(results)


        response = {
            'statusCode': 200,
            'body': 'successfully delete table {tablename}!'.format(tablename = 'BankSystem'),
        }
        
        return response