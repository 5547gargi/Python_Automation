# Simple python scripts to maintain employee data
class Employee:
    # If you define a variable immediately after declaration of class(class related variable); class attribute.
    count=0
    def get_name_age_salary(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.increase_employee_count()
        self.display_details()
        return None
    def increase_employee_count(self):
        Employee.count=Employee.count+1
        return None
    def display_details(self):
        print(f'The name is : {self.name}')
        print(f'Age of {self.name} is : {self.age}')
        print(f'Salary of {self.name} is : {self.salary}')
        return None

employee1=Employee()
employee2=Employee()

employee1.get_name_age_salary('Radha',16,'$30k')
# employee1.display_details()
# employee1.increase_employee_count()
employee2.get_name_age_salary('Krishna',12,'$16k')
# employee2.display_details()
# employee2.increase_employee_count()
# print(Employee.count)