import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.update_item(
    Key={'Name': 'Luzze John', 'Email': 'john@handson.cloud'},
    ExpressionAttributeNames={
        "#section": "Section",
        "#qa": "QA",
        },
        ExpressionAttributeValues={
            ':id': 'QA-2'
        },
        UpdateExpression="SET #section.#qa = :id",
    )
print(response)