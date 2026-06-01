shared_list=[1, 2, 3]
L=shared_list
X=shared_list
D=shared_list
X[1]="THAY ĐỔI"
print("L:",L)
print("X:",X)
print("D:",D)
import copy
L=[1, 2, 3]
X=L.copy()
X[1]="khác biệt"
print("L:",L)
print("X:",X)