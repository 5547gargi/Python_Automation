fos=open("/workspaces/Python_Automation/python/concepts/with_loop.txt",'r')
data=fos.readlines()
fos.close()

fod=open("/workspaces/Python_Automation/python/practice/abc.txt",'w')
for each_line in data:
    fod.write(each_line)
fod.close()