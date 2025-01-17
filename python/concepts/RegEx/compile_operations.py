import re
text="This is about python. Python is easy and we have two major versions python2 and python3"
mypat=r"\bpython[23]?\b"
'''
print(re.search(mypat,text))
print(re.findall(mypat,text,flags=re.I))
print(re.split(mypat,text,flags=re.I))
'''
pat_obj=re.compile(mypat,flags=re.I)
print(pat_obj)
print(pat_obj.search(text))
print(pat_obj.findall(text))

# re.findall(mypat,text) ===> re.compile(mypat).findall(text)
