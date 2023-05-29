import boto3
from dotenv import load_dotenv
import os

load_dotenv()
bucket = 'no18'


def downloads_recording(member_nickname, file_name):
    s3 = boto3.resource('s3',
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    key = member_nickname + '/' + file_name
    s3.Bucket(bucket).download_file(Key=key, Filename='recordings/'+file_name)
    return file_name
