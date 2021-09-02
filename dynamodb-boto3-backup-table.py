import boto3

client = boto3.client('dynamodb')

response = client.create_backup(
    TableName='Employees',
    BackupName='Employees-Backup-01'
)
print(response)