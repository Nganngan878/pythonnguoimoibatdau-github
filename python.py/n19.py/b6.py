#19/07/2026
"""
Dạng 6:Recursive Functions (

Đề bài: Viết hàm đệ quy giai_thua(n) để tính giai thừa của một số (n!).
Mục tiêu: Hiểu cách hàm tự gọi chính nó và tầm quan trọng của điều kiện dừng để tránh lỗi lặp vô hạn.

"""
def giai_thua(n):
    if n==1:return 1
    return n* giai_thua(n-1)
print(f"giai thua của 5 là:{giai_thua(5)}")