import csv

req_file="/workspaces/Python_Automation/python/practice/newinfo.csv"
fo=open(req_file,"r")
# content=csv.reader(fo) # for coma separated csv file *No need to mention: delimiter="," exceptionally 
content=csv.reader(fo,delimiter="|") # for | separated csv file *Need to mention: delimiter="|" explicitly 
for each in content:
    print(each)
fo.close()
