import json
import boto3
import urllib3

# Virtual Buttons Source
# https://www.patreon.com/posts/getting-started-31849096


def get_secret():
    """AWS Secrets Manager to retrieve your API key"""
    secret_name = "VirtualButton-alexa"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(f'encountered exception: {e}')
    else:
        # Decrypts secret using the associated KMS CMK.
        secret = get_secret_value_response['SecretString']
        return secret


def lambda_handler(event, context):
    """Makes the call to your Alexa, set up a routine in the Alexa app for your Virtual button!"""
    http = urllib3.PoolManager()
    body = json.dumps({
        "virtualButton": 1,
        "accessCode": get_secret()[14:-2]
    })

    http.request(
        "POST",
        "https://api.virtualbuttons.com/v1",
        body=body
    )
