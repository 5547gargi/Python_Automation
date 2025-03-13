import boto3
session=boto3.session.Session(profile_name="dev_root")
'''
#using resource object
iam_res=session.resource(service_name="iam",region_name="us-east-1")
cnt=1
for each_user in iam_res.users.all():
    print(cnt,each_user.user_name)
    cnt=cnt+1
'''
#using client object
iam_cli=session.client(service_name="iam", region_name="us-east-1")
cnt=1
for each_user in iam_cli.list_users()['Users']:
    print(cnt, each_user['UserName'])
    cnt=cnt+1