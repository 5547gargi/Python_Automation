import re

text="""This is for 
python and there are two major
versions python2 and python3 in future python4"""
mypat=r"\bpython[23]?\b"
mypat1=r"\bpython\d?\b"
# print(re.findall(mypat1,text))
match_obj=re.search(mypat,text)
print(match_obj.group())
print(match_obj.start())
print(match_obj.end())
print("length :",match_obj.end()-match_obj.start())