import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_res=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-1")

'''
all_instances_ids=[]
#print(dir(ec2_con_res.instances))
for each_instaceIds in ec2_con_res.instances.all():
    all_instances_ids.append(each_instaceIds.id)
print("Starting all instances")
ec2_con_res.instances.start()
print("Waiting for all instances to get started") 
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=all_instances_ids)
print("Now your all instances are up and running")
'''
#Requirement is to start non_prod servers
#using ressource
all_instances_ids=[]
f1={"Name": "tag:Name", "Values":['non_prod']}
for each_item in ec2_con_res.instances.filter(Filters=[f1]):
    all_instances_ids.append(each_item.id)
    print("statind non_prod servers")
    each_item.start()
    print("waiting for non_prod servers to get started")
    waiter=ec2_con_cli.get_waiter('instance_running')
    waiter.wait(InstanceIds=all_instances_ids)
    print("Your non_prod servers are up and running")

#using client
all_instances_ids=[]
f1={"Name": "tag:Name", "Values":['non_prod']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    for each_instance in each_item['Instances']:
        all_instances_ids.append(each_instance['InstanceId'])
print("statind non_prod servers: ",all_instances_ids)
ec2_con_cli.start_instances(InstanceIds=all_instances_ids)
print("waiting for non_prod servers to get started")
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=all_instances_ids)
print("Your non_prod servers are up and running")