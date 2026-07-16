#16/07/2026
"""
Dạng Closures (Hàm đóng)
Đề bài: Viết một hàm tao_bo_nhan(n) (hàm nhà máy) trả về một hàm nhân giá trị x với n.
"""
def tao_bo_nhan(a):
    def nhan(b):
        return a*b
    return nhan

nhan_doi=tao_bo_nhan(2)
print(f"Nhan doi 5:{nhan_doi(5)}")