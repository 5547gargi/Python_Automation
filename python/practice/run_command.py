import os
import time
import platform

def mycode(cmd1,cmd2):
    print("Please wait...")
    time.sleep(2)
    os.system(cmd1)
    print("Displaying filrs and directories")
    time.sleep(2)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode("cls","dir")
else:
    mycode("clear","ls -lrt")