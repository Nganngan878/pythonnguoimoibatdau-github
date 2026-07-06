#Built-in Iterables
"""
Đề bài:
Viết chương trình sử dụng range(1, 1000000) và enumerate để duyệt qua các số chẵn, nhưng chỉ in ra 5 số đầu tiên.
Giải thích tại sao cách này không gây tốn RAM mặc dù dải số rất lớn.
Thử nghiệm với một dictionary: Tạo một dictionary chứa thông tin học sinh, dùng vòng lặp để in ra tất cả các "key" của dictionary đó mà không dùng phương thức .keys().
"""
gen=enumerate(range(1,1000000))
for i,val in enumerate(range(5)):
    print(f"số thư{i+1} :{val}")
student={'name':'Ngân' ,'age':19,'major':'IT'}
for key in student:
    print(f"Key:{key}")
          