import boto3
import datetime

aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_res=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
sts_client=aws_mag_con.client(service_name="sts", region_name="us-east-1")
response=sts_client.get_caller_identity()
users_id=response.get('Account')
today=datetime.datetime.now()
start_time=str(datetime.datetime(today.year, today.month, today.day, 4, 15, 44))   # Here the time formt is 24-Hrs 
for each_snap in ec2_con_res.snapshots.filter(OwnerIds=[users_id]):
     if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time: 
         print(each_snap.id,each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))