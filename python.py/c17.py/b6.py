#16/07/2026
"""
Dạng 6 Bẫy vòng lặp Lambda (Gotchas)
Đề bài: Tạo một danh sách các hàm lambda lặp qua i từ 0 đến 2. Bạn sẽ thấy lỗi "nhớ giá trị cuối" nếu không dùng i=i
"""
#bãy
funs=[lambda :i for i in range(5)]
print(f"Ket qua sai:{[f() for f in funs]}")
# fix
funs_fix=[lambda i=i : i for i in range(5)]
print(f"ket qua dung:{[f() for f in funs_fix]}")
#17/06/2026
#thực hành 
#bẫy 1
funs=[lambda: i for i in range(8)]
print(f"ket quả sai:{[f() for f in funs]}")
# fix 1
funs_fix_1=[lambda i=i :i for i in range(8)]
print(f"ket qua dung:{[f() for f in funs_fix_1]}")