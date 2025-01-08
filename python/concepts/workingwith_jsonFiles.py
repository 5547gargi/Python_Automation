import json
'''
req_file="/workspaces/Python_Automation/python/concepts/demo.json"
fo=open(req_file,'r')
# print(type(fo.read()))
# print(type(json.load(fo)))
# print(json.load(fo).get("glossary"))
print(json.load(fo))
fo.close()
'''
my_dict={'Name':'Gargi','Skills':['Python','shell','yaml','AWS']}
req_file="/workspaces/Python_Automation/python/concepts/my_info.json"
fo=open(req_file,'w')
json.dump(my_dict,fo,indent=4)
fo.close()