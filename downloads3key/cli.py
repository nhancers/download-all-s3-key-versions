import boto3
import os
from datetime import datetime
import click

@click.command()
@click.option('--bucket', '-b', required=True, help='Bucket name.')
@click.option('--key', '-k', required=True, help='Key.')
def download(bucket, key):
    profile_name = 'default'
    session = boto3.Session()
    s3_client = session.client('s3')
    bucket_name = bucket;

    path_separator = os.path.sep
    output_folder_path = '.' + path_separator + 'output' + path_separator + str(datetime.now())

    print('BucketName:' + bucket_name)
    print('Key:' + key)

    versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix=key)

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    print('Downloading to:' + output_folder_path)

    i = 0
    head, file_name = os.path.split(key)

    for obj in versions.get('Versions') or []:
        i = i + 1
        version_id = ''
        if obj.get('VersionId') != 'null':
            version_id = obj.get('VersionId')
        output_file = output_folder_path + path_separator + str(
            obj.get('LastModified').date().isoformat()) + "_" + version_id + file_name
        s3_client.download_file(bucket_name, key, output_file, ExtraArgs={"VersionId": obj.get('VersionId')})

    print("Total Files: " + str(i))