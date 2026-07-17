#17/07/2026
"""
Dạng 4:(* và /)
Đề bài: Viết hàm dang_ky(ten, *, lop) (dùng * để bắt buộc dùng keyword) và in_so(a, /, b) (dùng / để bắt buộc dùng vị trí cho a). Hãy thử gọi sai cách để xem lỗi
"""
def dang_ky(ten,*,lop):
    print(f"{ten} học lop {lop}")
def in_so(a,/,b):
    print(f" a={a},b={b}")
dang_ky("Ngân",lop="25IT2")
in_so(10,b=20)