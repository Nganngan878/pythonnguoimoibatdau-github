#Công cụ nâng cao & Bẫy (Traps)
"""
Đề bài:
Unpacking: Tạo một file văn bản ảo (hoặc một list các dòng). Sử dụng hàm max() để tìm dòng dài nhất trong file đó mà không cần đọc hết vào một list trước.
Bẫy: Tạo một đối tượng map hoặc zip từ hai danh sách. Hãy in ra các phần tử của đối tượng đó 2 lần. Bạn nhận thấy điều gì ở lần in thứ hai? Làm thế nào để khắc phục nếu bạn cần dùng dữ liệu đó nhiều lần?
"""
data=['a','b','c']
print("Max:",max(data))
z=zip([1,2],[3,4])
print(list(z))
print(list(z))
z_saved=list(zip([1,2],[3,4]))
print(list(z_saved))
print(list(z_saved))
#7/07/2026
data=['b','c','f']
print("Max:" ,max(data))
z=zip([2,4],[6,9])
print(list(z))
print(list(z))
z_saved=list(zip([2,4],[6,9]))
print(list(z_saved))
print(list(z_saved))