import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.get_item(
    Key={
        'Name': 'Kelvin Galabuzi',
        'Email': 'kelvingalabuzi@handson.cloud'
    }
)
print(response['Item'])