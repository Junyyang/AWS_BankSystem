# Users Management
# Read the item for User by Partition Key(emailAddress)
# event contains "emailAddress"

# API method: POST method

'''
Test Json
[
    {
        "UserID": "USERID#2"
    }
]
'''


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
        postINFO = json.loads(event['body'])[0]
        userID = postINFO['UserID']    # 'S':string

        try:
            results = client.get_item(
                TableName = 'BussinessCard',
                Key = {
                        'PK': {'S': str('USER')},
                        'SK': {'S': str(userID)}
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