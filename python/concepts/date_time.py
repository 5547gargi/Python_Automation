import datetime
import pytz
ist=pytz.timezone('Asia/Kolkata')
# print(datetime.datetime.now())
# print(datetime.datetime.now(ist),type(ist))
# print(datetime.datetime.now(ist))
# print(datetime.datetime.today())
# print(datetime.datetime.now(ist).date())
# print(datetime.datetime.now(ist).year)
# print(datetime.datetime.now(ist).day)
# print(datetime.datetime.now(ist).month)
# print(datetime.datetime.now(ist).strftime("%y-%m-%d"))
# print(datetime.datetime.now(ist).strftime("%Y-%m-%d"))

#https://strftime.org/ 

print(datetime.datetime.now(ist).strftime("%c"))