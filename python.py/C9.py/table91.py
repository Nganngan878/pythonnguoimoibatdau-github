T=()
print(T)
T=(0,)
print(T)
T=(0,'Py',1.2,3)
print(T)
T=0,'Py',1.2,3
print(T)
T=tuple('hack')
#độ dài
T = ('Python', 'Java', 'C++', 'JavaScript')
print(T)
print(T[0])
print(T[0][1])
print(T[1:3])
print(len(T))
#+ và* tuple
T=(1,2)
T1=(3,4)
print(T+T1)
print(T*3)
#so sánh
T=('a', 'b', 'c')
print('a' in T)
for x in T:
    print(x)
print([x*2 for x in(1,2,3)])
#giải nén
x=(1,2)
y=(3,4)   
T=(*x,0,*y,*x) 
print(T)
#method
T=('py' ,'C','java','py')
print(T.index('py'))
print(T.count('py'))
#named tuple
from collections import namedtuple
Emp=namedtuple('Emp','name age job')
e1=Emp('Phan Thi Ngan',19,'Developer')
print(e1.name)
print(e1.age)
print(e1.job)