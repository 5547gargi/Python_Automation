myContent=['this is using iteraion 1','this is using iteraion 2','this is using iteraion 3']
'''
fo=open("with_loop.txt",'a')
for each_line in myContent:
    fo.write(each_line+"\n")
fo.close()
'''
'''
fo=open("with_loop.txt",'r')
data=fo.read()
print(data)
fo.close()
'''
fo=open("with_loop.txt",'r')
data=fo.readlines()
fo.close()

for each in range(3):
    print(data[each])