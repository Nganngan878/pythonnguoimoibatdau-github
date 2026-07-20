#19/07/2026
"""
Dạng 2: Functions are "First-Class Objects" (
Tạo hai hàm xin_chao() và tam_biet(). Lưu cả hai hàm này vào một danh sách, sau đó dùng vòng lặp để gọi lần lượt các hàm trong danh sách đó.
Mục tiêu: Hiểu cách lưu trữ hàm trong cấu trúc dữ liệu.

"""
def xin_chao(): print("Xin chào!")
def tam_biet(): print("Tạm biệt!")

funcs = [xin_chao, tam_biet] 
for f in funcs:
    f() 
#thực hành lại 
#20/07/2026
def hello_ngan():
    print("Xin chao ngân!")
def goodbye_ngan():
    print("tạm biệt ngân!")
funcs1=[hello_ngan,goodbye_ngan]
for f1 in funcs1:
    f1()