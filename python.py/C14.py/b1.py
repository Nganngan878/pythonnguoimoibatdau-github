#Iteration Protoco
"""
Đề bài: Cho một danh sách fruits = ['apple', 'banana', 'cherry'].
Bước 1: Sử dụng hàm iter() để lấy ra một iterator từ danh sách này.
Bước 2: Sử dụng next() để in ra từng phần tử một.
Bước 3: Dùng khối try-except với ngoại lệ StopIteration để duyệt toàn bộ danh sách mà không cần dùng vòng lặp for.
"""
fruits=['apple','banana','cherry']
iterator=iter(fruits)
while True:
    try:
        item=next(iterator)
        print(f"Item:{item}")
    except StopIteration:
        print("đã duyệt xong")
#7/07/2026 làm lại cho hiểu bản chất
trai_cay=['xoài','mít','mận']
iterator=iter(trai_cay)
while True:
    try:
        item=next(iterator)
        print(f"Item:{item}")
    except StopIteratiom:
        print("duyệt")

