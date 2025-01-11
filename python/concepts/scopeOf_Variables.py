
def myfunction1():
    x=50
    print("Welcome to Functions")
    print("x from function1 : ",x)
    # myfunction2()
    return None

def myfunction2(y): # y is here a Parameter
    print("thank You")
    print("x value from function2 : ",y)
    return None

def main():
    # global x
    x=10
    myfunction1()
    myfunction2(x) # x here is an Argument
    return None

main()