# Admin Management
# Sort the item User by Attribute
# event contains "attribute name, ascending"

# Restful API: POST method


import boto3
import time
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
    if event:
        print("This is a POST request for Admin Sorting")

        client = boto3.client('dynamodb', region_name = 'us-east-1')
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('BankSystem')

        # POST method
        sortedBy = event['Attribute_name']    # 'S':string
        ascending = (event['Ascending'] == 'ascending')         # Bool value
        gsiName = "SortedIndex" + sortedBy

        if sortedBy in ['Email_address', 'Name', 'Job_title', 'City', 'Phone_number']:
            attributeType = 'S'
        elif sortedBy in ['Age', 'Birthday', 'Phone_number']:
            attributeType = 'N'

        # if GSI does't exist:
        tableInfo = client.describe_table(
                    TableName='BankSystem'
                )
        print(tableInfo['Table'])
        try:
            # some GSI have been created but not sure whether the "gsiName" has been created before
            GlobalSecondaryIndexes = tableInfo['Table']["GlobalSecondaryIndexes"]
            GSI_list = [GlobalSecondaryIndexes[i]['IndexName'] for i in range(len(GlobalSecondaryIndexes))]
            if gsiName not in GSI_list:
                # Create new GSI
                print("Creating new GSI sorted by {sort}".format(sort = sortedBy))
                results = client.update_table(
                    TableName = 'BankSystem',

                    AttributeDefinitions = [
                        {
                            "AttributeName": "StaticSortKey",
                            "AttributeType": "S"
                        },
                        {
                            "AttributeName": sortedBy,
                            "AttributeType": attributeType   # "S" or "N"
                        }
                    ],
                    
                    GlobalSecondaryIndexUpdates=[
                        {
                            'Create':{
                                # You need to name your index and specifically refer to it when using it for queries.
                                "IndexName": gsiName,
                                "KeySchema":[
                                    {
                                        "AttributeName": "StaticSortKey",
                                        "KeyType": "HASH"
                                    },
                                    {
                                        "AttributeName":sortedBy,
                                        "KeyType":"RANGE"  # "RANGE" for SortKey
                                    }
                                ],
                                "Projection":{
                                    "ProjectionType":"ALL"
                                },
                                "ProvisionedThroughput":{
                                    "ReadCapacityUnits":10,
                                    "WriteCapacityUnits":10
                                }
                            }
                        }
                    ]
                )
                print(results)
            else:
                pass
        except:
            # GSI already exists
            print("GSI already exists")
            pass

        
        while True:
            if (not table.global_secondary_indexes) or (table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE'):
                print('Waiting for index to backfill...')
                time.sleep(5)
                table.reload()
            else:
                break
        
        # Scan/Query the table based on sortedBy
        '''
        Query results are always sorted by the sort key value. 
        If the data type of the sort key is Number, the results are returned in numeric order; 
        otherwise, the results are returned in order of UTF-8 bytes. 
        By default, the sort order is ascending. 
        To reverse the order, set the ScanIndexForward parameter to false.
        '''
        results = table.query(
            # Add the name of the index you want to use in your query.
            IndexName = gsiName,
            KeyConditionExpression = Key('StaticSortKey').eq('bussiness_card'),
            ScanIndexForward = ascending
        )

        # TODO response
        response = {
            'statusCode': 200,
            'body': json.dumps(results["Items"])
        }
        
        return response