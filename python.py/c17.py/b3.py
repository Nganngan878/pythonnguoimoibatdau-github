#16/07/2026
"""
Dạng 3 Lệnh Global và Nonlocal
Đề bài: Sử dụng nonlocal để hàm con thay đổi biến của hàm cha. Sử dụng global để thay đổi biến toàn cục.

"""
x=5
def ham_ngoai():
    x=10
    def ham_trong():
        nonlocal x
        x=30
    ham_trong()
    print(f"x sau khi nonlocal:{x}")
ham_ngoai()
#17/07/2026
#thực hành lại
a=6
def ham_ngoai():
    a=8
    def ham_trong():
        nonlocal a
        x=20
    ham_trong()
    print(f" a sau khi nonlocal:{a}")
ham_ngoai()