class Emp(object):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.display()
        return None
    def display(self):
        print(f'The name is : {self.name}\nThe salary is : {self.salary}')
        return None
    
emp1=Emp('Kamakshi','$50k')
emp2=Emp('Parvati','$40k')
# emp1.display()
# emp2.display()

#*By using __init__ method one biggest  advantages is we can create attributes while creating objects.