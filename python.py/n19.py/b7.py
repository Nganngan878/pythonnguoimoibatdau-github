#19/07/2026
"""
Dạng 7:Annotations and Decorators
Đề bài:
Viết một hàm với Annotations chỉ định tham số là int và trả về int.
Viết một Decorator đơn giản dùng @ để in ra dòng chữ "Hàm đang được gọi" mỗi khi hàm đó thực thi.
"""
def log_goi_ham(func):
    def wrapper(*args,** kwargs):
        print(f"đang gọi hàm :{func.__name__}__")
        return func(*args,**kwargs)
    return wrapper
@log_goi_ham
def cong(a:int ,b:int)-> int:
    return a+b
print(cong(10,20))
#THỰC HÀNH LẠI
#20/07/2026
def log_goi_ham(func):
    def wrapper(*args,**kwargs):
        print(f" đang gọi hàm :{func.__name__}")
        return func(*args,**kwargs)
    return wrapper
@log_goi_ham
def cong(a:int ,b:int)->int:
    return a+b
print(cong(30,40))