'''
def myfun(a,b):
    return a+b

def main():
    a=eval(input("enter 1st number : "))
    b=eval(input("enter 2nd number : "))
    result=myfun(a,b)
    print("result is :",result)
    return None
main()
'''
'''
def display(*data):
    for each in data:
        print(type(each))
    # print(data)
    return None

# display()
# display(4)
# display(4,5)
# display("hello")
display("Hello",5,4.5)
'''

# def display(**krg):
#     print(krg)
#     return None

# display()
# display(a=2,b=3)
# display(x="hi",y=4,z=1.5,user="dev01")

def display(a,**krg):
    print(a)
    print(krg)
    return None

display(22,x="hi",y=4,z=1.5,user="dev01")