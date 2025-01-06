import subprocess

'''
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
'''
cmd="java -version"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0:
    if bool(o)==True:
        print(o)
    if bool(o)==False and bool(e)==True:
        # print(e.split('"')[1])
        print(e.splitlines()[0].split()[2].strip("\""))
else:
    print(e)