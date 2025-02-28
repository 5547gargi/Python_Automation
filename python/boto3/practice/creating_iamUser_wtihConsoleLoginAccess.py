import boto3
from random import choice

def get_iam_client():
     session=boto3.session.Session(profile_name="dev_root")
     iam_client=session.client(service_name="iam",region_name="us-east-1")
     return iam_client

def get_random_password():
     return "".join(choice("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+") for each_char in range(12))

def main():
     iam_client=get_iam_client()
     iam_user_name="testuser1"
     passwd=get_random_password()
     policy_arn="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
     try:
          iam_client.create_user(UserName=iam_user_name)
          iam_client.create_login_profile(UserName=iam_user_name,Password=passwd,PasswordResetRequired=False)
          iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn=policy_arn)
          # print(f"IAM User Created {iam_user_name} and password is {passwd}")
          print("IAM USER Name ={} and Password={}".format(iam_user_name,passwd))
          return None
     except Exception as e:
          print(f"Error creating IAM User: {e}")
          return e
     

if __name__=="__main__":
     main()