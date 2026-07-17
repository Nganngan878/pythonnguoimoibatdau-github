#17/07/2026
"""
dạng 1:Immutable vs Mutable
Đề bài: Viết một hàm thay_doi(n, lst):
Hàm cộng n thêm 10.
Hàm append thêm 100 vào lst.
Sau khi gọi hàm với so = 5 và danh_sach = [1], hãy in ra giá trị của so và danh_sach để xem cái nào thay đổi, cái nào giữ nguyên.
"""
#thực hành
def thay_doi(n,list):
    n+=10
    list.append(100)
so=5
danh_sach=[1]
thay_doi(so,danh_sach)
print(f"so sau ham:{so}")
print(f"list sau ham:{danh_sach}")