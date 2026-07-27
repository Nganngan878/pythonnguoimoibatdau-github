#27/07/2026
"""
Dạng 2
Bài tập: Tạo file gamod.py có hàm __getattr__(name) để khi truy cập một thuộc tính không tồn tại, nó trả về câu thông báo lỗi tùy chỉnh.

"""
def __getatr__(name):
    return f"Lỗi:Thuộc tính '{name}' không tồn tại !"
import gamod
print(gamod.hello)