class Emp:
    count=0
    def __init__(self):
        Emp.count=Emp.count+1
        return None
    def display(self):
        print("This is display method")
        return None
    
emp1=Emp()
emp2=Emp()
# emp1.display()
# emp2.display()
print("The number of objects created from Emp class are : ",Emp.count)