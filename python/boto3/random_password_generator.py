import string
import secrets
from random import choice

len_of_password=12
valid_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

#print (choice(valid_chars))
password=[]
#using for loop
for each_char in range(len_of_password):
    password.append(choice(valid_chars))
# print(password)
print("using for loop")
print ("".join(password))

#using whileloop
password=[]
while len(password)<len_of_password:
    password.append(choice(valid_chars))
print("using while loop")    
print("".join(password))

#using list comp
random_password="".join(choice(valid_chars) for each_char in range(len_of_password))
print("using list comprehension")
print(random_password)

def random_passsword_generator(length=12):
      #Generating a random password with specified length
      chars=string.ascii_letters + string.digits + string.punctuation
      password=""
      for each_char in range(length):
         password+=secrets.choice(chars)
      return password 

print("using secrets module")
print(random_passsword_generator())