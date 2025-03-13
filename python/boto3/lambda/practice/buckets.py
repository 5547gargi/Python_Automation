import boto3
session=boto3.Session(profile_name='dev_root')

#using resource
s3=session.resource(service_name='s3',region_name='us-east-1')
for each_bucket in s3.buckets.all():
     print(each_bucket.name)

#using client
s3=session.client(service_name='s3', region_name='us-east-1')
for each_bucket in s3.list_buckets()['Buckets']:
     print(each_bucket['Name'])

#listing bucket objects for a perticular bucket using resource obj
s3_re=session.resource(service_name='s3', region_name='us-east-1')
bucket_name='XXXXXXXX'
bucket_obj=s3_re.Bucket(bucket_name)
cnt=1
for each_obj in bucket_obj.objects.all():
     print(cnt, each_obj.key)
     cnt+=1

#listing bucket objects for a perticular bucket using client obj
s3_cl=session.client(service_name='s3', region_name='us-east-1')
bucket_name='XXXXXXXX'
cnt=1
for each_obj in s3_cl.list_objects(Bucket=bucket_name)['Contents']:
     print(cnt, each_obj['Key'])
     cnt+=1

#listing bucket objects for a perticular bucket using paginator
s3_cl=session.client(service_name='s3', region_name='us-east-1')
paginator=s3_cl.get_paginator('list_objects')
cnt=1
for each_page in paginator.paginate(Bucket=bucket_name):
     for each_obj in each_page['Contents']:
          print(cnt,each_obj['Key'])
          cnt+=1