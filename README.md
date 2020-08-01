
##	Description

Utility to download all version of s3 file. 

##	Usage  
```shell
python3 download-s3-file.py -b "{{s3  bucket  name}}" -k "{{s3  key}}" -o "{{output folder path}}"
```

Parameters:
```
-b : S3 bucket name.
-k : S3 key.
-o : output folder path where downloaded files will be stored. (optional:If not specified a folder with name output will be created in current directory)
```

## Sample
```shell
python3 download-s3-file.py -b "my-bucket" -k "filename.txt"
```