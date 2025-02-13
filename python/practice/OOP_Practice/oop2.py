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
     def __repr__(self):
          return f"Item({"self.name"}, {self.price}, {self.quantity})" 
    
item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
item3=Item("Cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("Keyboard",75,5)

# print(Item.all) # [<__main__.Item object at 0x7eb6f7b30710>, <__main__.Item object at 0x7eb6f7b30740>, <__main__.Item object at 0x7eb6f7b30860>, <__main__.Item object at 0x7eb6f7b30890>, <__main__.Item object at 0x7eb6f7b308c0>]
for each_instances in Item.all:
    print(each_instances.name)  
print(Item.all) #[Item(self.name, 100, 1), Item(self.name, 1000, 3), Item(self.name, 10, 5), Item(self.name, 50, 5), Item(self.name, 75, 5)]
