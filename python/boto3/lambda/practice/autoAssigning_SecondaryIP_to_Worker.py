#Assigning secondary IP of Master Server to Worker Server when Master server goes down
import json
import boto3

def lambda_handler(event, context):
     master_id='xxxxxx'
     worker_id='xxxxxx'
     secondary_ip='xxxxxx'
     ec2_res = boto3.resource('ec2','us-east-1')
     primary_instance = ec2_res.Instance(master_id)
     if primary_instance.state['Name'] == 'running':
         print('Master Server is up and running; No need of Modification')
     else:
         print('Master Server is down; Modifying Worker Server')
         secondary_instance = ec2_res.Instance(worker_id)
         primary_network_interface = primary_instance.network_interfaces_attribute[0]
         secondary_network_interface = secondary_instance.network_interfaces_attribute[0]
         primary_network_interface_id = primary_network_interface['NetworkInterfaceId']
         secondary_network_interface_id = secondary_network_interface['NetworkInterfaceId']
         ec2_cli = boto3.client('ec2', 'us-east-1')
         ec2_cli.unassign_private_ip_addresses(NetworkInterfaceId=primary_network_interface_id, PrivateIpAddresses=[secondary_ip])
         ec2_cli.assign_private_ip_addresses(AllowReassignment=True,NetworkInterfaceId=secondary_network_interface_id, PrivateIpAddresses=[secondary_ip])
     return None     
         
    


  