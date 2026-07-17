#16/07/2026
"""
Dạng 5Lưu trữ trạng thái với Thuộc tính hàm
Đề bài: Tạo một hàm đếm số lần được gọi bằng cách gán một thuộc tính (attribute) trực tiếp lên chính đối tượng hàm đó.

"""
def dem_so_lan_goi():
    dem_so_lan_goi.count +=1
    return dem_so_lan_goi.count
dem_so_lan_goi.count=0
print(f"lan 1:{dem_so_lan_goi}")
print(f"lan 2:{dem_so_lan_goi}")
print(f"lan 3:{dem_so_lan_goi}")
print(f"lan 4:{dem_so_lan_goi}")

#17/07/2026
def dem_so_lan_goi_1():
    dem_so_lan_goi_1.count+=3
    return dem_so_lan_goi_1.count
dem_so_lan_goi_1.count=0
print(f"lan1:{dem_so_lan_goi_1}")
