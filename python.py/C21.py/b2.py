#21/07/2026
"""
Dạng 2:Function Calls and the map Trap 
Yêu cầu: Giải thích ngắn gọn vì sao việc dùng hàm map kết hợp với một hàm tự viết (custom function) hoặc hàm ẩn (lambda) đôi khi lại chạy chậm hơn so với việc dùng một vòng lặp hoặc List Comprehension đơn giản.
Kết quả mong đợi: Nêu được ý chính là do chi phí gọi hàm (function call overhead) và "bẫy" hiệu năng của map khi không gọi hàm tối ưu bằng C bên trong.
"""
import timeit
numbers=range(1000)
time_1=timeit.timeit(lambda:list(map(abs,numbers)),number=1000)
def square(x):
    return x*x
time_2=timeit.timeit(lambda:list(map(square,numbers)),number=1000)
print("kết quả:",time_1)
print("Kết quả:",time_2)