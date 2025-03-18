import boto3
from datetime import datetime, timedelta, timezone

ec2=boto3.resource('ec2')
print(ec2.snapshots.all())
'''
for snapshot in ec2.snapshots.all():
     # start_time=snapshot.start_time
     # delete_time=datetime.now(tz=timezone.utc)-timedelta(days=1)
     # if delete_time>start_time:
     #     snapshot.delete()
     #     print(snapshot)
     print(snapshot)
#It will list all the snapshots available for this account     
'''
# snaphot_maxage=30 
current_date=datetime.now(tz=timezone.utc)
diffin_days=current_date-timedelta(days=30)

for snapshot in ec2.snapshots.filter(OwnerIds=['self']):
     print(snapshot)
     start_time=snapshot.start_time
     snapshot_id=snapshot.snapshot_id
     if diffin_days>start_time:
         try:
             snapshot.delete()
             print("Deleting snapshot {}".format(snapshot_id))
         except Exception as e:
             print("Issue deleting snapshot or snapshot is in use {}".format(snapshot_id))
             continue
    