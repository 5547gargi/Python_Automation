import re
'''

text="This 1is @ python3 and it_is easy - 2 learn"
mypat1="is"
mypat2="i[st]"
mypat3="[@s]"
mypat4="[a-d]" #"[a,b,c,d]"
mypat5="\w"
mypat6="\w\w"
mypat7="\W"
mypat8="\d" # "\d\d" matches for double digits number
mypat9="\d\d"
mypat10="." # matches every character except newline ; "\." matches for . only 
print(re.findall(mypat1,text))
print(len(re.findall(mypat1,text)))
print(re.findall(mypat2,text))
print(re.findall(mypat3,text))
print(re.findall(mypat4,text))
print(re.findall(mypat5,text))
print(re.findall(mypat6,text))
print(re.findall(mypat7,text))
print(re.findall(mypat8,text))
print(re.findall(mypat9,text))
print(re.findall(mypat10,text))
'''

text1="Ip of my server is : 127.221.321  ttl 12586"
newpat="\d\d\d\.\d\d\d\.\d\d\d"
print(re.findall(newpat,text1))