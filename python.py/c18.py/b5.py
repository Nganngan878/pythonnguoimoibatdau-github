#17/07/2026
"""
Dạng 5:Shared List
Đề bài: Viết hàm them_vao(item, ds=[]). Hãy gọi hàm này 2 lần với các giá trị khác nhau và in ra kết quả. Bạn sẽ thấy danh sách cũ vẫn còn ở đó! Sau đó, sửa lại để nó không bị lỗi.
"""
#bãy
def them_vao(item,ds=[]):
    ds.append(item)
    return ds
print(them_vao(1))
print(them_vao(2))
#fixx
def thm_vao_dung(item,ds=None):
    if ds is None:ds=[]
    ds.append(item)
    return ds