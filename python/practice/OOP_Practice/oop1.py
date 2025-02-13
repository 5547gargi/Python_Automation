# Costructor, __init__
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
    #  def apply_dicount(self):
    #      self.price=self.price*self.pay_rate
     def calculate_total_price(self):
          return self.price*self.quantity

 
item1=Item("screen",150,2)
item2=Item('mobile',200,3)
# print(item1.display())  #300
# print(item2.display())  #600
# print(Item.pay_rate)  #0.8
# print below All the attributes for Class label 
# print(Item.__dict__) #{'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x7ed9ceabd120>, 'display': <function Item.display at 0x7ed9ceabcb80>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
# print below All the attributes for Instance label 
# print(item1.__dict__) # {'name': 'screen', 'price': 150, 'quantity': 2}
# item1.apply_dicount()
# print(item1.display()) #240.0
item2.pay_rate=0.7
# item2.apply_dicount()
# print(item2.display()) #420.0
print(item1.display())