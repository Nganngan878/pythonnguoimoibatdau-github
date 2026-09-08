try:
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = a / b
except ValueError:
    print("error:Vui lòng nhập số nguyên")
except ZeroDivisionError:
    print("error:Không thể chia cho 0")
else:
    print("kết quả :", c)
finally:
    print("Chương trình kết thúc")