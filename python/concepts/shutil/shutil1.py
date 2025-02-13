import shutil

# 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'
# copy file -->
src="/home/Automation/working_with_remote_server.py"
dest="/home/Automation/working_with_remote_server.py_bkp"

shutil.copyfile(src,dest)
shutil.copy(src,dest) # to retain same file permissions for src and dest
shutil.copy2(src,dest) # same metedata from source to destination

shutil.copymode(src,dest) # here same file permissions to be given for destination file without copying the content of src
shutil.copystat(src,dest) # here same time stamp willbe given to destination file without copying it

f1=open('xyz.txt','r')
f2=open('pqr.txt','w')
shutil.copyfileobj(f1,f2) # copying file content of xyz.txt to pqr.txt

shutil.copytree(src,dest) # here to copy the entire directory structure including all files and folders recursively from src to dest
shutil.rmtree(dest) # to remove the entire directory structure recursively
