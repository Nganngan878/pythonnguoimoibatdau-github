#11/07/2026
"""
Bài 4: Polymorphism (Tính đa hình)
Đề bài: Viết một hàm nhan_doi(vat) mà không cần quan tâm vat là số hay chuỗi.
nhan_doi(5) phải trả về 10.
nhan_doi("Python") phải trả về "PythonPython".
Mục tiêu: Hiểu cách Python tự động điều chỉnh phép toán dựa trên kiểu dữ liệu (Interface).
"""
def nhan_doi(vat):
    return vat*2
print(f"Đa hình số :{nhan_doi(5)}")
print(f"da hinh chuỗi:{nhan_doi('Python')}")
#16/07/2026
#thực hành
def nhan_doi_1(son):
    return son*2
print(f"Đa hình số:{nhan_doi_1(4)}")
print(f"da hinh chuỗi :{nhan_doi_1('ngan')}")
