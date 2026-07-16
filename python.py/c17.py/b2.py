#16/07/2026
"""
dạng 2 Quy tắc LEGB
Đề bài: Viết một hàm lồng nhau. Hàm cha định nghĩa a = 1, hàm con truy cập a. Sau đó thử truy cập một hàm Built-in (ví dụ len) từ bên trong hàm con để kiểm chứng quy tắc LEGB.
"""
a=2
def ham_cha():
    a=4
    def ham_con():
        print(f"Giá trị a:{a}")
        print(f"Độ dài list: {len([1, 2, 3,4])}")
    ham_con()
ham_cha()
