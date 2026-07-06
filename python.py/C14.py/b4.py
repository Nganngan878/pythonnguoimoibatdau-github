#Advanced Comprehensions
"""
Đề bài:
Lọc (Filter): Từ danh sách data = [10, -5, 3, 0, -1, 8], sử dụng List Comprehension để tạo danh sách mới chỉ gồm các số dương.
Lồng (Nested): Cho một ma trận (danh sách các danh sách): matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Sử dụng List Comprehension để làm "phẳng" (flatten) ma trận này thành một danh sách duy nhất: [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""
data=[10,-5,3,0,-1,8]
positives=[x for x in data if x>0]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for now in matrix for num in now]
print(f"So dương :{positives}")
print(f"Ma trận phẳng:{flat}")
