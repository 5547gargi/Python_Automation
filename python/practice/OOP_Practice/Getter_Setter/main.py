# Getters and Setters
from item import Item

item1=Item("MyItem", 750)
#item1.name="OtherItem" # AttributeError: property 'name' of 'Item' object has no setter
#print(item1.__name) # AttributeError: 'Item' object has no attribute '__name'.

# Setting an Attribute
# item1.name="OtherItem"
# # Getting an Attribute
# print(item1.name)
# item1.price=-900
# item1.quantity=-4
item1.apply_increment(0.2)
item1.apply_dicount()
print(item1.price)