#21/07/2026
"""
3. Using the timeit Module
Đề Bài Tập
Yêu cầu: Khi dùng module timeit để đo tốc độ mã lệnh, tại sao chúng ta nên chạy thử nghiệm nhiều lần và chọn ra thời gian nhỏ nhất (minimum time) thay vì lấy thời gian trung bình?
Kết quả mong đợi: Trả lời được rằng kết quả nhỏ nhất giúp loại bỏ các khoảng trễ do máy tính đang bận chạy các ứng dụng ngầm khác ở thời điểm đó.
"""
import timeit
bt_1="""
total=0
for i in range(10):
    total +=i
"""
bt_2=timeit.timeit(stmt=bt_1,number=1000)
print("time run:",bt_2)
