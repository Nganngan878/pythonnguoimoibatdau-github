class reposibity:
    def __init__(self,list_item):
        self.items=list(list_item)
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        self.items[index]=value
    def __delitem__(self,index):
        del self.items[index]
kho = reposibity(["appple","orange"])
print("1. Lấy phần tử index 1:", kho[1]) 

kho[1] = "Mít"
print("2. Sau khi sửa index 1:", kho[1]) 

del kho[0]
print("3. Sau khi xóa index 0:", kho[:]) 