import boto3
aws_mag_con=boto3.session.Session(profile_name='root')
ec2_con_res=aws_mag_con.resource(service_name='ec2',region_name='us-east-1')

# On ec2_con_res object, talking about all,limit,filter
'''
#all
for each_item in ec2_con_res.instances.all():
     print(each_item) 
'''
'''     
#limit     
for each_item in ec2_con_res.instances.limit(1):
     print(each_item)
'''
# Filter
f1={"Name": "instance-state-name", "Values":['running']}
f2={"Name": "instance-type", "Values":['t2.micro']}
for each_item in ec2_con_res.instances.filter(Filters=[f1,f2]):
     print(each_item)     