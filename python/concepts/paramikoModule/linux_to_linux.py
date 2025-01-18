import paramiko
#setting up a client by using paramiko 
ssh=paramiko.SSHClient()
#Avoiding paramiko.ssh excepiton.SSHException: Server '3.92.79.119' not found in known hosts 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#conncet to  remote server by using password
# ssh.connect(hostname='3.92.79.119',username='ec2-user',password='paramiko123',port=22)
# #conncet to  remote server by using private key
# ssh.connect(hostname='3.92.79.119',username='ec2-user',key_filename='demo_private_key',port=22)

ssh.connect(hostname='3.92.79.119',username='ec2-user',key_filename='home/automation/.ssh/id_rsa',port=22)
stdin, stdout, stderr = ssh.exec_command('whoami')
stdin, stdout, stderr = ssh.exec_command('uptime')
stdin, stdout, stderr = ssh.exec_command('free -m')

print("The output is : ")
print(stdout.read)
print("The error is :")
print(stderr.read)