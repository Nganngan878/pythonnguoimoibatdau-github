class Student:
    def __init__(self,age):
        self.age=age
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self,age):
        if age <0:
            raise ValueError("Age canot be negative")
        return age 
    @age.getter
    def age(self,age):
        return self.age
    
    