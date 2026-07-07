#List Comprehensions 
"""
Đề bài: Cho danh sách numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Viết một List Comprehension để tạo ra danh sách mới chứa bình phương của các số trên.
Viết một List Comprehension để tạo ra danh sách các chuỗi dạng "Number: x" cho mỗi số trong danh sách gốc.
"""
numbers=[1,2,3,4,5,6,7,8,9,10]
square=[x**2 for x in numbers]
print(f"Binh phuong:{square}")
labels=[f"Number:{x}" for x in numbers]
print(f"labels:{labels}")
#7/7/2026
numbers=[2,4,6,8,10]
square=[x**2 for x in numbers]
print(f"Binh phuong :{square}")
labels=[f"Numbers:{x}" for x in numbers]
print(f"labels:{labels}")