# User Management
# Delete the item for User by SK: "UserID"
# event contains "UserID"
# return 

# Restful API: POST method

'''
N (string) --
An attribute of type Number. For example:

"N": "123.45"
Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. 
However, DynamoDB treats them as number type attributes for mathematical operations.
'''

import boto3


def lambda_handler(event, context):
    if event:
        print("This is a POST request for detele item")

        client = boto3.client('dynamodb', region_name = 'us-east-1')

        sk = event['UserID']    # 'S':string

        results = client.delete_item(
            TableName = 'BankSystem',
            Key = {
                'PK': {'S': str('USER')},
                'SK': {'S': str(sk)}
            }
        )

        print(results)

        response = {
            'statusCode': 200,
            'body': "successfully deleted the item of {id}!"\
                .format(id = sk)
            }

        return response