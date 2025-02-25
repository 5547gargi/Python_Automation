'''
 Here we won't create aws management console object  as we have attached IAM role to our ec2 instance.
 we will use boto3 to connect to aws services.
'''
import boto3

ec2_con_res=boto3.resource(service_name="ec2",region_name="us-east-1")
for each_instance in ec2_con_res.instances.all():
    print(each_instance.id,each_instance.state,each_instance.instance_type,each_instance.launch_time)