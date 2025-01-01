import os

path=input("Enter your path : ")
if os.path.exists(path):
    print(f"Given path is exist in the system.")
    if os.path.isfile(path):
        print(f"The given path : {path} is a File.")
    else:
        print(f"The given path : {path} is a Directory.")
else:
    print(f"given path : {path} not exists in the system.")
