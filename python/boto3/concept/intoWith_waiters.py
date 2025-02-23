import boto3
import time
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_res=aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

'''
#Using resource
my_inst_ob=ec2_con_res.Instance("i-0b1a1c2d3e4f5g6h7")
print("Starting given instance")
my_inst_ob.start()
my_inst_ob.wait_until_running() # Resource waiters waits for 200sec(40 checks after every 5 sec)
print("Now instance is up and running")
'''
'''
#Using client
print("Starting given instance")
ec2_con_cli.start_instances(InstanceIds=['i-0b1a1c2d3e4f5g6h7'])
print("Waiting for Instance starting")
my_inst_ob_waiter=ec2_con_cli.get_waiter('instance_running')
my_inst_ob_waiter.wait(InstanceIds=['i-0b1a1c2d3e4f5g6h7'])  # 40 checks after every 15sec
print("Now instance is up and running")
'''
'''
while True:
    my_inst_ob=ec2_con_res.Instance("i-0b1a1c2d3e4f5g6h7")
    print("The current state of instance is: ", my_inst_ob.state['Name'])
    if my_inst_ob.state['Name'] == 'running':
        break
    time.sleep(5)
'''

# clubing uses of resource and client
my_inst_ob=ec2_con_res.Instance("i-0b1a1c2d3e4f5g6h7")
print("Starting given instance")
my_inst_ob.start()
print("Waiting for Instance starting")
my_inst_ob_waiter=ec2_con_cli.get_waiter('instance_running')
my_inst_ob_waiter.wait(InstanceIds=['i-0b1a1c2d3e4f5g6h7'])  # 40 checks after every 15sec
print("Now instance is up and running")