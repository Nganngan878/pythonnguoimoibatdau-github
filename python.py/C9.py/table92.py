#ghi dữ liệu
file=open('demo.txt','w',encoding='utf-8')
file.write('Hello, this is a demo file.\n')
lines=["hoc python minh rat thics.\n","python la ngon ngu lap trinh rat manh me.\n"]
file.writelines(lines)
file.close()
#đọc dữ liệu
# Mở file để đọc
file = open('demo.txt', 'r', encoding='utf-8')
for line in file:
    print("Đang đọc: ", line.strip()) # .strip() để xóa khoảng trắng/xuống dòng thừa

file.close() 
#meo chuyên chuyên nghiệp
with open('demo.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
