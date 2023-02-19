# Admin Management
# Create the item (User) by Partition Key(emailAddress)
# event contains "Email_address, Name, Age, Birthday, Job_title, Employer, City, Phone_number"

# Restful: POST Method

import boto3

def lambda_handler(event, context):
    if event:
        print("This is a POST request")

        client = boto3.client('dynamodb', region_name = 'us-east-1')

        # email_address
        emailAddress = event['Email_address']    # 'S':string
        name = event['Name']            # 'S':string
        age = event['Age']                      # 'N':strings, DynamoDB treats them as number type  
        birthday = event['Birthday']            # 'N':strings, DynamoDB treats them as number type    YYYYMMDD
        jobTitle = event['Job_title']            # 'S':string
        employer = event['Employer']            # 'S':string
        city = event['City']                    # 'S':string
        phoneNumber = event['Phone_number']      # 'N':strings, DynamoDB treats them as number type

        # TODO
        # if event['attribute'] == None, how to handle
        # Decorator???


        results = client.put_item(
            TableName='BankSystem',
            Item={
                'EmailAddress': {
                    'S': str(emailAddress)
                },
                'StaticSortKey':{
                    'S': str('bussiness_card')
                },
                'Name': {
                    'S': str(name)
                },
                'Age':{
                    'N': str(age)
                },
                'Birthday':{
                    'N': str(birthday)
                },
                'JobTitle':{
                    'S': str(jobTitle)
                },
                'Employer':{
                    'S': str(employer)
                },
                'City':{
                    'S': str(city)
                },
                'PhoneNumber':{
                    'N': str(phoneNumber)
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