#29/07/2026
"""
dạng :__int__
Operator Overloading
"""
class C2:
    pass
class C3:
    pass
class C1(C2,C3):
    def __init__(self ,who):
        self.name=who
I1=C1('sue')
I2=C1('bob')
print(I1.name)
print(I2.name)
#B2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("linus",28)
print(p1.name)
print(p1.age)
#b3Các giá trị mặc định trong __init__()
class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("Email")
p2=Person("Tobias",25)
print(p1.name,p1.age)
print(p2.name,p2.age)
#b4Nhiều tham số
#The __init__() method can have as many parameters as you need:
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
