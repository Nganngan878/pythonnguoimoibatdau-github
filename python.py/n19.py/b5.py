#19/07/2026
"""
 Dạng 5:Functional Tools (map, filter, reduce)
Đề bài: Cho danh sách L = [1, 2, 3, 4].
Dùng map để tạo list mới với các số nhân đôi.
Dùng filter để lấy ra các số lớn hơn 2.
Dùng reduce (từ functools) để tính tổng danh sách.

"""
from functools import reduce
L=[1,2,3,4]
print(list(map(lambda x: x *2,L)))
print(list(filter(lambda x:x>2,L)))
print(reduce(lambda x,y:x+y,L))
#THỰC HÀNH LẠI
#20/07/2026
from functools import reduce
L=[1,2,3,4,5]
print(list(map(lambda a:a*2,L)))
print(list(filter(lambda a:a>2,L)))
print(reduce(lambda x,y:x+y,L))