# __doc__
"""
Hàm này tính diện tích hình chữ nhật.
    
    Đầu vào:
    - dai: số đo chiều dài
    - rong: số đo chiều rộng
    
    Kết quả trả về: Diện tích (dai * rong)
"""
def tinh_dien_tich_hinh_chu_nhat(dai,rong):
    return dai*rong
#b1 gọi hàm bình thương
ket_qua=tinh_dien_tich_hinh_chu_nhat(3,4)
print(f"Dien tich la:{ket_qua}")
#b2 truy cập doc
print("--Hướng dẫn sử dụng hàm--")
print(tinh_dien_tich_hinh_chu_nhat)
#b2
"""
Tính bình phương
"""
edition=4
def square(x):
    return x **m2
class PartVI:
    """class dodumnetation for"""
    pass
#b1 gọi hàm 
print(f"Bình phương là:{square(4)}")
#2 b2 truy cập
print("\n--Nộid ung dócatring của hàm square---")
print(square.__doc__)
#3 truy cập docstring của class thông qua__doc__
print("\n--Nội dung docsstring của class PartIV---")
print(PartVI.__doc__)


