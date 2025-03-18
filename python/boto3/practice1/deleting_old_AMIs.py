import boto3
import datetime
from dateutil.parser import parse

session=boto3.client('ec2')
current_date=datetime.datetime.now()
max_ami_age=45

my_ami=session.describe_images(Owners=['self'])['Images']
for ami in my_ami:
     creation_date=ami['CreationDate']
     creation_date_parse=parse(creation_date).replace(tzinfo=None)
     # print(creation_date_parse)
     image_id=ami['ImageId']
     diff_in_days=(current_date-creation_date_parse).days
     if diff_in_days > max_ami_age:
         print('Cleaning old ami greater than sop',image_id)
         session.deregister_image(ImageId=image_id,Dryun=True)