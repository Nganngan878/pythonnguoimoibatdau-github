#11/07/2026
"""
Bài 6: Relationship (Functions là Object)
Đề bài: Tạo hai hàm cong(a, b) và tru(a, b). Đưa cả hai hàm này vào một danh sách danh_sach_ham = [cong, tru]. Sau đó dùng vòng lặp để lấy từng hàm trong danh sách ra và tính toán với số 10 và 5.
Mục tiêu: Hiểu "First-Class Objects" – hàm cũng là một đối tượng có thể lưu trữ trong danh sách.
"""
def cong(a,b):return a+b
def tru(a,b):return a-b
danh_sachham=[cong,tru]
print(f"list:{danh_sachham[0](10,5)}")
#16/07/2026
#thực hành lại
def nhan(a,b):return a*b
def chia(a,b):return a/b
list_ham=[nhan,chia]
print(f"list:{list_ham[0](12,6)}")
for ham in list_ham:
    ket_qua=ham(12,6)
    print(f"kết quả của hàm {ham.__name__} là:{ket_qua}")