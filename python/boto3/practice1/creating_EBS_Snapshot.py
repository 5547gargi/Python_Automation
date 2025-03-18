import boto3

ec2 = boto3.resource('ec2')

for vol in ec2.volumes.all():
     vol_id=vol.id
     volume=ec2.Volume(vol_id)
     print('creating Snapshot of the following volumes',vol_id)
     volume.create_snapshot(Description='snapshot of volume'+vol_id)
