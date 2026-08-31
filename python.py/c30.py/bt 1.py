#Cách tự tùy biến __getitem__ để đọc dữ liệu từ một file text hoặc database thay vì từ list.
class Nicknamepro:
    def __init__(self,name,point):
        self.name=name
        self.point=point
        print(f"[__init__]: Đã tạo tài khoản cho {self.name}")
    def __str__(self):
        return f"Nicknamepro(name='{self.name}',point={self.point})"
    def __repr__(self):
        return f"Nicknamepro(name='{self.name}',point={self.point})"
    def __add__(self,other):
        if isinstance(other,Nicknamepro):
            return Nicknamepro(f"{self.name} & {other.name}",self.point +other.point)
        elif isinstance(other,int):
            return Nicknamepro(self.name,self.point +other)
    def __radd__(self,other):
        return self.__add__(other)
    def __iadd__(self,other):
        self.point  +=other if isinstance(other,int) else other.point
        return self
    def __or__(self,other):
        return f"Gộp nhóm {self.name} | {other.name}"
    def __bool__(self):
        return self.point >0
    def __eq__(self, other):
        return self.point ==other.point
    def __lt__(self,other):
        return self.point <other.point
    def __del__(self):
        print(f"[__del__]: TaiKoan {self.name} đã delete !")
tk1=Nicknamepro("An",50)
tk2=Nicknamepro("in",510)
print(tk1)            
print(repr(tk2))
tk3=tk1+tk2
tk4=20+tk1
tk1 +=30
print(" ss tk1 ==tk2 :" ,tk1==tk2)
print(" ss tk1 <tk2 :",tk1 <tk2)
print("phép toán or:", tk1 |tk2)
if tk1 :
    print(f"{tk1.name} đang activity no hop le ")
del tk4

