#16/07/2026
"""
Dạng 7 Mối quan hệ và Thiết kế (Interface)
Viết hàm tinh_chu_vi(hinh) mà không cần quan tâm hinh là class nào, miễn là đối tượng đó có thuộc tính chu_vi(). Đây là ví dụ về Interface và Đa hình (Polymorphism).
"""
class Circle:
    def chu_vi(self): return 10
class HinhVuong:
    def chu_vi(self): return 20
def in_chu_vi(hinh):
    print(f"chu_vi la:{hinh.chu_vi()}")
in_chu_vi(Circle())
in_chu_vi(HinhVuong())
#17/06/2026
#thực hành lại
class hinhtron:
    def chu_vi(self):return 100
class hinhvuong:
    def chu_vi(self):return 200
def in_chu_vi(hinh):
    print(f"chu vi là:{hinh.chu_vi()}")
in_chu_vi(hinhtron())
in_chu_vi(hinhvuong())