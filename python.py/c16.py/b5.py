#11/07/2026
"""
Bài 5: Common Traps (Bẫy Mutable Arguments)
Đề bài: Viết một hàm them_vao_list(danh_sach, item) thực hiện danh_sach.append(item).
Tạo một list my_list = [], gọi hàm này 2 lần. Sau đó kiểm tra xem my_list ban đầu có bị thay đổi không.
Mục tiêu: Hiểu bẫy "Mutable Arguments" (Đối số có thể thay đổi).
"""
def them_vao_list(danh_sach,item):
    danh_sach.append(item)
my_list=[1,2,3]
them_vao_list(my_list,3)
print(f"List sau khi them:{my_list}")
#16/07/2026
#thực hành lại
def add_list(list,item):
    list.append(item)
my_list_1=[4,5,6]
add_list(my_list_1,7)
print(f"list sau khi them:{my_list_1})")