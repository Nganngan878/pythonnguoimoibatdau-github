
L1 = [0, 0, 0, 0, 0]
L2 = [0] * 5
print(f"L1: {L1}, L2: {L2}")
D1={"a":0,'b':0}
D2=dict(a=0,b=0)
D3={}
D3['a']=0
D3['b']=0
L=[1,2,3]
L.append(4);
L.extend([5,6]);
L.sort(reverse=True)
del L[0]
print(f"Danh sách sau thay đổi: {L}")
D={'a':1 ,'b':2,'c' :3}
D['d']='new'
L=[1,2,3]
my_info = {
    'full_name': ('Phan', 'Thi', 'Ngan'),
    'age': 19,
    'job': 'Developer',
    'contact': {                        
        'email': 'nagpt@email.com',
        'phones': ['090123', '090456']   
    }
}


ho = my_info['full_name'][0]
phone_chinh = my_info['contact']['phones'][0]

print(f"Họ của tôi là: {ho}")
print(f"Số điện thoại chính: {phone_chinh}")
