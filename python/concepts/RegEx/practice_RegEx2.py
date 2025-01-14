import re

text="This is a pythonnnn and aaa asdhhhdddd bbbbb"
mypat1=r'\bpython{4}\b'
mypat2=r'\ba{3}\b'
print(re.findall(mypat1,text))
print(re.findall(mypat2,text))