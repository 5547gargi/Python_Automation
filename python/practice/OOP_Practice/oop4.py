#Inheritance

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
        

      def apply_dicount(self):
           self.price=self.price*self.pay_rate
      def calculate_total_price(self):
           return self.price*self.quantity
    
      #*When we call our classmethod ; the class-object it's-self passed as the first argument always in the background 
      @classmethod
      def instantiate_from_csv(cls):
           with open('items.csv', 'r') as f:
               reader = csv.DictReader(f)
               items=list(reader)
           for item in items:
               #print(item)
               Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
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
           # return f"Item({"self.name"}, {self.price}, {self.quantity})"
            return f"{self.__class__.__name__}({"self.name"}, {self.price}, {self.quantity})" 
     
class Phone(Item):
      def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
           # Calling the super function to have access to all atributes/methods
           super().__init__(
               name,price,quantity
           )
           # Run validations to the received arguments
           assert broken_phones >=0, f"Broken_phones {broken_phones} is not greater or equal to zero!"
           # Assign to self object
           self.broken_phones=broken_phones
           return None

phone1=Phone("jscPhonev10", 500, 5, 1)
# print(phone1.calculate_total_price())
phone2=Phone("jscPhonev20", 700, 5, 1)

print(Item.all)
print(Phone.all)