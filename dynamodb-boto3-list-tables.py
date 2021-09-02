import boto3

dynamodb = boto3.resource('dynamodb')

print(list(dynamodb.tables.all()))