'''
print("Welcome to exceptions")
try:
    fo=open(host.txt)
    print(fo.read())
    fo.close()
except Exception as e:
    print(e)
'''
my_list=[2,4,6]
try:
    print(my_list[3])
except Exception as e:
    print(e)