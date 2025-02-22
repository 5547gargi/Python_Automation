import boto3
import sys
aws_mag_con = boto3.session.Session(profile_name="root")
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mag_con.client(service_name="ec2", region_name="us-east-1")

'''
while True:
    print("This script performs the following actions on ec2 instance")
    print("""
        1. start
        2. stop
        3. terminate
        4. Exit
        """)
    opt=int(input("Enter the option: "))
    if opt==1:
         Instance_Id=input("Enter your instance id: ")
         my_req_instance_object=ec2_con_re.Instance(Instance_Id)
         #print(dir(my_req_instance_object))
         print("Starting ec2 instance.....")
         my_req_instance_object.start()
    elif opt==2:
         Instance_Id=input("Enter your instance id: ")
         my_req_instance_object=ec2_con_re.Instance(Instance_Id)
         print("Stopping ec2 instance.....")
         my_req_instance_object.stop()
    elif opt==3:
         Instance_Id=input("Enter your instance id: ")
         my_req_instance_object=ec2_con_re.Instance(Instance_Id)
         print("Terminating ec2 instance.....")
         my_req_instance_object.terminate()
    elif opt==4:
         print("Thanks for using this script")
         sys.exit()
    else:
         print("Invalid option! Please try once again")
'''
#using client
while True:
    print("This script performs the following actions on ec2 instance")
    print("""
        1. start
        2. stop
        3. terminate
        4. Exit
        """)
    opt=int(input("Enter the option: "))
    if opt==1:
         Instance_Id=input("Enter your instance id: ")
         print("Starting ec2 instance.....")
         ec2_con_cli.start_instances(InstanceIds=[Instance_Id])
    elif opt==2:
         Instance_Id=input("Enter your instance id: ")
         print("Stopping ec2 instance.....")
         ec2_con_cli.stop_instances(InstanceIds=[Instance_Id])
    elif opt==3:
         Instance_Id=input("Enter your instance id: ")
         print("Terminating ec2 instance.....")
         ec2_con_cli.terminate_instances(InstanceIds=[Instance_Id])
    elif opt==4:
         print("Thanks for using this script")
         sys.exit()
    else:
         print("Invalid option! Please try once again")