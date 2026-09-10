def func2():
    print("Bắt đầu func2")
    raise ValueError("Lỗi từ func2!") 
def func1():
    try:
        print("Bắt đầu func1")
        func2()  
    except ValueError as e:
        print(f"func1 đã bắt được: {e}")  
try:
    func1()
    print("Chương trình chạy tiếp bình thường sau khi ngoại lệ được xử lý.")
except ValueError:
    print("Khối ngoài cùng không nhận được lỗi vì func1 đã xử lý mất rồi.")