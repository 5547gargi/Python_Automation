import os

def main():
    
    req_path=input("Enter path to change directory : ")
    print("The current working directory is :",os.getcwd())
    try:
        os.chdir(req_path)
        print("The currnet working dir is :",os.getcwd())
    except FileNotFoundError:
        print(f"The gien path : {req_path} is not found")
    except NotADirectoryError:
        print(f"The gien path : {req_path} is not a Directory")
    except PermissionError:
        print(f"Can't have access for the gien path : {req_path}")
    except Exception as e:
        print(e)
    return None


if __name__=="__main__":
    main()