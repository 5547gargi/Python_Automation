import re
my_str="This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat=r"python[23]?"
'''
# Syntax : split(pattern, string, maxsplit=0, flags=0)

print(re.split(my_pat,my_str,flags=re.I))
print(re.split(my_pat,my_str,maxsplit=1,flags=re.I))
print(re.split(my_pat,my_str,maxsplit=2,flags=re.I))
'''
# Syntax : sub(pattern, repl, string, count=0, flags=0)
print(re.sub(my_pat,'java',my_str))
print(re.sub(my_pat,'java',my_str,flags=re.I))
print(re.sub(my_pat,'java',my_str,count=2,flags=re.I))

print(re.subn(my_pat,'go',my_str,flags=re.I))
#('This is about go and go is very easy and we are having go vers and go vers', 4)