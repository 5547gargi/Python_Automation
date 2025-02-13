# Class_Methods Vs Static_Methods
#*A Class_Meyhod cloud be accessed from the Class level only
import csv

class Item(object):
      pay_rate = 0.8 # The pay rate after 20% discount
      all=[]
      def __init__(self, name: str, price: float, quantity=0):
           # Run validations to the received arguments
           assert price >= 0, f"price {price} is not greater or equal to zero!"
           assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"
           # Assign to self object
           self.name=name
           self.price=price
           self.quantity=quantity
           # Actions to execute
           Item.all.append(self)  # self is the insatance it's-self every time it is created
           return None
      def display(self):
           return self.price*self.quantity
      def apply_dicount(self):
           self.price=self.price*self.pay_rate
    
      #*When we call our classmethod ; the class-object it's-self passed as the first argument always in the background 
      @classmethod
      def instantiate_from_csv(cls):
           with open('items.csv', 'r') as f:
                reader = csv.DictReader(f)
                items=list(reader)
           for item in items:
                # print(item)
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )
     
      # Here in staticmethod ; the class-object doesn't pass as an argument for the mehod ; this is an isolated function 
      @staticmethod
      def is_integer(num):
           #we will count out the floats that are point zero(ie; 10.0,50.0) 
           if isinstance(num,float):
                #cout out decimal values that are point zero
                return num.is_integer()
           elif isinstance(num,int):
                return True
           else:
                return False

      def __repr__(self):
           return f"Item({"self.name"}, {self.price}, {self.quantity})" 

Item.instantiate_from_csv()    
print(Item.all)
print(Item.is_integer(6.3))

# When to use class-method and when to use static-method?
'''
The static-method should do something that has a relationship
with the class, but not something that must be unique 
per instance! 
''' 
'''
The class-method should do somthing that has relationship 
with the class, but usually, those are used to manipulate 
different structures of data instantiate objects,
like we have done with csv-file.
'''