#Automate Snapshots of EBS Volumes for All Regions
import boto3
import datetime

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2','us-east-1')
    all_regions= []
    for each_reg in ec2_client.describe_regions()['Regions']:
         all_regions.append(each_reg['RegionName'])
    for each_reg in all_regions:
         print(each_reg)
         ec2 = boto3.client('ec2', each_reg)
         # volumes = get_volumes(ec2)
         # create_snapshots(ec2, volumes)
         # cleanup_old_snapshots(ec2)
         list_of_volids=[]    
         paginator = ec2.get_paginator('describe_volumes')
         filter={"Name": "tag:Prod", "Values":['Backup']}
         for each_page in paginator.paginate(Filters=[filter]):
               for each_vol in each_page['Volumes']:
                   list_of_volids.append(each_vol['VolumeId'])
    print("The list of VolIds are : ",list_of_volids)
    if bool(list_of_volids)==False:
        print("No volumes to backup")
        continue
    snapshotIds=[]
    for each_volid in list_of_volids:
        print("Taking snapshot of the volumes : ", each_volid)
        response=ec2.create_snapshot(
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
        snapshotIds.append(response['SnapshotId'])
    print("The snapshot ids are : {}".format(snapshotIds))
    waiter = ec2.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapshotIds)
    print("Successfully completed snaps for the volumes of {}".format(list_of_volids))    

    






'''
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions()['Regions']
    for region in regions:
        ec2 = boto3.client('ec2', region_name=region['RegionName'])
        volumes = ec2.describe_volumes()['Volumes']
        for volume in volumes:
            if volume['State'] == 'available':
                snapshot = ec2.create_snapshot(VolumeId=volume['VolumeId'])
                ec2.create_tags(Resources=[snapshot['SnapshotId']], Tags=volume['Tags'])
                ec2.delete_volume(VolumeId=volume['VolumeId'])
                print('Snapshot of Volume ' + volume['VolumeId'] + ' created and volume ' + volume['VolumeId'] + ' deleted')
'''                