import boto3 

aws_management_console=boto3.session.Session(profie_name="root")
s3_management_console=aws_management_console.resource('s3')

for each_bucket in s3_management_console.all():
    print(each_bucket.name)