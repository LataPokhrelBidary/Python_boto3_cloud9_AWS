import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='mytestbukcet65485623351'
)

print('bucket deleted successfully')