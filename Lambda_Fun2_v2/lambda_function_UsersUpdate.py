# Users Management
# Update the specific attribute for User by Partition Key(emailAddress)
# event contains "Email_address, Attribute_name, Update_Value"
# return successfully updated the attribute

# Restful API: POST method

'''
Test Json
[
    {
        "UserID": "USERID#2",
        "Attribute_name": "Age",
        "Update_value": 22
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
import json


def lambda_handler(event, context):
    if event:
        print("This is a POST request for attribute update")

        client = boto3.client('dynamodb', region_name = 'us-east-1')
        postINFO = json.loads(event['body'])[0]
        userID = postINFO['UserID']    # 'S':string
        attributeToUpdate = postINFO['Attribute_name']
        updateValue = postINFO['Update_value']
        
        results = client.update_item(
            TableName = 'BussinessCard',
            Key = {
                'PK': {'S': str('USER')},
                'SK': {'S': str(userID)}
            },
            ExpressionAttributeNames={
                "#attribute": str(attributeToUpdate),
            },
            ExpressionAttributeValues={
                ":value": {'S': str(updateValue)},
            },
            UpdateExpression="SET #attribute =:value",
        )

        print(results)

        response = {
            'statusCode': 200,
            'body': "successfully updated the attribute {attributename} of item to {value}!"\
                .format(attributename = attributeToUpdate, value = updateValue)
            }

        return response