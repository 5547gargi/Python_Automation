import boto3

aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_res=aws_mag_con.resource(service_name="ec2")

for each_item in ec2_con_res.meta.client.describe_regions()['Regions']:
     print(each_item['RegionName'])