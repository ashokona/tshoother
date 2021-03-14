import boto3
from sts import credentials
from utils import fetchKey

class Boto3Client:
    def __init__(self, client):
        self.client = boto3.client(client,
                                   aws_access_key_id=credentials['AccessKeyId'],
                                   aws_secret_access_key=credentials['SecretAccessKey'],
                                   aws_session_token=credentials['SessionToken']
                                   )

    def execMethod(self, method, args, value):
        response = getattr(self.client, method)(**args)
        # return response[value]
        return fetchKey(value, response)

