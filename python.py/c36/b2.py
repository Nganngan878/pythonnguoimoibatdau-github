def func2():
    print("func2: Đang thực hiện...")
    raise ZeroDivisionError("Lỗi chia cho 0!")  # Ngoại lệ được ném ra

def func1():
    try:
        print("func1: Gọi func2")
        func2()
    finally:
        print("func1.finally: Dọn dẹp tài nguyên của func1 trước khi lỗi đi qua")

try:
    func1()
except ZeroDivisionError as e:
    print(f"Chương trình chính nhận được lỗi: {e}")