# 1. Assignment (Câu lệnh gán)
a, b = 'python', 3.12  

# 2. Expression Statements (Câu lệnh biểu thức)
# Gọi hàm mà không gán kết quả (dùng cho side effect)
print(f"Giá trị là: {a}, {b}") # Hàm print là một biểu thức

# 3. Selection & Iteration (Chọn hành động & Lặp)
if 'python' in a: 
    print("Đây là ngôn ngữ Python!")

for i in range(2): # for/else
    print(f"Lần lặp thứ: {i}")

# 4. Functions & Namespace (Hàm & không gian tên)
def my_func(x):
    return x * 2

def my_gen(n):
    yield n + 1 

# 5. Global (Thay đổi biến toàn cục)
x = 10
def change_x():
    global x # global
    x = 20

change_x()
print(f"Giá trị x sau khi dùng global: {x}")

# 6. Placeholder (Trình giữ chỗ)
if True:
    pass # 