# Admin Management
# Create table for Bussiness Card
# Partition key: PK: USER#
# Sort key: SK: USERID 
# GSI1PK: "USER" | "Admin"
# event contains "Email_address, Name, Age, Birthday, Job_title, Employer, City, Phone_number"

# Restful: GET Method

import json
import boto3

def lambda_handler(event, context):
    if event:
        print("This is a GET request")
        client = boto3.client('dynamodb', region_name = 'us-east-1')

        attributeDef = [
          {
            "AttributeName": "PK",
            "AttributeType": "S"
          },
          {
            "AttributeName": "SK",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Age",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Job_title",
            "AttributeType": "S"
          },
          {
            "AttributeName": "Employer",
            "AttributeType": "S"
          },
          {
            "AttributeName": "City",
            "AttributeType": "S"
          }
        ]

        GSISchema1 = [
            {'IndexName': 'Readall',
                'KeySchema': [
                    {
                        'AttributeName': 'PK',
                        'KeyType': 'HASH'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': [
                        'SK',
                        'Name',
                        'Age',
                        'Birthday',
                        'Job_title',
                        'Employer',
                        'City',
                        'Email',
                        'Phone_number',
                        'Profile_picture'
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            },

            {'IndexName': 'SortByAge',
                'KeySchema': [
                    {
                        'AttributeName': 'PK',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'Age',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': [
                        'SK',
                        'Name',
                        'Age',
                        'Birthday',
                        'Job_title',
                        'Employer',
                        'City',
                        'Email',
                        'Phone_number',
                        'Profile_picture'
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            },

            {'IndexName': 'SortByJobTitle',
                'KeySchema': [
                    {
                        'AttributeName': 'PK',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'Job_title',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': [
                        'SK',
                        'Name',
                        'Age',
                        'Birthday',
                        'Job_title',
                        'Employer',
                        'City',
                        'Email',
                        'Phone_number',
                        'Profile_picture'
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            },

            {'IndexName': 'SortByEmployer',
                'KeySchema': [
                    {
                        'AttributeName': 'PK',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'Employer',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': [
                        'SK',
                        'Name',
                        'Age',
                        'Birthday',
                        'Job_title',
                        'Employer',
                        'City',
                        'Email',
                        'Phone_number',
                        'Profile_picture'
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            },

            {'IndexName': 'SortByCity',
                'KeySchema': [
                    {
                        'AttributeName': 'PK',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'City',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'INCLUDE',
                    'NonKeyAttributes': [
                        'SK',
                        'Name',
                        'Age',
                        'Birthday',
                        'Job_title',
                        'Employer',
                        'City',
                        'Email',
                        'Phone_number',
                        'Profile_picture'
                    ]
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            },
        ]


        results = client.create_table(
            TableName='BussinessCard',
            KeySchema = [
                    {
                        'AttributeName':'PK',
                        'KeyType':'HASH'                                       
                    },
                    {
                        'AttributeName':'SK',
                        'KeyType':'RANGE'
                    }      
                ],
                
            AttributeDefinitions = attributeDef,
            GlobalSecondaryIndexes = GSISchema1,
            
            ProvisionedThroughput = {
                'ReadCapacityUnits':10,
                'WriteCapacityUnits':10
            }
            )
        print(results)


        response = {
            'statusCode': 200,
            'body': 'successfully created table, (PK: USER#, SK: USERID)!',
        }
        
        return response