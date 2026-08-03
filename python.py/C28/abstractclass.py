#3/08/2026
"""
Abstract Class
"""
class Dog:
    def __init__(self,name):
        self.name=name
    #abstract class
    def abstractClassName(self):
        pass
    # create class implement từ abstract calss
    #khái báo
    def methodName(self):
        pass
    def show(self):
        print("Tên:",self.name)
Dod=Dog("liuliu")
Dod.show()
Dod.abstractClassName()
Dod.methodName()
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def do(self):
        pass

class Impl(Base):
    def do(self):
        print("done")
Impl().do() 
