# In orser to list_access_keys --> We need user
import boto3
from datetime import datetime, timezone, timedelta
client=boto3.client("iam")
paginator=client.get_paginator('list_users')
current_date=datetime.now(timezone.utc)
max_key_age=45
for response in paginator.paginate():
     #print(response)
     for each_user in response['Users']:
         # print(each_user['UserName'])
         # print(each_user['Arn'])
         # print(each_user['CreateDate'])
         # print(each_user['UserId'])
         username = each_user['UserName']
         # list_key= client.list_access_keys(UserName=username)
         for access_key in client.list_access_keys(UserName=username)['AccessKeyMetadata']:
             # print(access_key['UserName'])
             # print(access_key['AccessKeyId'])
             # print(access_key['Status'])
             # print(access_key['CreateDate'])
             access_key_id = access_key['AccessKeyId']
             key_creation_date = access_key['CreateDate']
             age=(current_date-key_creation_date).days
             if age > max_key_age:
                 print(f"Access key {access_key_id} is older than {max_key_age} days. It will be deleted.")
                 client.update_access_key(UserName=username, AccessKeyId=access_key_id, Status='Inactive')
                 #  client.delete_access_key(UserName=username, AccessKeyId=access_key_id)
                 #  print(f"Access key {access_key_id} has been deleted.")
                 print("--------------------------------------------------")