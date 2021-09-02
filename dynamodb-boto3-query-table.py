import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

response = table.query(KeyConditionExpression=Key('Name').eq('Luzze John'))

print("The query returned the following items:")
for item in response['Items']:
    print(item)
