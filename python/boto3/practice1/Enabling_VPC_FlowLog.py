'''
 VPC flowlog captures all the traffic which is going in or out of your VPC.
 Traffic comming out your elastic network interface(eni).
 eg:- Accepted and rejected traffic
      In this example, SSH traffic (destination port 22, TCP protocol) from IP address 172.31.16.139 
      to network interface with private IP address is 172.31.16.21 and ID eni-1235b8ca123456789 in 
      account 123456789010 was allowed.
      2 123456789010 eni-1235b8ca123456789 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK  
      count_no        eni_id                 srcIP           destIP   srpt  dp  
      In this example, RDP traffic (destination port 3389, TCP protocol) to network interface eni-1235b8ca123456789 in account 123456789010 was rejected.
      2 123456789010 eni-1235b8ca123456789 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK
'''
import boto3
from botocore.exceptions import ClientError

ec2_client=boto3.client('ec2')
log_client=boto3.client('logs')
for vpc in ec2_client.describe_vpc()['Vpcs']:
       print(vpc['VpcId'])
       vpc_id=vpc['VpcId']

       log_group=vpc_id + "-flowlog" # vpc-dfag0ab9-flowlog
       try:
             response_create_log_group=log_client.create_log_group(logGroupName=log_group)
       except ClientError:
             print("Log group is already created for the follwing vpc",vpc_id)
       filter_flowlog={'Name':'resource-id','Values':[vpc_id]}
       responce_describe_flowlog=ec2_client.describe_flow_logs(Filters=[filter_flowlog])
       if len(responce_describe_flowlog['FlowLogs'])>0:
             print("Flow log is already enabled for the following vpc", vpc_id)
       else:
             response_create_flowlog=ec2_client.create_flow_logs(ResourceIds=[vpc_id],ResourceType='VPC',TrafficType='ALL',LogGroupName=log_group,DeliverLogsPermissionArn="arn:aws:iam:892515485494:role/flowlogrole")
             print("Flow log  is enabled for the following vpc", vpc_id)                        