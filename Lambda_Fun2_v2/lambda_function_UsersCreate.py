
# Users Management
# Create the item for User by SK(UserID)
# event contains "Email_address, Name, Age, Birthday, Job_title, Employer, City, Phone_number"

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
        print("This is a POST request")

        client = boto3.client('dynamodb', region_name = 'us-east-1')

        # email_address
        sk = event['UserID']
        emailAddress = event['Email_address']    # 'S':string
        name = event['Name']            # 'S':string
        age = event['Age']                      # 'N':strings, DynamoDB treats them as number type  
        birthday = event['Birthday']            # 'N':strings, DynamoDB treats them as number type    YYYYMMDD
        jobTitle = event['Job_title']            # 'S':string
        employer = event['Employer']            # 'S':string
        city = event['City']                    # 'S':string
        phoneNumber = event['Phone_number']      # 'N':strings, DynamoDB treats them as number type
        profilePicture = event['Profile_picture']

        results = client.put_item(
            TableName='BussinessCard',
            Item={
                'PK':{
                    'S': str('USER')
                },
                'SK': {
                    'S': str(sk)
                },
                'Name': {
                    'S': str(name)
                },
                'Age':{
                    'S': str(age)
                },
                'Email': {
                    'S': str(emailAddress)
                },
                'Birthday':{
                    'S': str(birthday)
                },
                'Job_title':{
                    'S': str(jobTitle)
                },
                'Employer':{
                    'S': str(employer)
                },
                'City':{
                    'S': str(city)
                },
                'Phone_number':{
                    'S': str(phoneNumber)
                },
                'Profile_picture':{
                    'S': str(profilePicture)
                }
            }
        )
        print(results)


        # TODO response
        response = {
            'statusCode': 200,
            'body': 'successfully created item!'
        }
        
        return response