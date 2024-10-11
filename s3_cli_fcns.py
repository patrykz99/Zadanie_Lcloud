import boto3
import os
from config import Config

config_class = Config()
bucket = 'developer-task'
prefix = 'y-wing/'


s3_b = boto3.client('s3',
                    aws_access_key_id=config_class.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key = config_class.AWS_SECRET_ACCESS_KEY)


def list_files_s3():
    ''' Fcn to list all files S3 Bucket prefix y-wing/'''
    try:
        response = s3_b.list_objects_v2(Bucket=bucket, Prefix=prefix)
        print(response)
        if 'Contents' in response:
            print(f'Files in bucket {bucket} (prefix: {prefix}): ')
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f'No files in bucket {bucket} (prefix: {prefix}).')
    except Exception as e:
        print(f"Error in listing files: {e}")

