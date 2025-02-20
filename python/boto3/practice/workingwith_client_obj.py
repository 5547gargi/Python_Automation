import boto3

aws_mag_con=boto3.session.Session(profile='root')
#iam,ec2,s3
iam_con_client=aws_mag_con.client(service_name="iam",region_name='us-east-1')
ec2_con_client=aws_mag_con.client(service_name="ec2",region_name='us-east-1')
s3_con_client=aws_mag_con.client(service_name="s3",region_name='us-east-1')

#List all iam users using client object
#Follow boto3 documentation
response_iam=iam_con_client.list_users()
for each_iam in response_iam['Users']:
    print(each_iam['UserName'])
    
#List all ec2_instances id's
response_ec2=ec2_con_client.describe_instances()
for each_ec2 in response_ec2['Reservations']:
     for each_ec2_instance in each_ec2['Instances']:
        print(each_ec2_instance['InstanceId'])