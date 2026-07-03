#Range, Zip, Enumerate
# range
for i in range(9): print(i,end="")
#zip
ten=['Anh','Bình','Cường']
tuoi=[20,21,22]
for t,a in zip(ten,tuoi):
    print(f"\n{t} {a} tuoi")
# Enumerate
color=['đỏ','xanh','vàng']
for i,c in enumerate(color):
 print(f"Vị trí {i} có màu {c}")