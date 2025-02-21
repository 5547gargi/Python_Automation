import boto3
from pprint import pprint
aws_mag_con = boto3.session.Session(profile_name='ec2_developer')
ec2_client=aws_mag_con.client(service_name="ec2",region_name="us-west-1")

#getting instance_ids,state,luching time
response_ec2=ec2_client.describe_instances()['Reservations']
for each_item in response_ec2:
     for each in each_item['Instances']:
         print("The Image_Id is: {}\nThe Instance_Id is: {}\nThe Lunch_Time is: {}".format(each['IamgeId'],each['InstanceId'],each['LunchTime'].strftime("%Y-%m-%d")))

# getting attached volumes details
response_ec2_vol=ec2_client.describe_volumes()['Volumes']
#print(response_ec2_vol) # getting all volumes details as alist
for each_item in response_ec2_vol:
    print("The Volume_Id is: {}\nThe Volume_State is: {}\nThe Volume_Type is: {}\nThe Volume_Size is: {}\nThe Volume_Creation_Time is: {}".format(each_item['VolumeId'], each_item['State'], each_item['VolumeType'], each_item['Size'], each_item['CreateTime'].strftime("%Y-%m-%d")))