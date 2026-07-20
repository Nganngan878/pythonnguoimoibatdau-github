#19/07/2026
"""
Dạng 1;Function Design Rules
Đề bài: Viết một hàm tinh_thue(thu_nhap) chỉ thực hiện tính thuế và một hàm hien_thi(ket_qua) chỉ thực hiện in kết quả. Tránh dùng biến toàn cục để lưu kết quả.
Mục tiêu: Tách biệt chức năng (Cohesion) và sử dụng input/output rõ ràng

"""
#thực hành
def tinh_thue(thu_nhap):
    return thu_nhap*0.1
def hien_thi(ket_qua):
    print(f"thuế phải nôpk :{ket_qua}")
hien_thi(tinh_thue(10000))
#THỰC HÀNH THÊM 1 LẦN CHO NHỚ 
#20/07/2026
def tinh_thue_1(thu_nhap_1):
    return thu_nhap_1*0.1
def hien_thi_1(ket_qua_1):
    print(f"thuế phải nộp :{ket_qua_1}")
hien_thi_1(tinh_thue_1(1000))
