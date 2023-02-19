# Users Management
# Update the specific attribute for User by Partition Key(emailAddress)
# event contains "Email_address, Attribute_name, Update_Value"
# return successfully updated the attribute

# Restful API: POST method

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

        emailAddress = event['Email_address']    # 'S':string
        attributeToUpdate = event['Attribute_name']
        updateValue = event['Update_value']
        
        if attributeToUpdate in ['Email_address', 'Name', 'Job_title', 'City', 'Phone_number']:
            attributeType = 'S'
        elif attributeToUpdate in ['Age', 'Birthday', 'Phone_number']:
            attributeType = 'N'

        results = client.update_item(
            TableName = 'BankSystem',
            Key = {
                'EmailAddress': {'S': str(emailAddress)},
                'StaticSortKey': {'S': str('bussiness_card')}
            },
            ExpressionAttributeNames={
                "#attribute": str(attributeToUpdate),
            },
            ExpressionAttributeValues={
                ":value": {attributeType: str(updateValue)},
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