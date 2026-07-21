#21/07/2026
"""
Dạng 4:Automating Your Benchmarks
Đề Bài Tập
Yêu cầu: Dựa trên bài học về tự động hóa benchmark và tìm "bẫy tốc độ", hãy cho biết việc truyền một generator expression trực tiếp vào hàm list() (ví dụ: list(x for x in range(10))) có nhanh bằng việc dùng trực tiếp [x for x in range(10)] hay không?
Kết quả mong đợi: Nhận diện được rằng cách dùng generator bên trong list() thường chậm hơn do tốn thêm thao tác gọi hàm tạo cấu trúc dữ liệu trung gian
"""
import timeit

# So sánh chi phí ẩn: Dùng Generator truyền vào list() so với List Comprehension trực tiếp
time_gen_constructor = timeit.timeit(lambda: list(x for x in range(10)), number=10)
time_comprehension = timeit.timeit(lambda: [x for x in range(10)], number=10)

print("Dùng generator bên trong list():", time_gen_constructor)
print("Dùng list comprehension trực tiếp:", time_comprehension)