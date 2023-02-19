# User Management
# Delete the item for User by Partition Key(emailAddress)
# event contains "Email_address"
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

        emailAddress = event['Email_address']    # 'S':string

        results = client.delete_item(
            TableName = 'BankSystem',
            Key = {
                'Email_address': {'S': str(emailAddress)},
                'StaticSortKey': {'S': str('bussiness_card')}
            }
        )

        print(results)

        response = {
            'statusCode': 200,
            'body': "successfully deleted the item of {emailaddress}!"\
                .format(emailaddress = emailAddress)
            }

        return response