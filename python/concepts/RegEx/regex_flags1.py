import re

text="this is a string ThIs is a new String THIS"
mypat=r"this"
# print(re.findall(mypat,text,re.IGNORECASE))
# print(re.findall(mypat,text,re.I))

text1="""this is a string
this is second string eNd
This is third string End
asdf thIs end"""
mypat2=r"^this"
mypat3=r"end"
print(re.findall(mypat2,text1,re.M|re.I))
print(re.findall(mypat3,text1,re.M|re.I))