#s. Ví dụ 4-2: Sử dụng yield (Hàm sinh - Generator)
from fastapi import FastAPI
app=FastAPI()
def doh2():
    yield "Homer: D'oh!"
    yield "Marge: A deer!"
    yield "Lisa: A female deer!"

for line in doh2():
    print(line)