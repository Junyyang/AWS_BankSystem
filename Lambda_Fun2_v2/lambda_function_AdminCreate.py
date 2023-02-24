# Admin Management
# Create the item (User) by Partition Key PK: UserID
# event contains "UserID, Email_address, Name, Age, Birthday, Job_title, Employer, City, Phone_number, Profile_picture"

# Restful: POST Method
'''
Test Json
[
    {
        "UserID": "USERID#1",
        "Email_address": "aaaa@gmail.com",
        "Name": "aaaa",
        "Age": "10",
        "Birthday": "11112233",
        "Job_title": "Engineer",
        "Employer": "AAAA",
        "City": "Acity",
        "Phone_number": "11111111111111",
        "Profile_picture": "PIC#1"
    }
]
'''

import boto3
import json

def lambda_handler(event, context):
    if event:
        print(" ")
        print(" ")
        print("=======================")
        print("This is a POST request")
        print("event body: ", json.loads(event['body'])[0])

        client = boto3.client('dynamodb', region_name = 'us-east-1')
        postINFO = json.loads(event['body'])[0]

        # email_address
        sk = postINFO['UserID']
        emailAddress = postINFO['Email_address']    # 'S':string
        name = postINFO['Name']            # 'S':string
        age = postINFO['Age']                      # 'N':strings, DynamoDB treats them as number type  
        birthday = postINFO['Birthday']            # 'N':strings, DynamoDB treats them as number type    YYYYMMDD
        jobTitle = postINFO['Job_title']            # 'S':string
        employer = postINFO['Employer']            # 'S':string
        city = postINFO['City']                    # 'S':string
        phoneNumber = postINFO['Phone_number']      # 'N':strings, DynamoDB treats them as number type
        profilePicture = postINFO['Profile_picture'] 

        # TODO
        # if event['attribute'] == None, how to handle
        # Decorator???


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
                'Email':{
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
        # how to handle False
        # false_response = {
        #     'statusCode': 404,
        #     'body': 'Created item by Admin failed.'
        # }

        response = {
            'statusCode': 200,
            'body': 'successfully created item by Admin!'
        }
        
        return response