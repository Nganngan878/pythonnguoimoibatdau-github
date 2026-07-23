#23/07/2026
"""
Dạng 8:
Bài tập: Mô phỏng lại ví dụ changer.py với một biến thông điệp, sau đó dùng reload() để cập nhật giá trị mới của biến khi chương trình đang chạy.
"""
import changer
from importlib import reload
print("Before edit:",changer.message)