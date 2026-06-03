# if/elif/else: Chọn hành động
text = 'python'
if 'python' in text:
    print("Found it!")

# for/else: Lặp qua dữ liệu
for x in [1, 2, 3]:
    print(x)
else:
    print("Loop finished!")
#loop control
for i in range(5):
    if i==2:
        continue 
    if i==4:
        break
    print(i)
#Functions
def add(a,b):
    return a+b
result=add(5,3)
print(result)
#gián biến 
a,b='python',3.14
a=(b:=3.14)
print(a,b)
print(f"Value of :{a} {b}")
#--5 match/case: Kiểm tra giá trị

edition = 6
if edition == 1:
    print("First edition")
elif edition == 2:
    print("Second edition")
elif edition == 3:
    print("Third edition")
elif edition == 4:
    print("Fourth edition")
elif edition == 5:
    print("Fifth edition")
else:
    print("Unknown edition")
#7--while/else
x=0
while x<1:
    x+=1
    print(x)
else:
    print("While loop finished!")
#--8pass
if 'java' not in text:
    pass
#--9 break
while True:
    print("9.break :stoooping loop now""")
    break
#--10 continue
for i in range(2):
    continue
    print("This will never be printed")
#--11 def
def f(a,b,c=2):
    return a+b+c
result=f(1,2)
print(result)
#--12 yield
def gen(n):
    for i in range(n):
        yield i*2
print(f"13. YIELD: {next(gen(5))}")
#--14 global
val=1
def function():
    global val
    val=2
function()
print(f"14. GLOBAL: {val}")
#class định nghĩa đối tượng
class person:
    def __init__(self,name):
        self.name=name
import math
from datetime import datetime as dt
with open('demo.txt','w') as f:
    f.write("Hello, World!")
#xử lý lỗi
try:
    x=1/0
except ZeroDivisionError:
    print("Cannot divide by zero!") 
finally:
    print("This will always execute.")
x=10
assert x>5, "x must be greater than 5"