#19/07/2026
"""
Dạng 3:(Introspection) and Attributes (Medium Level)
Introspection and Attributes (Soi chiếu)
Đề bài: Tạo một hàm cong(a, b). Gán một thuộc tính tùy chỉnh func.mo_ta = "Hàm cộng hai số" vào hàm đó. Sau đó, dùng __name__ để in tên hàm và in thuộc tính mo_ta ra màn hình.
Mục tiêu: Học cách kiểm tra và đính kèm dữ liệu vào đối tượng hàm.
"""
def cong(a,b):
    return a+b
cong.mo_ta="Hàm cộng hai số "
print(f"ten:{cong.__name__}")
print(f"Mô tả :{cong.mo_ta}")