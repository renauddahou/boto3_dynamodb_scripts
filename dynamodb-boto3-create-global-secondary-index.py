import boto3

client = dynamodb = boto3.client('dynamodb')

try:
    resp = client.update_table(
        TableName="Employees",
        AttributeDefinitions=[
            {
                "AttributeName": "CapacityBuildingLevel",
                "AttributeType": "S"
            },
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "CapacityBuildingIndex",
                    "KeySchema": [
                        {
                            "AttributeName": "CapacityBuildingLevel",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1,
                    }
                }
            }
        ],
    )
    print("Secondary index added!")
except Exception as e:
    print("Error updating table:")
    print(e)