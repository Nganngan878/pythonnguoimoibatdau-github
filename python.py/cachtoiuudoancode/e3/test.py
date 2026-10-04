#Mudules,packages,namespaces
def get_max(list):
    mx=float("-inf")
    for n in list:
        if n > mx:
            mx = n
    return mx
def get_min(list):
    mn=float("inf")
    for n in list:
        if n < mn:
            mn = n
    return mn
def get_average(list):
    return sum(list)/len(list)
def get_median(list):
    lst=sorted(list)
    if len(lst)%2==0:
        return (lst[len(lst)//2-1]+lst[len(lst)//2])/2
    else:
        return lst[(len(lst)-1)/2]
    
#HASH TABLE functions
def get_keys(ht):
    return list(ht.keys())
def has_key(ht,key):
    return key in ht
def max_value(ht):
    mx=float("-inf")
    for v in ht.values():
        if v > mx:
            mx = v
    return mx
def min_value(ht):
    mn=float("inf")
    for v in ht.values():
        if v < mn:
            mn = v
    return mn

