#8/07/2026
#DIR
"""
Đề bài:
Tạo một chuỗi bất kỳ: my_text = "Hello Python".
Sử dụng print(dir(my_text)) để xem các thuộc tính và phương thức của chuỗi đó.
Câu hỏi: Bạn có thấy các tên bắt đầu bằng __ không? Hãy thử đoán xem chúng được dùng để làm gì (gợi ý: đó là các phương thức đặc biệt của Python).
"""
#Luyện tập
my_list=[1,2,3]
#print(dir(my_list))
named_attributes=[ a for a in dir(my_list) if not a.startswith('__')]
print("các phương thức hữu ích của list :")
print(named_attributes)
#tên bất kỳ
fruits=['appple','banana','cherry']
#len
tong_so=len(dir(fruits))
print(f"Tổng số 'phụ tùng' của danh sách fruits là :{tong_so}")
#list && dict
#print(dir(fruits))
useful_methods=[a for a in dir(fruits) if not a.startswith('__')]
print("các phương thức của fruits:")
print(useful_methods)
useful_methods_class=[a for a in dir(list) if not a.startswith('__')]
print(useful_methods_class)
useful_methods_class_name=[a for a in dir(dict) if not a.startswith('__')]
print("các phương thức của dict")
print(useful_methods_class_name)
print(dir(useful_methods_class_name))



