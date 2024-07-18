import boto3
import boto3.session
import csv

region = 'ap-southeast-2'

session = boto3.session.Session()
iam = session.client('iam', region_name = 'region')

out_file = "./iam_users.csv"
response = iam.list_users()
for user in response['Users']:
    UserName = user['UserName']
    UserID = user['UserId']
    DateCreated = user['CreateDate']
    

with open (out_file, 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['UserName', 'UserID', 'DateCreated'])
    csv_writer.writerow([UserName, UserID, DateCreated])
