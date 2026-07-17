#17/07/2026
"""
Dạng 2:Positional, Keyword, Defaults
Đề bài: Viết hàm thiet_lap_may(ten, ram=8).
Gọi hàm theo 3 cách: (1) Chỉ truyền ten (dùng mặc định), (2) Truyền ten và ram theo thứ tự, (3) Truyền ten và ram bằng cách sử dụng Keyword.
"""
def thiet_lap_may(ten,ram=8):
    print(f" Máy {ten} có {ram} GB Ram")
thiet_lap_may("LpatopA") # defaults
thiet_lap_may("LaptopB",16)# positional
thiet_lap_may(ram=32,ten="PC_PRO")# keywword