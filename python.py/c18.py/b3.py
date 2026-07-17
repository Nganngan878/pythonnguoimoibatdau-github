#17/07/2026
"""
Dạng 3 :* và Collecting & Unpacking
Đề bài: Viết một hàm tinh_tong(*args) để tính tổng tất cả các số truyền vào. Sau đó, tạo một list data = [1, 2, 3] và gọi hàm bằng cách "unpack" list này.
"""
def tinh_tong(*args):
    return sum(args)
data=[1,2,3]
print(f"Tong:{tinh_tong(*data)}")