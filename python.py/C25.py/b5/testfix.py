#27/07/2026
"""
fix



"""
import mod
from mod import x

print("Giá trị x ban đầu:", x)
import importlib
importlib.reload(mod)
print("Giá trị x sau khi reload (dùng mod.x):", mod.x)  
print("Giá trị x sau khi reload (dùng biến x cũ):", x)  