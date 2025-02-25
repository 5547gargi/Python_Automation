from random import choice

len_of_password=8
valid_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

#print (choice(valid_chars))
password=[]
#using for loop
for each_char in range(len_of_password):
    password.append(choice(valid_chars))
# print(password)
print ("".join(password))

#using whileloop
password=[]
while len(password)<len_of_password:
    password.append(choice(valid_chars))
print("".join(password))

random_password="".join(choice(valid_chars) for each_char in range(len_of_password))
print(random_password)