#mutable
s='Hello'
s='h'+s[1:]
print(s)
t=(1,2,3)
#exmple list
my_list=[1,2,3]
my_list[0]=100
print(my_list)
#exmple of Dictionary
my_dic={'a':1,'b':2 ,'c':3}
my_dic['a']=99
print(my_dic)
#Nhóm Numeric (Numbers) - Immutable
x=10
print(10)
#. Nhóm Sequence (Trình tự)
#Strings (Chuỗi) - Immutable
s='Hello'
print(s.upper())
#Tuples (Bộ) - Immutable
T=(1,2,3)
print(T)
#bytearray - Mutable
ba=bytearray(b'Hello')
ba[0]=104
print(ba)
#Mapping
d={'a':1,'b':2,'c':4}
d['a']=99
print(d)
#sets
s={1,2,3}
s.add(4)
print(s)
#Frozenset - Immutable
fs=frozenset([1,2,3])
print(fs)
#Nhóm Extension
f=open('test.txt''','w')
f.write("Hello, this is a test file.")
f.close()


