import subprocess

cmd="echo $HOME"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
output,error=sp.communicate()
print(f'The retuen code : {rc}')
print(f'The Output : \n{output.splitlines()}')
print(f'The Error : \n{error.splitlines()}')

'''
# cmd="ls -lrt".split()
cmd=['ls']
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
output,error=sp.communicate()
print(f'The retuen code : {rc}')
print(f'The Output : \n{output.splitlines()}')
print(f'The Error : \n{error.splitlines()}')
'''