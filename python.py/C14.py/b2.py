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
#7/7/2026 làm lại cho hiểu bản chất
#iterable: Đối tượng cần duyệt qua (List, String, Dictionary, v.v.).
#start (Tùy chọn): Số bắt đầu đếm. Mặc định là 0
gen=enumerate(range(1,100000))
for i,val in enumerate(range(6)):
    print(f"số thứ{i+2}:val")
student={'lop':'25IT2' ,'age':19,'hobby':'English and oop'}
for key in student:
    print(f"key:{key}")
