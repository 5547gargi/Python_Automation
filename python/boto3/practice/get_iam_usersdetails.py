import boto3
import datetime

session=boto3.session.Session(profile_name="root")
iam_con_re=session.resource(service_name="iam")

'''
#Get details of any iam user
iam_user_obj=iam_con_re.User("s3_developer")
print(iam_user_obj.user_name,iam_user_obj.user_id,iam_user_obj.arn,iam_user_obj.create_date.strftime("%Y-%m-%d"))
'''
#get details of all iam users
for each_user in iam_con_re.users.all():
     print(each_user.user_name, each_user.user_id, each_user.arn, each_user.create_date.strftime("%Y-%m-%d"))