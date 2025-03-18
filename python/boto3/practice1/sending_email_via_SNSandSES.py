import boto3

ec2= boto3.resource('ec2')

#sending email via sns
sns=boto3.client('sns')
response_createTopic=sns.create_topic(Name='boto3-sns')
response_subscibe=sns.subscribe(TopicArn=response_createTopic['TopicArn'],Protocol='email',Endpoint='gsd@gmail.com',ReturnSubscriptionArn=True)

#sending email via ses
ses=boto3.client('ses')

vol_filter={'Name':'status','Values':['available']}
for vol in ec2.volumes.filter(Filters=[vol_filter]):
     print(vol.id,vol.state)
     vol_id=vol.id
     volume=ec2.Volume(vol_id)
     print('Deleting EBS Volumes',vol_id)
     volume.delete()
     print('EBS Volume Deleted')
     sns.publish(TopicArn=response_createTopic['TopicArn'], Message=f'EBS Volume {vol_id} Deleted', Subject='EBS Volume Deleted')
     ses.send_email(Source='office@gmail.com', Destination={'ToAddresses':['gsd@gmail.com']}, Message={'Subject':{'Data':(f'EBS Volume {vol_id} Deleted')}, 'Body':{'Text':{'Data':'EBS Volume Deleted'}}})