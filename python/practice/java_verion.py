import subprocess

cmd=['java','-version']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
output,error=sp.communicate()
if rc==0:
    for each_line in error.splitlines():
        if "version" in each_line:
            print(each_line.split('"')[1])
else:
    print("Command execution Failed !!",error)