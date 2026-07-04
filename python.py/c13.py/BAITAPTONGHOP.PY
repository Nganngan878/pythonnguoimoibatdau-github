#BÀI TẬP TỔNG HỢP CHƯƠNG 13
# Giả sử chúng ta có 2 danh sách: tên khách và trạng thái đơn hàng
kh=["Ngân"]
tt=["đã giao","đang giao","huỷ","đang xử lý"]
print("--- 1, 3. Basic & Tools (Zip, Enumerate, Range) ---")
#range để đém,zip để kết hợp danh sách
for i in range(len(kh)):
    print(f"Khách hàng: {kh[i]} có trạng thái đơn hàng: {tt[i]}")
print("\n---2.Controlling (break,continue,pass) ---")
for t in tt:
    if t=="huỷ":
        print("Đơn hàng bị huỷ, dừng vòng lặp!")
        break #dừng
    if t=="đang giao":
        print("đang giao-bỏ qua...")
        continue # Bỏ qua bước này
    pass # Placeholder không làm gì cả
print("\n--4.Loop else---")
dss=[2,4,6,8]
for x in dss:
    if x==8:
        print("Tìm thấy 8, dừng vòng lặp!")
        break
else:
    print("dừng")
print("\n--5.reading files (best practice)---")
# Thay vì load hết file, dùng for để đọc từng dòng (tiết kiệm RAM)
# with open('data.txt', 'w') as f: f.write("Dòng 1\nDòng 2") # Tạo file demo
# for line in open('data.txt'):
#     print(line.rstrip())
print("\6--7. List Comprehension---")
nums=[1,2,3]
for x in nums:
    x=x+1
print(f"nums={nums}")