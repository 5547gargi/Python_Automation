import boto3

ec2=boto3.resource('ec2')

for vol in ec2.volumes.all():
     print(vol)

for vol in ec2.volumes.filter(Filters=[{'Name':'status','Values':['available']}]):
     print(vol.id,vol.state,vol.tags)
     vol_id=vol.id
     volume=ec2.Volume(vol_id)
     print(f'Deleting {vol_id}')
     volume.delete()