import csv
'''
req_file="/workspaces/Python_Automation/python/practice/newinfo.csv"
fo=open(req_file,"r")
csv_reader=csv.reader(fo,delimiter="|")
for each_row in csv_reader:
    print(each_row)
fo.close()
'''
req_file="/workspaces/Python_Automation/python/concepts/demo.csv"
fo=open(req_file,'w')
csv_writer=csv.writer(fo,delimiter=",")
'''
csv_writer.writerow(['Sl_No','Name','Age'])
csv_writer.writerow([1,'radha','8'])
csv_writer.writerow([2,'durga',16])
'''
mydata=[['Sl_No','Name','Age'],[1,'Laxmi',12],[2,'Meenakshi',16]]
csv_writer.writerows(mydata)
fo.close()