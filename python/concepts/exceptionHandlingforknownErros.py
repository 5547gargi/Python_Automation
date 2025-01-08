#print(a) # NameError: name 'a' is not defined
#print(1+"asdf") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#open("abc.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
#print(2/0) # ZeroDivisionError: division by zero

try:
    # print(a)
    # print(4+"abc")
    # open("abc.txt")
    # print(5/0)
    import fabric
except ZeroDivisionError:
    print("Division by zero not possible")
except ModuleNotFoundError:
    print("Please install the module before using it")
except NameError:
    print("variable not defined")
except TypeError:
    print("addition of string and number is not possible")
except FileNotFoundError:
    print("No such file or diectory found")
except Exception as e:
    print(e)
else:
    print("Tihis will execute if there is no exception")
finally:
    print("This will execute after trying with try and except block")