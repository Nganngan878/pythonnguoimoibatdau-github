D = {'name': 'Pat', 'age': 40.0}
print(f"Lấy giá trị theo khóa 'name': {D['name']}")
D['city']='DN'
D['age']=41
print(f"Sau khi thêm/sửa: {D}")
if 'age' in D:
   print("Khóa 'age' có tồn tại trong D.")
print(f"Tất cả các khóa: {list(D.keys())}")
print(f"Tất cả các khóa: {list(D.values())}")
print(f"Tất cả các khóa: {list(D.items())}")
print(f"Lấy 'salary' (nếu không có thì trả về 0): {D.get('salary', 0)}")
D.pop('city')
print(f"Sau khi pop 'city': {D}")
del D['age']
print(f"Sau khi del 'age': {D}")
D_moi = {x: x**2 for x in range(5)}
print(f"Dictionary tạo từ comprehension: {D_moi}")
D1 = {'a': 1}
D2 = {'b': 2}
D_gop = D1 | D2
print(f"Sau khi gộp D1 và D2: {D_gop}")
