import script1

def mult(a,b):
    print(f"The multiplication of {a} and {b} is {a*b}")
    return None

def main():
    x=10
    y=20
    # print(dir(script1))
    script1.addition(x,y)
    # script1.sub(x,y)
    # mult(x,y)
    return None

if __name__=="__main__":
    main()