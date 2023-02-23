# Users Management
# Read the item for User by Partition Key(emailAddress)
# event contains "emailAddress"

# API method: POST method
'''
N (string) --
An attribute of type Number. For example:

"N": "123.45"
Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. 
However, DynamoDB treats them as number type attributes for mathematical operations.
'''
import boto3
from botocore.exceptions import ClientError
import json

def lambda_handler(event, context):
    if event:
        print("This is a POST request for user read items")

        client = boto3.client('dynamodb', region_name = 'us-east-1')

        emailAddress = event['Email_address']    # 'S':string

        try:
            results = client.get_item(
                TableName = 'BankSystem',
                Key = {
                        'EmailAddress': {'S': str(emailAddress)},
                        'StaticSortKey': {'S': str('bussiness_card')}
                    }
                )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print(results)

        response = {
            'statusCode': 200,
            'body': json.dumps(results["Item"])
            }

        return response