#1 gán giá trị
a,b=1,2
print(a,b)
#3 cấu trúc điều khiển
# Đảm bảo a là một chuỗi (string) nếu bạn muốn dùng 'in'
a = 'python_code' 
if 'py' in a:
    print("Tìm thấy 'py' trong a!")
else:
    print("'py' không có trong a.")

#4 vòng lặp
for i in range(2):
    print("Hello")
else:
    print("Loop is done")
#5 điều khiển vòng lặp
while True:
    break
#6 hàm & Gểnator
def myy_func(x):
    return x*2
def my_gen(n):
    yield n+1
#7 global
x=10
def change_x():
    global x
    x=20
change_x()
print(x)
#8 pass
if True:
    pass
