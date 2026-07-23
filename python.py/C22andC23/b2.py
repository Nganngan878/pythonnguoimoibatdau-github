#23/07/2026
"""
Dạng2
Bài tập: Viết chương trình in ra danh sách các đường dẫn tìm kiếm của Python (sys.path) và thử dùng phương thức append() để thêm một thư mục mới vào danh sách đó.
"""
import sys
print("Curent sys.path:")
print(sys.path)
sys.path.append("/my/custom/folder")
print("\nUpdated sys.path:")
print(sys.path)