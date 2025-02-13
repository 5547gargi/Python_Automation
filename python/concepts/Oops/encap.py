class Person(object):
     def assign_name_age(self,name,age):
         self.name=name
         self.__age=age
         return None
     def display(self):
          print(self.name,self.__age)

person1=Person()
person1.assign_name_age("radha",16)
person1.display()
print(person1.name)
print(person1.age) # AttributeError: 'Person' object has no attribute 'age'