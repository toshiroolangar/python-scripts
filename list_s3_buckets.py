import boto3
#Open a session
session = boto3.session.Session()
#Create a client
s3_client = session.client('s3')
#Variable for list buckets
list_response = s3_client.list_buckets()
#List of s3 buckets 
s3_buckets = []
#Get s3 buckets and write the result to s3_buckets list variable
for bucket in list_response['Buckets']:
    #print(bucket['Name'])
    s3_buckets.append(bucket['Name'])
#List all the files inside the s3 buckets, access "Contents" in Response, then access the object name using "Key"
for folder in s3_buckets:
    objects = s3_client.list_objects_v2(Bucket=folder)
    try:
        for obj in objects['Contents']:
            print(folder, obj['Key'])
    except KeyError:
        print('Bucket',folder,'is empty')