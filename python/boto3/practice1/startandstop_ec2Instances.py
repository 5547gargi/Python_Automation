import boto3

session=boto3.session.Session(profile_name="root")
ec2_res=session.resource(service_name="ec2",region_name="us-east-1")

#filtering ec2 instances with tag:Name=prod and instance type=t2.micro
ec2_tag={"Name":"tag:Name", "Values":["prod"]}
ec2_filter={"Name":"instance-type", "Values":["t2.micro"]}
for each_instance in ec2_res.instances.filter(Filters=[ec2_tag, ec2_filter]):
     each_instance.stop()

#Now stopping instances in different region
regions=[]
for region in ec2_res.meta.client.describe_regions()["Regions"]:
     regions.append(region["RegionName"])
     
for region in regions:
     ec2_res=session.resource(service_name="ec2", region_name=region)
     for each_instance in ec2_res.instances.filter(Filters=[ec2_tag, ec2_filter]):
         each_instance.stop()         