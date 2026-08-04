#4/08/2026
"""
NapChongToanTu
"""
from pyclbr import Class


class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def print(self):
        print("x=",self.x,"y=",self.y)
    def phep_cong(self):
        return Point(self.x+1,self.y+1)
    def phep_tru(self):
        return Point(self.x-1,self.y-1)
p=Point(3,4)
p.print()
p.phep_cong().print()
p.phep_tru().print()
# fuction overloading __str__:nó là kết quả chuẩn hơn
class Point2:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point2(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Point2(x,y)
    def __pow__(self,other):
        x=self.x**other.x
        y=self.y**other.y
        return Point2(x,)
    def __mod__(self,other):
        x=self.x%other.x
        y=self.y%other.y
        return Point2(x,y)
    def __lshift__(self, other):
        x=self.x<<other.x
        y=self.y<<other.y
        return Point2(x,y)
    # so sánh
    def __lt__(self,other):
        self_mag=(self.x**2)+self.y**2
        other_mag=(other.x**2)+other.y**2
        return self_mag < other_mag
p=Point2(3,4)
print(p)
p1=Point2(1,2)
p2=Point2(5,6)
p3=p1+p2
print(p3)
p1=Point2(2,3)
p2=Point(-1,2)
print(p1+p2)
p=Point2(1,1)<Point2(2,2)
print(p)
