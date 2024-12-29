import sys
# user_str=input("Enter your string : ")
# user_action=input("Enter your action on your string (<lower>/<upper>/<title>): ")

if len(sys.argv) !=3 :
    print(f"{sys.argv[0]} <req` action> <lower|upper|title>")
    sys.exit()
user_str=sys.argv[1]
user_action=sys.argv[2]

if user_action=="upper" :
    print(user_str.upper())
elif user_action=="lower" :
    print(user_str.lower())
elif user_action=="title" :
    print(user_str.title())
else :
    print(f"{user_action} not a vaild option. \nPlease enter valid options <lower>/<upper>/<title>")