import re

text="it isa python alearnr and it is easy to learn"
mypat1="i[ts]"
mypat2="^i[ts]"
mypat3="learn$"
mypat4="\\blearn"
mypat5=r"\bpython\b"
mypat6=r"\Blearn\B"
print(re.findall(mypat1,text))
print(re.findall(mypat2,text))
print(re.findall(mypat3,text))
print(re.findall(mypat4,text))
print(re.findall(mypat5,text))
print(re.findall(mypat6,text))