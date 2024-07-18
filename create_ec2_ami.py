import boto3

region = 'ap-southeast-2'
#Create a session 
session = boto3.session.Session()
#Open ec2 client
ec2_client = session.client('ec2', region_name=region)
#Response
response = ec2_client.describe_instances()
'''
with open('ami_list.csv', 'w', newline='') as f:
    for instances in response['Reservations']:
        for instance in instances['Instances']:
            InstanceID = instance['InstanceId']
            print(InstanceID)
'''
#InstanceID list where Instance IDs will be stored
instance_ids = []
#Name tag list where Instance IDs will be stored
name_tags= []
for instances in response['Reservations']:
        #Get instance ID
        for instance in instances['Instances']:
            #Add instance ID to instance_ids list
            instance_ids.append(instance['InstanceId'])
            #Get name tag of instance
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    #Add name tag to name_tag list
                    name_tags.append(tag['Value'])
#Dictionary to store instance name and name_tag as key/value pair
output = {}
for i, instance in enumerate(instance_ids):
     output[instance] = name_tags[i]

#Create AMI image using instance id 
for instances in instance_ids:
    ami_name = output.get(instances)
    try:
        ec2_client.create_image(InstanceId=instance, Name=ami_name)
        print("Created AMI for:", ami_name)
    #Print error if encountered
    except:
         print("Error creating AMI for:", ami_name)

    

