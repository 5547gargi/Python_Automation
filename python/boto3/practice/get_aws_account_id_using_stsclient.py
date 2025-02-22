import boto3

aws_mag_con_root= boto3.session.Session(profile_name="root")
sts_client=aws_mag_con_root.client(service_name="sts",region_name="us-east-1")
response_sts=sts_client.get_caller_identity()
print(response_sts) #will get o/p as dictionary 
print(response_sts['Account'])
print(response_sts.get('Account'))