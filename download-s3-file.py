#!/usr/bin/python3

import boto3
import sys
import getopt
import os
from datetime import datetime


def usage():
    print("Please check readme for usage.")


def main():
    profile_name = 'default'
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3')

    key = ''
    bucket_name = ''

    path_separator = os.path.sep
    output_folder_path = '.' + path_separator + 'output' + path_separator + str(datetime.now())

    try:
        opts, args = getopt.getopt(sys.argv[1:], "b:k:o:", [])
    except getopt.GetoptError as err:
        # Print help information and exit:
        print(err)  # Will print something like "option -a not recognized."
        usage()
        sys.exit(2)

    for o, opt_val in opts:
        if o in ("-b", "--bucket"):
            bucket_name = opt_val
        elif o in ("-k", "--key"):
            key = opt_val
        elif o in ("-o", "--output_folder"):
            output_folder_path = opt_val
        else:
            assert False, "unhandled option."
    print("BucketName:" + bucket_name)
    print("Key:" + key)

    versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix=key)

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    print(output_folder_path)

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


if __name__ == "__main__":
    main()
