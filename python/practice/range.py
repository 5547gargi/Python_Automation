'''
# Even no between 100
print(f"Even Numbers List : {list(range(0,101,2))}")

# Odd numbers between 100
print(f"Odd Numbers List :{list(range(1,100,2))}")
'''   
my_list=[2,5,6,"python",18,36]
# print(list(range(len(my_list))))
# print(my_list[0])
for each_index in range(len(my_list)):
    print(f"Index --> {each_index} : value --> {my_list[each_index]}")