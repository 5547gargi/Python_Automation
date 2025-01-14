import re

my_string="Python is easy and it simple"
# print(my_string.split("is")) # ['Python ', ' easy abd simple']
# print(my_string.split("it")) # ['Python is easy and ', ' simple']
print(re.split("i[st]",my_string)) # ['Python ', ' easy and ', ' simple']