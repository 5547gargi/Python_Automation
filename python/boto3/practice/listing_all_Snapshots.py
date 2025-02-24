import boto3
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_client_res=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")

sts_client=aws_mag_con_root.client(service_name="sts",region_name="us-east-1")
response_sts=sts_client.get_caller_identity()
# print(response_sts.get('Account'))
users_id=response_sts.get('Account')
'''
for each_snap in ec2_client_res.snapshots.all():
      print(each_snap)
'''
'''      
# using resource
for each_snap in ec2_client_res.snapshots.filter(OwnerIds=[users_id]):
    print(each_snap)
'''
# using client
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-1")
for each_snap in ec2_con_cli.describe_snapshots(OwnerIds=[users_id])['Snapshots']:
    print(each_snap['SnapshotId'], each_snap['Description'])    