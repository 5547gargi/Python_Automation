#Automated EBS Snapshots using AWS Lambda and CloudWatch
import boto3
from pprint import pprint

session=boto3.session.Session(profile_name="default")
ec2_cli=session.client(service_name="ec2",region_name="us-east-1")
list_of_volids=[]
filter={"Name": "tag:Prod", "Values":['Backup']}
# for each_vol in ec2_cli.describe_volumes(Filters=[filter])['Volumes']:
#     list_of_volids.append(each_vol['VolumeId'])
paginator = ec2_cli.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[filter]):
    for each_vol in each_page['Volumes']:
        list_of_volids.append(each_vol['VolumeId'])
print("The list of VolIds are : ",list_of_volids)

snapshotIds=[]
for each_volid in list_of_volids:
     print("Taking backup of {}".format(each_volid))
     res=ec2_cli.cerate_snapshot(
         Description="Taking snap with Lambda and cw",
         VolumeId=each_volid,
         TagSpecifications=[
               {
                 'ResourceType': 'snapshot',
                 'Tags': [
                     {
                         'Key': 'Delete-on',
                         'Value': '90'
                    }
                ]
                }
            ]
        )
     snapshotIds.append(res['SnapshotId'])
pprint("The snapshot ids are : {}".format(snapshotIds))
waiter = ec2_cli.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapshotIds)
print("Successfully completed snaps for the volumes of {}".format(list_of_volids))   


'''
def create_ebs_snapshot(event, context):
    """Lambda handler to create EBS snapshots"""
    ec2 = boto3.client('ec2')
    volumes = get_ebs_volumes(ec2)
    create_snapshots(ec2, volumes)
    cleanup_old_snapshots(ec2)

def get_ebs_volumes(ec2):
    """Get list of EBS volumes with backup tag"""
    filters = [{'Name': 'tag:Backup', 'Values': ['true']}]
    response = ec2.describe_volumes(Filters=filters)
    return response['Volumes']
    #print(response['Volumes'])

def create_snapshots(ec2, volumes):
    """Create EBS snapshots for the specified volumes"""
    for volume in volumes:
        volume_id = volume['VolumeId']
        description = f"Snapshot for volume {volume_id}"
        ec2.create_snapshot(VolumeId=volume_id, Description=description)
        print(f"Created snapshot for volume {volume_id}")
        #print(volume_id)

def cleanup_old_snapshots(ec2):
    """Delete EBS snapshots older than 7 days"""
    seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)
    filters = [{'Name': 'tag:Backup', 'Values': ['true']}]
    snapshots = ec2.describe_snapshots(Filters=filters)['Snapshots']
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        snapshot_date = snapshot['StartTime'].replace(tzinfo=None)
        if snapshot_date < seven_days_ago:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id}")
'''            