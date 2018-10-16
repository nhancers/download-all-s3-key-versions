
# Description

Downloads all the versions of the given key

##  Usage  
* Generate token for the environment.

* Run

    *sudo python3 download-s3-file.py -b "{{s3  bucket  name}}" -k "{{s3  key}}* 

	Parameters:

		-b : S3 bucket name.

		-k : S3 key.

## Sample

    sudo python3 download-s3-file.py -b "prod-mp-gateway-store" -k "prod/SSB-direct-import/DirectCloudSSBHoldings.csv"
