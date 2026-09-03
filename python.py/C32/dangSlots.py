#__slots__ ở subclass, superclass không có __slots__
class A:
    pass
class B(A):
    __slots__=['x']
ob=B()
ob.x=10
ob.y=20
print(ob.x)
print(ob.y)
print(ob.__dict__)
#Superclass có __slots__, subclass không có
class C:
    __slots__=['a']
class D(C):
    pass
b1=D()
b1.a=30
b1.b=40
print(b1.a)
print(b1.b)
print(b1.__dict__)
#only lowest slot accessible
class E:
    __slots__=['b']
class F(E):
    __slots__=['c']
b2=F()
b2.b=50
b2.c=60
print(b2.b)
print(b2.c)
#print(b2.__dict__)
# Bullet 4: no class-level defaults
class G:
    __slots__=['d']
    def __init__(self):
        self.d=70
p=G()
print(p.d)
# Bullet 5: only one nonempty in mixins
class C:
    __slots__=['e']
class D:
    __slots__=()
class E(C,D):
    pass
b1=E()
b1.e=80
print(b1.e)
