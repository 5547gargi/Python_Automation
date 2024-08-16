# Create an array of integers and print its elements.
#L1 = [2,3,9,5,8,4,7,1]
#print(f"List : {L1}")
'''
for i in range(len(L1)):
  #  print(f"List : {L1[i]}")
  L1[i]*=2
print(f"List : {L1}")
'''
# Iterate through an array using a loop.
#for i in L1:
 #   print(i)
'''
index=0
while index < len(L1):
    print(f"List element : {L1[index]}")
    index +=1
 '''

# Removing duplicate items from list
'''
my_list = [1, 2, 3, 2, 4, 1,3,2]
unique_list = list(set(my_list))
print(unique_list)
'''
'''
my_list = [1, 2, 3, 2, 4, 1,5,8,3,5,9,8]
unique_list = []
seen = set()

for element in my_list:
    if element not in seen:
        unique_list.append(element)
        print(f"unique_list : {unique_list}")
        seen.add(element)
        print(f"seen : {seen}")

print(f"unique_list : {unique_list}") 
'''


