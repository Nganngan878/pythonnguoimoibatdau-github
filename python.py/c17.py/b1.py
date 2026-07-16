#16/07/2026
"""
thực hành chương 17
Dạng1
Khái niệm Phạm vi (Local vs Global)
Đề bài: Khai báo một biến toàn cục x = 100. Viết hàm xem_pham_vi() tạo ra một biến cục bộ x = 50. In x bên trong hàm và bên ngoài hàm để thấy sự khác biệt.
"""
#thực hành 
x=100
def pham_vi():
    x=50
    print(f"trong ham:{x})")
pham_vi()
print(f"Ngoài hàm :{x})")