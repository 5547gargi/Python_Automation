# Automating the start and stop EC2 instances for test evironment using AWS Lambda and Python
# Every day 
# start EC2 instances at 8 am Monday-Friday
# stop Ec2 instances at 5 pm Monday-Friday
import json
import boto3

def lambda_handler(event, context):
      #ToDo implement
      ec2_con_res=boto3.resource(service_name="ec2",region_name="us-east-1")
      test_env_filter={"Name": "tag:Environment", "Values": ['test']}
      for each_in in ec2_con_res.instances.filter(Filters=[test_env_filter]):
         #print(each_in.id, each_in.state['Name'])
         each_in.start()
      return {
          'statusCode': 200,
          'body': json.dumps('Hello from Lambda!')
      }
'''
To implement as cornjon or schedule the job, you have to go to CloudWatch and create a rule.
 > Two types of Event source you will get, Event pattern and Schedule
 > go for schedule
     > Select Corn Expression for every day from monday-friday at 8am
     > Corn Expression : 0 8 ? * MON-FRI *
 > After this select the Targets(means perticular lambda job)    
'''

'''
# Automating the start and stop EC2 instances for test evironment using AWS Lambda and Python
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_ec2_instances(ec2_client):
    """Get list of EC2 instances with test environment tag"""
    filters = [{'Name': 'tag:Environment', 'Values': ['test']}]
    response = ec2_client.describe_instances(Filters=filters)

    instances = []
    for reservation in response['Reservations']:
        instances.extend(reservation['Instances'])
    return instances

def start_instances(instance_ids, ec2_client):
    """Start the specified EC2 instances"""
    try:
        ec2_client.start_instances(InstanceIds=instance_ids)
        logger.info(f"Started instances: {instance_ids}")

    except Exception as e:
        logger.error(f"Error starting instances: {str(e)}")

def stop_instances(instance_ids, ec2_client):

    """Stop the specified EC2 instances"""
    try:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        logger.info(f"Stopped instances: {instance_ids}")
    except Exception as e:
        logger.error(f"Error stopping instances: {str(e)}")

def lambda_handler(event, context):

    """Main Lambda handler function"""
    ec2_client = boto3.client('ec2')
    action = event.get('action', '').lower()
    
    instances = get_ec2_instances(ec2_client)
    instance_ids = [instance['InstanceId'] for instance in instances]
    
    if action == 'start':
        start_instances(instance_ids, ec2_client)
    elif action == 'stop':
        stop_instances(instance_ids, ec2_client)
    else:
        logger.error(f"Invalid action: {action}")

    return {
        'statusCode': 200,
        'body': f"Action {action} completed for test environment instances"
    }
'''    