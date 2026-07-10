#11/07/2026
"""
Đề bài: Viết một hàm chao_hoi(ten) để in ra câu "Xin chào, [ten]!". Sau đó, sử dụng hàm này để chào 3 người bạn khác nhau trong danh sách ['An', 'Bình', 'Chi'].
Mục tiêu: Hiểu cách tránh "copy-paste" bằng cách dùng hàm.
"""
#thực hành
def chao_hoi(ten):
    """hàm chào hỏi"""
    return f"Xin chào, {ten}!"
names = ['An', 'Bình', 'Chi']
for name in names:
    print(chao_hoi(name))
def printer(messsage):
    print('Hello',messsage)
def adder(a,b=1,*c):
    return a+b+c[0]

