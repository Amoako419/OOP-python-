# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# item1 = Item("Phone",100,5)
# item2 = Item("laptop",1000,3)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(end="\n")

# print(item2.name)
# print(item2.price)
# print(item2.quantity)
# print(end="\n")


# class Person:
#     def __init__(self, name,age,gender,phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone

# Artist = Person("Adele",32,"Female",0000000000)

# print(Artist.name)
# print(Artist.age)
# print(Artist.gender)
# print(Artist.phone)


class Foo:
    def __init__(self,x=30):
     self.x = x
    def foo(self,y=30):
     return self.x*y
 
f = Foo(9)
print(f.foo(10))