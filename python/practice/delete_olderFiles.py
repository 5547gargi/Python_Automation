import os
import sys
import datetime

req_path=input("Enter your path : ")
age=3
if not os.path.exists(req_path):
    print("Please provide Valid Path.")
    sys.exit(1)
if os.path.isfile(req_path):
    print("Please provide directory path")
    sys.exit(2)

today=datetime.datetime.now()
for each_file in os.listdir(req_path):
    eachFile_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file):
        file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(eachFile_path))
        # print(dir(today-file_cre_date))
        dif_days=(today-file_cre_date).days
        if dif_days > age:
            print(eachFile_path,dif_days)