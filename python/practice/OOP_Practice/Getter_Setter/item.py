import csv
class Item(object):
      pay_rate = 0.8 # The pay rate after 20% discount
      all=[]
      def __init__(self, name: str, price: float, quantity=0):
         # Run validations to the received arguments
         assert price >= 0, f"price {price} is not greater or equal to zero!"
         assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"
         # Assign to self object
         self.__name=name # Making name private to the class once it's instantiated 
         self.__price=price
         self.quantity=quantity
         # Actions to execute
         Item.all.append(self)  # self is the insatance it's-self every time it is created
      
      @property
      def price(self):
           return self.__price
      
      def apply_dicount(self):
           self.__price=self.__price*self.pay_rate
     
      def apply_increment(self,increment_value):
           self.__price = self.__price + self.__price*increment_value

      @property
      # Property Decorator = Read-Only Atribute
      def name(self):
          #print("you are tring to get")
          return self.__name      
       
      @name.setter
      # Yet we want to set new value for *name*
      def name(self,value):
           if len(value) > 10:
                raise Exception("The name is too long!")
           else:
                #print("Ypu are trying to set")
               self.__name=value

      def calculate_total_price(self):
           return self.__price*self.quantity
    
      #*When we call our classmethod ; the class-object it's-self passed as the first argument always in the background 
      @classmethod
      def instantiate_from_csv(cls):
           with open('/workspaces/PythonDevOps/practice1/OOP_Practice/items.csv', 'r') as f:
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


