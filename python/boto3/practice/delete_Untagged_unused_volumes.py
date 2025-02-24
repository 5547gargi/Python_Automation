import boto3

aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_res=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
'''
for each_vol in ec2_con_res.volumes.all():
    print(each_vol.id, each_vol.state)
'''
'''
#using resource
f1={"Name": "status", "Values":['available']}
for each_vol in ec2_con_res.volumes.filter(Filters=[f1]):
     if not each_vol.tags:
        print(each_vol.id, each_vol.state, each_vol.tags)
        print("Deleting unused and untagged volumes...")
        each_vol.delete()
        print("Deleted unused and untagged volumes...")
'''
#using client
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-1")
f2={"Name": "status", "Values":['available']}
for each_vol in ec2_con_cli.describe_volumes(Filters=[f2])['Volumes']:
    if not each_vol['Tags']:
        print(each_vol['VolumeId'], each_vol['State'], each_vol['Tags'])
        print("Deleting unused and untagged volumes...")
        ec2_con_cli.delete_volume(VolumeId=each_vol['VolumeId'])
        print("Deleted unused and untagged volumes...")        