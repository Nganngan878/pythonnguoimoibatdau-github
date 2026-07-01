
if not 1:
    print("This will not be printed because the condition is True.")
else:
    print("This will be printed because the condition is False.")
False

os='iOS'
mode='mobile'
if  os in ['iOS', 'Android']:
    print('macOS')
elif mode ==' moblile' and os !='Windows':
    print('Linux')
else:
    print('unknown?')

if mode=='mobile':
    if os=='Android':
        print('Linux')
    elif os!='Windows':
        print('macOS')
#if/elif/else
tuoi=19
member=True
if tuoi>=18 and member:
    print("Đủ tuổi mua vé")
elif tuoi>=18 and not member:
    print("Cần đăng ký thể lệ thành viên")
else:
    print("Chưa đủ tuổi mua vé")
#Dạng 2: Thay thế "Switch/Case" bằng Dictionary (Tra cứu nhanh)
#Chuyển đổi mã lỗi (Error code) thành thông báo cụ thể.
error_code = 404
messagess={
    200:"ok",
    404:"Not Found",
    500:"Internal Server Error"
}


print(messagess.get(error_code, "Unknown Error"))
#Dạng 3: Lựa chọn hiện đại (Cấu trúc match/case)
#Bài tập: Xử lý các trạng thái đơn hàng.
status='shipped'
match status:
    case 'pending':
        print("đang xử lý ")
    case 'shipped':
        print("đang giao hàng")
    case 'delivered':
        print("đã giao hàng")
    case 'canceled':
        print("đơn hàng đã hủy")
