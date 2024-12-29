import getpass

db_pass=getpass.getpass()
print(f"The entered password is ; {db_pass}")
env_user=getpass.getuser()
print(f"The env_user is : {env_user}")