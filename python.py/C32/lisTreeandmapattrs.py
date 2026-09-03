class C(list):
    pass

I = C()
print(I)
class C(list):
    __slots__=['x','y']
I=C()
I.x=3
I.y=4
print(I)
#
class ListTree:
    pass

class A: __slots__ = ['a'] # Both OK by bullet 1 above
class B(A, ListTree): pass
print(B())
class A: __slots__ = ['a']
class B(A, ListTree): __slots__ = ['b'] 
print(B())
