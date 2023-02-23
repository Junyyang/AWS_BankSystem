# Admin Management
# Delete table for Bussiness Card

# Restful: GET Method

'''
Test Json
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
'''


import boto3

def lambda_handler(event, context):
    if event:
        print("This is a GET request")
        client = boto3.client('dynamodb', region_name = 'us-east-1')

        results = client.delete_table(
            TableName='BussinessCard',
            )
        print(results)


        response = {
            'statusCode': 200,
            'body': 'successfully delete table {tablename}!'.format(tablename = 'BankSystem'),
        }
        
        return response