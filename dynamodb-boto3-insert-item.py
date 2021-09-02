import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.put_item(
Item = { 
     'Name': 'Kelvin Galabuzi',
     'Email': 'kelvingalabuzi@handson.cloud'
       }
)
print(response)
