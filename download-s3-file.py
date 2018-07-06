import boto3
import os
from datetime import datetime
session = boto3.Session(profile_name='saml')
s3Client = session.client('s3')
i=0;
outputFolderPath = '//US-WASH-D49WSC2/share/SSBFiles/prod_'+ str(datetime.now().date())
key = "prod/SSB-direct-import/DirectCloudSSBHoldings.csv"
bucketName = "prod-mp-gateway-store"
versions = s3Client.list_object_versions(Bucket = bucketName, Prefix  = key)
if not os.path.exists(outputFolderPath):
    os.makedirs(outputFolderPath)
print(outputFolderPath)
for obj in versions.get('Versions'):
    i=i+1
    s3Client.download_file(bucketName,key, outputFolderPath + "/"+ str(obj.get('LastModified').date().isoformat())+".csv", ExtraArgs={"VersionId": obj.get('VersionId')})

print("Total Files" + str(i))