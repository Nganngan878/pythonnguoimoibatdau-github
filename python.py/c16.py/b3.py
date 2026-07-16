#11/07/2026
"""
Bài 3: Variables & Arguments (Biến cục bộ và Tham số)
Đề bài: Viết một hàm tang_gia_tri(x). Bên trong hàm, tạo một biến y = 10 rồi cộng x + y. Sau khi gọi hàm, hãy thử print(y)bên ngoài hàm xem có lỗi không?

Mục tiêu: Hiểu phạm vi của biến cục bộ (Local variables). demcode đi 

"""
def tang_gia_tri(x):
    y=10
    return x+y
ket_qua=tang_gia_tri(5)
print(f"\nket quả: {ket_qua}")
#16/07/2026
#Thực hành lại
def tang_gia_tri_1(a):
    b=5
    return a+b
ket_qua_2=tang_gia_tri_1(4)
print(f"\n ket qua:{ket_qua_2}")