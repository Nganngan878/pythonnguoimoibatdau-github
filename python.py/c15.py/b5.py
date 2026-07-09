#dạng 5
"""
Đề bài:
Giả sử bạn có một đoạn văn bản: text = "python,java,c++,javascript". Bạn muốn biến nó thành một danh sách: ['python', 'java', 'c++', 'javascript'].
Bạn biết có một phương thức trong kiểu dữ liệu str (chuỗi) giúp làm việc này, nhưng không chắc chắn 100% cách dùng.
Hãy dùng kỹ thuật dir() để tìm tên phương thức đó.
Sau đó, hãy tra cứu nó trên Library Reference (docs.python.org) để xem cách dùng chính xác.
"""
text="python,java,c++,js"
cac_lenh_str=[ a for a in dir(text) if not a.startswith('__')]
print("--b1:tìm tên phương thức trong danh sách dưới đây--")
print(cac_lenh_str)
#2 áp dụng lệnh vừa tìm đc 
# thử dùn split
ket_qua=text.split(',')
print(f"\n--B2:Kết quả sau khi dùng lệnh:{ket_qua}--")
#3 kiểm chúng 
print("\n--- Bước 3: Hãy truy cập https://docs.python.org/3/library/stdtypes.html#str.split")
print("Đọc phần giải thích về split để hiểu tại sao nó hoạt động!")
#9/07/2026 
#thực hành cho nhớ
clas="ngan,xinh đẹp,thích học tiếng anh,thích chơi đàn guitar"
so_thich_cua_ngan=[a for a in dir(clas) if not a.startswith('__')]
print("--b1 :tìm tên sở thích của ngân ngân trong danh sách--")
print(so_thich_cua_ngan)
#2 áp dụng lệnh vưa tìm được
# thử dùng split
ket_qua_cua_ngan=clas.split(',')
print(f"\n--b2:kết quả sau khi dùng lệnh:{ket_qua_cua_ngan}--")
#3 kiểm tra
print("\n--- Bước 3: Hãy truy cập https://docs.python.org/3/library/stdtypes.html#str.split")
print("Đọc phần giải thích về split để hiểu tại sao nó hoạt động!")