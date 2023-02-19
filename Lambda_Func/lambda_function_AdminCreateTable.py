# Admin Management
# Create table for Bussiness Card
# Partition key: userID, Sort key: (static )
# event contains "Email_address, Name, Age, Birthday, Job_title, Employer, City, Phone_number"

# Restful: GET Method

import json
import boto3

def lambda_handler(event, context):
    if event:
        print("This is a GET request")
        client = boto3.client('dynamodb', region_name = 'us-east-1')

        results = client.create_table(
            TableName='BankSystem',
            KeySchema = [
                    {
                        'AttributeName':'EmailAddress',
                        'KeyType':'HASH'                                       
                    },
                    {
                        'AttributeName':'StaticSortKey',
                        'KeyType':'RANGE'
                    }      
                ],
                
            AttributeDefinitions = [
                {
                    'AttributeName':'EmailAddress',
                    'AttributeType':'S'  # S for string
                },
                {
                    'AttributeName':'StaticSortKey',
                    'AttributeType':'S'
                }
            ],
            
            ProvisionedThroughput = {
                'ReadCapacityUnits':10,
                'WriteCapacityUnits':10
            }
            )
        print(results)


        response = {
            'statusCode': 200,
            'body': 'successfully created table, (PK: EmailAddress, SK: StaticSortKey)!',
        }
        
        return response