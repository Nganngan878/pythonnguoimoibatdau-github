#23/07/2026
"""
Dạng 7:
Bài tập: Import một module, giả lập quá trình thay đổi nội dung của module đó trong bộ nhớ, sau đó dùng reload() để cập nhật thay đổi mà không cần khởi động lại chương trình.
"""
from importlib import reload
import my_module
print("Truoc khi sua:", my_module.version)

print("\n--- HEY! HUNG DAU ---")
print("Bay giờ bạn hãy vào tệp 'my_module.py', sửa lại thành:")
print('version = "Version 2: Da cap nhat"')
print("Rồi lưu file (Ctrl+S / Cmd+S) lại, sau đó bấm chạy lại chương trình này!")