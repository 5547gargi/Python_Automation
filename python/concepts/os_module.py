import os

'''
print(os.sep)
print(os.getcwd())
os.chdir("/workspaces/Python_Automation/python/concepts")
print(os.getcwd())
print(os.listdir())
os.mkdir("table") ; to make directory in the present location 
os.makedirs("/workspaces/Python_Automation/python/concepts/test/temp") ; to make directory in any location (Recursive directory creation function)
os.remove(path)
os.removedirs(path) (Remove directories recursively)
os.rename(srcPath,destPath)
print(os.environ)
print(os.geteuid())
print(os.getgid())
print(os.getpid())
'''
'''
print(os.path.sep)
path="/workspaces/Python_Automation/python/concepts/test.py"
path1="/workspaces/Python_Automation"
path2="python/concepts/test.py"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join(path1,path2))
print(os.path.split(path))  # it will separate the path by head and tail.
print(os.path.exists(path))

if os.path.isfile(path) :
    print(f"{path} is a file")
else:
    print(f"{path} is a directory")
'''

