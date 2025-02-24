import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_res=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")

sts_con_cli=aws_mag_con.client(service_name="sts", region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
users_id=response.get('Account')
f1={"Name": "volume-size", "Values": ['10']}
for each_snap in ec2_con_res.snapshots.filter(OwnerIds=[users_id],filter=[f1]):
    print(each_snap)