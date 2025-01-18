# Transfer a file from local server to remote server and viceversa

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='54.165.97.91',username='ec2-user',password='paramaiko123',port=22)
sftp_client=ssh.open_sftp()
sftp_client.get('/home/ec2-user/sampledata.txt','/workspaces/Python_Automation')
# we can direct 'sftp_clint' explicity to a perticular remote drectory; so that no need to provide complete remote path 
sftp_client.chdir("/home/ec2-user")
print(sftp_client.getcwd())
sftp_client.get('demo.txt','c:\\users\\Automation\\Desktop\\dowmload_demofile.txt')
# to send a file from local sever to remote server
sftp_client.put('file_transfer.py','/home/ec2-user/file_transfer.py')
sftp_client.close()
ssh.close()