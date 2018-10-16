#!/usr/bin/python3

import boto3
import sys
import getopt
import os
from datetime import datetime

def usage():
    print("Please check readme for usage")

def main():
    session = boto3.Session(profile_name='default')
    s3Client = session.client('s3')
    i = 0

    outputFolderPath = './s3_files/' + str(datetime.now().date())
    key = ""
    bucketName = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "b:k:", [])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-b", "--bucket"):
            bucketName = a
        elif o in ("-k", "--key"):
            key = a
        else:
            assert False, "unhandled option"
    print("BucketName:" + bucketName)
    print("Key:" + key)
    
    versions = s3Client.list_object_versions(Bucket=bucketName, Prefix=key)

    if not os.path.exists(outputFolderPath):
        os.makedirs(outputFolderPath)
    print(outputFolderPath)

    for obj in versions.get('Versions'):
        i = i+1
        s3Client.download_file(bucketName, key, outputFolderPath + "/" + str(obj.get('LastModified').date().isoformat())+".csv", ExtraArgs={"VersionId": obj.get('VersionId')})

    print("Total Files" + str(i))

if __name__ == "__main__":
    main()