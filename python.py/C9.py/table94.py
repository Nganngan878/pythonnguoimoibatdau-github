items=['text','',[1,2],[],{'a':1},{},1,0.0,True,False,None]
for item in items:
    print(f"Đối tượng {repr(item)} là: {bool(item)}")
#Tại sao cái này lại cực kỳ quan trọng?
my_list=[1,2]
if len(my_list)>0:
    print("Danh sách không rỗng" )
    #cách chuẩn Python):
    my_list=[1,2]
if my_list:
    print("Danh sách không rỗng")   