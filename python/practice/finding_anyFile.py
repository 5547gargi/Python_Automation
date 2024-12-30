# Write down a platform independent script ; How to do a system wide search for a file ?
import os
import string
import platform

req_fileName=input("Enter your file Name to search : ")
if platform.system=="Windows":
    print("----------- Please Wait Finding your file_Path on Windows System ----------")
    pd_names=string.ascii_uppercase
    vd_names=[]
    for each_drive in pd_names:
        if os.path.exists(each_drive+":\\"):
            #print(each_drive)
            vd_names.append(each_drive+":\\")
    print(vd_names)

    for each_drive in vd_names:
        #print(each_drive)
        for r,d,f in os.walk(each_drive):
            for each_file in f:
                if each_file==req_file:
                    print(os.path.join(r,each_file))
else:
    print("----------- Please Wait Finding your file_Path on Linux System ----------")
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file==req_fileName:
                print(os.path.join(r,each_file))