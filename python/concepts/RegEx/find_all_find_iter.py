import re
text="This is for python and there are two major versions python2 and python3 in future python4"
mypat=r"\bpython[23]?\b"
# print(re.search(mypat,text))
# print(re.findall(mypat,text))
# print(len(re.findall(mypat,text)))

for each_obj in re.finditer(mypat,text):
    print(f'The match is : {each_obj.group()} starting index is : {each_obj.start()} ending Index is : {each_obj.end()-1}')