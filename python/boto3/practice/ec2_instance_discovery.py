import boto3
import csv

'''
#using resource
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name="us-east-1")
cnt=1
csv_ob=open("inventory.csv", "w", newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO", "InstanceID", "InstanceType", "Architecture", "LaunchTime", "PrivateIP"])
for each in ec2_con_re.instances.all():
    print(cnt, each,each.instance_id, each.instance_type,each.architecture, each.launch_time.strftime("%Y-%m-%d"), each.private_ip_address)
    csv_w.writerow([cnt, each.instance_id, each.instance_type, each.architecture, each.launch_time.strftime("%Y-%m-%d"), each.private_ip_address])
    cnt+=1
csv_ob.close()
'''
#using client
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-1")
cnt=1
csv_ob=open("inventory.csv", "w", newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO", "InstanceID", "InstanceType", "Architecture", "LaunchTime", "PrivateIP"])
for each in ec2_con_cli.describe_instances()['Reservations']:
    for each_in in each['Instances']:
        print(cnt, each_in['InstanceId'], each_in['InstanceType'], each_in['Architecture'], each_in['LaunchTime'].strftime("%Y-%m-%d"), each_in['PrivateIpAddress'])
        csv_w.writerow([cnt, each_in['InstanceId'], each_in['InstanceType'], each_in['Architecture'], each_in['LaunchTime'].strftime("%Y-%m-%d"), each_in['PrivateIpAddress']])
        cnt+=1
        #print(each_in)
csv_ob.close()