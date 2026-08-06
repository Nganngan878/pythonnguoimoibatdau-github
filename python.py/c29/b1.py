#6/08/2026
"""
Super
"""
class Super:
    def method(self):
        print('in Super.method()')
class sub(Super):
    def method(self):
        print('in sub.method()')
        super().method()
s=sub()
s.method()
#b2
class Super:
    def __init__(self,x):
        print("dèault code")
class Sub(Super):
    def __init__(self,x,y):
        Super.__init__(self,x)
        print('custom code')
s=Sub(1,2)