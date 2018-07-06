download-s3-file: downloads all the versions of the given key.

Usage:
	* Generate token for the environment.
	* Open download-s3-file.py 
		Update :
			outputFolderPath:- path where files are downloaded.
			bucketName :- Name of bucket.
			key:- S3 Key.
			
			Current default values are as below:		
			outputFolderPath = '//US-WASH-D49WSC2/share/SSBFiles/prod_'+ str(datetime.now().date())
			key = "prod/SSB-direct-import/DirectCloudSSBHoldings.csv"
			bucketName = "prod-mp-gateway-store"
	* Run below command:
		python download-s3-file.py