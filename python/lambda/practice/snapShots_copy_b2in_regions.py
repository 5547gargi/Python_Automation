import os,sys
try:
    import boto3
    print("boto3 is installed")
except ImportError:
    print("boto3 is not installed")
    os.system("pip install boto3")
    import boto3
    print("boto3 is installed")
except Exception as e:
    print(e)
    sys.exit(1)

source_region='us-east-1'
dest_region='us-east-2'

session=boto3.session.Session(profile_name="root")
ec2_source_client=session.client(service_name="ec2",region_name=source_region)
sts_clirnt=session.client(service_name="sts", region_name=source_region)
account_id=sts_clirnt.get_caller_identity().get("Account")
f_bkp={'Name':'tag:backup','Values':['yes']}
bkpSnap_ids=[]
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id],Filters=[f_bkp]).get('Snapshots'):
     bkpSnap_ids.append(each_snap.get('SnapshotId'))

ec2_dest_client=session.client(service_name="ec2", region_name=dest_region)

for each_source_snapid in bkpSnap_ids:
     print("Taking backup {} into a {}".format(each_source_snapid, dest_region))
     ec2_dest_client.copy_snapshot(
        Description='For Disastor',
        SourceRegion=source_region,
        SourceSnapshotId=each_source_snapid
     )
     waiter=ec2_dest_client.get_waiter('snapshot_completed')
     waiter.wait(SnapshotIds=[each_source_snapid])
     print("The snapshot Ids are: ", bkpSnap_ids)
     print("The backup of the snapshots are completed")
     print("Terminating the snapshots in the source region")
     ec2_source_client.delete_snapshot(SnapshotId=each_source_snapid)
     print("The snapshots are terminated in the source region")
     print("All the snapshots are backed up successfully")

print("Modifying tags for which backup is completed")
for each_source_snapid in bkpSnap_ids:
     print("Deleting old Tags for {}",format(each_source_snapid))
     ec2_dest_client.delete_tags(
        Resources=[each_source_snapid],
        Tags=[{'Key':'backup','Value':'yes'}]
        )
     print("Creating new Tags for {}",format(each_source_snapid))   
     ec2_dest_client.create_tags(
        Resources=[each_source_snapid],
        Tags=[{'Key':'backup','Value':'completed'}]
        )   
     print("Thank you for using this script")