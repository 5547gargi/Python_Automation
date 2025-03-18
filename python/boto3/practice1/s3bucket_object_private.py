import boto3

s3=boto3.client('s3')
print(s3.list_buckets()['Buckets'])
for bucket in s3.list_buckets()['Buckets']:
     print(bucket['Name'])
     bucket_name=bucket['Name']

print(s3.list_objects(Bucket=bucket_name))
s3_objects=s3.list_objects(Bucket=bucket_name)
for object in s3_objects['Contents']:
     print(object['Key'])
     object_key=object['Key']

responce=s3.get_object(Bucket=bucket_name,Key=object_key)
# print(responce['Body'].read().decode('utf-8'))
print(response)
if len(responce['Grants'])>1:
     print("Object is public")
     print(f"The bucket {bucket_name} with key {object_key} is now marked as private")
     s3.put_object_acl(Bucket=bucket_name, Key=object_key, ACL='private')