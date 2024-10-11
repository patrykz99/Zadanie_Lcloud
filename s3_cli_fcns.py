import boto3
import os
import re
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
        # print(response)
        #print(response.items())
        if 'Contents' in response:
            print(f'Files in bucket {bucket} (prefix: {prefix}): ')
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f'No files found in {bucket} {prefix}')
    except Exception as e:
        print(f"Error in listing files: {e}")

def upload_local_file_s3(local_file_path:str, key_file_name:str):
    '''Upload local file to S3 Bucket with prefix y-wing/'''
    try:
        key_file_name = f"{prefix}{key_file_name}" #Added prefix before to mark the proper location
        s3_b.upload_file(local_file_path, bucket, key_file_name)
        print(f"Local file ('{local_file_path}') uploaded as '{key_file_name}'.")
    except Exception as e:
        print(f"Error in uploading file: {e}")

def list_files_with_regex_s3(pattern:str):
    ''' fcn to list files with proper regex pattern'''
    list_matched_files = []
    try:
        response = s3_b.list_objects_v2(Bucket=bucket, Prefix=prefix)
        if 'Contents' in response:
            r_patt = re.compile(pattern)
            for obj in response['Contents']:
                if r_patt.search(obj['Key']):
                    list_matched_files.append(obj['Key'])
                    
            if list_matched_files == True:
                print('Files: ')
                for file in list_matched_files:
                    print(file)
            else:
                print(f'No files with matching pattern')
        else:
            print(f'No files found in {bucket} {prefix}')
    
    except Exception as e:
        print(f"Error in listing files: {e}")

def delete_files_with_regex_s3(pattern):
    ''' fcn to delete proper files with pattern from bucket/prefix'''
    try:
        response = s3_b.list_objects_v2(Bucket=bucket, Prefix=prefix)
        
        if 'Contents' in response:
            r_patt = re.compile(pattern)
            for obj in response['Contents']:
                if r_patt.search(obj['Key']):
                    s3_b.delete_object(Bucket=bucket, Key=obj['Key'])
                    print(f"Deleted file: {obj['Key']}")
        else:
            print(f'No files found in {bucket} {prefix}')
    
    except Exception as e:
        print(f"Error in deleting files {e}")