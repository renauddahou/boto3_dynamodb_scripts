import time

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

while True:
    if not table.global_secondary_indexes or table.global_secondary_indexes[0]['IndexStatus'] != 'ACTIVE':
        print('Waiting for index to backfill...')
        time.sleep(5)
        table.reload()
    else:
        break

resp = table.query(
    IndexName="CapacityBuildingIndex",
    KeyConditionExpression=Key('CapacityBuildingLevel').eq('Level 4'),
)

print("The query returned the following items:")
for item in resp['Items']:
    print(item)
