#29/07/2026
"""
dạng self

"""
class C2:
    pass
class C3:
    pass
class C1(C2,C3):
    def setname(self,who):
        self.name=who
I1=C1()
I2=C1()
I1.setname('sue')
I2.setname('bob')
print(I1.name)
print(I2.name)