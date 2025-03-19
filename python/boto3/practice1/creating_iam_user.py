import boto3
import argparse
import string
import secrets
from random import choice

'''
iam_client=boto3.client('iam')
iam_client.create_user(UserName='XXXXXXXX')
# if we run this code again it will throw an error/exception(EntityAlreadyExistsException) because the user already exists
# so we need to delete the user first
iam_client.delete_user(UserName='XXXXXXXX')

def random_password_generator():
    len_of_password=8
    valid_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    random_password="".join(choice(valid_chars) for each_char in range(len_of_password))
    return random_password
'''
def random_passsword_generator(length=12):
      #Generating a random password with specified length
      chars=string.ascii_letters + string.digits + string.punctuation
      password=""
      for each_char in range(length):
         password+=secrets.choice(chars)
      return password   
             
       
def create_iam_user(userName):
     iam_client=boto3.client('iam')
     try:
         iam_client.get_user(UserName=userName)
         print(f'User {userName} already exists')
     except iam_client.exceptions.NoSuchEntityException:
         try:
             iam_client.create_user(UserName=userName)
             print('User created')
         except Exception as e:
             print('Error while creating user {userName} {e}')

if __name__ == '__main__':
      parser=argparse.ArgumentParser(description='Creating IAM user')
      # parser.add_argument('-u','--userName',type=str,required=True)
      parser.add_argument('--userName',type=str,help='The name of IAM user, owner wants to create',required=True)
      args=parser.parse_args()
      create_iam_user(args.userName)