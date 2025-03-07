#Mail Alert : get AWS EC2 instance status when it stopped
#Lambda Function :--> IAM Role(Ec2,sns)
import boto3
def lambda_handler(event, context):
     #ec2_con=boto3.resource(service_name="ec2",region_name="us-east-1")
     # my_ins=ec2_con.Instance("i-0f9f8f8f8f8f8f8f8")
     # print(my_ins.state['Name'])
     sns_client=boto3.client("sns", region_name="us-east-1")

     sns_client.publish(
        TopicArn='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        Subject="EC2 Instance Status",
        Message="Ec2 Instance got stopped")
'''
To trigger the lambda function Automatically, we have to go to CLOUDWATCH And create a Rule.
By selecting the event pattern following by selecting Service name, Event Type , specific chage, for all instances or specific instance
also adding the target lambda function name to it.
After that by giving a RULE_NAME create the rule.
'''      

'''
def lambda_handler(event, context):
    # Create an SNS client
    sns = boto3.client('sns','us-east-1')

    # Create an EC2 client
    ec2 = boto3.client('ec2', 'us-east-1')

    # Get the instance ID from the event
    instance_id = event['detail']['instance-id']

    # Get the instance status
    response = ec2.describe_instance_status(InstanceIds=[instance_id])

    # Check if the instance is stopped
    if response['InstanceStatuses'][0]['InstanceState']['Name'] == 'stopped':
        # Send an email using SNS
        sns.publish(
            TopicArn='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            Message='Instance ' + instance_id + ' is stopped',
            Subject='Instance Stopped'
        )
'''