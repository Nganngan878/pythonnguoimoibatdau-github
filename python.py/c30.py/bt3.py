class Computer:
    def __init__(self,name):
        object.__setattr__(self,'name',name)
        object.__setattr__(self,'bo_nho',{})
    def __getattribute__(self, name):
        if name in {'name', 'bo_nho', '__dict__', '__class__'}:
            return object.__getattribute__(self, name)
        bo_nho = object.__getattribute__(self, 'bo_nho')
        if name in bo_nho:
            return bo_nho[name]
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        self.bo_nho[name] = value
    def __delattr__(self, name):
        if name in self.bo_nho:
            del self.bo_nho[name]
    def __call__(self,*args):
        return f" Call hàm với ham :{args}"
ct=Computer("AI-Bt")
print(ct.name)
ct.ram="14GB"
print(ct.ram)
print(ct.ram)
del ct.ram               
print(ct("Kích hoạt"))
print(getattr(ct, "ram", "RAM chưa được thiết lập"))