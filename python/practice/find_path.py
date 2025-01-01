import os
import sys

path=input("Enter your directoryPath : ")
if os.path.exists(path):
    list_of_files_dir=os.listdir(path)
else:
    print("Please provide valid path !!!")
    sys.exit()

for each_fileOr_dir in list_of_files_dir:
    fileOr_dir_path=os.path.join(path,each_fileOr_dir)
    if os.path.isfile(fileOr_dir_path):
        print(f"{fileOr_dir_path} is a File.")
    else:
        print(f"{fileOr_dir_path} is a Directory.")
        print(os.listdir(fileOr_dir_path))
