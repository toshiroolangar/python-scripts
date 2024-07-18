import boto3
import csv
import boto3.session

#Region
region = 'ap-southeast-2'
#Open a session
session = boto3.session.Session()
#Access EC2 client
ec2_client = session.client('ec2', region_name=region)

response = ec2_client.describe_instances()

with open("instance_list.csv", 'w', newline='') as f:
    csv_write = csv.writer(f)
    for content in response['Reservations']:
        for instances in content['Instances']:
            InstanceID = instances['InstanceId']
            InstanceType = instances['InstanceType']
    name_tag = None
    for tag in instances.get('Tags', []):
        if tag['Key'] == 'Name':
            name_tag = tag['Value']
    csv_write.writerow(['Instance name', 'Instance ID', 'Instance Type'])
    csv_write.writerow([name_tag, InstanceID, InstanceType])

print("File has been successfully written")



