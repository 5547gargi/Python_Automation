import csv

req_file="/workspaces/Python_Automation/python/practice/newinfo.csv"
fo=open(req_file,"r")
# content=csv.reader(fo) # for coma separated csv file *No need to mention: delimiter="," exceptionally 
content=csv.reader(fo,delimiter="|") # for | separated csv file *Need to mention: delimiter="|" explicitly 
# print(list(content))
# print(f'The header is :\n{list(content)[0]}')
# header=next(content)
# print("the header is : ",header)
print("the no of rows are : ",len(list(content))-1)
'''
for each in content:
    print(each)
'''
fo.close()
