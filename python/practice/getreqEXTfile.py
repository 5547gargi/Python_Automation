import os
req_path=input("Enter your Directory_Path : ")

if os.path.isfile(req_path):
    print(f"The given path {req_path} is a file; Please provide Directory Path.")
else:
    allfiles_dir=os.listdir(req_path)
    if len(allfiles_dir)==0:
        print(f"The given path {req_path} is empty")
    else:
        req_extension=input("Enter the requored file extension .py/.sh/.log/.txt : ")
        req_files=[]
        for each_file in allfiles_dir:
            if each_file.endswith(req_extension):
                req_files.append(each_file)
        print(req_files)