#21/07/2026
"""
1. Speed Results for Iteration 
Yêu cầu: Hãy viết hai đoạn mã nhỏ tính bình phương các số từ 1 đến 50: một cách dùng List Comprehension và một cách dùng vòng lặp For Loop thông thường. Quan sát xem phương pháp nào trông ngắn gọn hơn.
Kết quả mong đợi: Cả hai cách đều cho ra danh sách chứa các bình phương từ 1 
2
  đến 50 
2
 , nhưng List Comprehension viết gọn trong một dòng duy nhất.

"""
import timeit
def test_bt():
    return[x**2 for x in range(1,51)]
def test_loop():
    result=[]
    for x in range(1,51):
        result.append(x**2)
    return result
print("thời gian list:",test_bt()[:5], "...", test_bt()[-1])
print("Thời gian for lopp:",test_loop()[:5], "...", test_loop()[-1])
