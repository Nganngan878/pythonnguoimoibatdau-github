#23/07/2026
"""
Dạng 6:
Bài tập: Tạo một module tự định nghĩa chứa một vài biến, sau đó dùng hàm dir() và từ điển __dict__ để khám phá không gian tên của nó.
"""
import math
print("Uisng dir(math):")
print(dir(math)[:5])
print("\nUsing mant.__dict__ keys:")
print(list(math.__dict__.keys())[:5])