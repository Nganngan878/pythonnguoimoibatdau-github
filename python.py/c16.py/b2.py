#11/07/2026
"""
Bài 2: Tools & Execution (def và return)
Đề bài: Viết một hàm tinh_binh_phuong(n) nhận vào một số và trả về (return) bình phương của nó. Nếu truyền vào không đúng số, hãy thử dùng lambda để tính bình phương cho một số bất kỳ ngay lập tức.
Mục tiêu: Phân biệt hàm có return và hàm ẩn danh lambda.

"""
#thực hành
def binh_phuong(n):
    if isinstance(n,(int,float)):
        return n**2
    else:
        return "Lỗi"
binh_phuong_lambda=lambda n: n**2
print(f"kêt quả:{binh_phuong(5)}")
print(f" kết quả(sai):{binh_phuong('Python')}")
print(f"dùng lambda:{binh_phuong_lambda(6)}")
ket_qua=(lambda x:x*x)(10)
print(f"dùng lamda ngay lap tức:{ket_qua}")
#16/07/2026
#Thực hành lại
def binh_phương_2(x):
    if isinstance(x,(int,float)):
        return x**2
    else:
        return "Lỗi"
binh_phương_2_lambda=lambda n:n**2
print(f"kết quả:{binh_phương_2(6)}")
print(f"kết quả(sai):{binh_phương_2('Python')}")
print(f"dung lambda:{binh_phương_2_lambda(7)}")
ket_qua_2=(lambda x:x*x)(10)
print(f"dùng lambda ngay lap tuc:{ket_qua_2}")
