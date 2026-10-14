#1. Ví dụ 4-1: Sử dụng return (Trả về toàn bộ danh sách)
def doh():
    return [
        "Homer: D'oh!",
        "Marge: A deer!",
        "Lisa: A female deer!"
    ]

for line in doh():
    print(line)
