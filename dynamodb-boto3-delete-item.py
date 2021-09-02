import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.delete_item(Key = {'Name': 'Peter Matovu', 'Email': 'petermatovu@handson.cloud'})

print(response)