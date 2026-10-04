def get_max(dict):
    mx=float("-inf")
    for v in dict.values():
        if v > mx:
            mx = v
    return mx
def get_min(dict):
    mn=float("inf")
    for v in dict.values():
        if v < mn:
            mn = v
    return mn
def get_average(dict):
    return sum(dict.values())/len(dict)
def get_median(dict):
    lst=sorted(dict.values())
    if len(lst)%2==0:
        return (lst[len(lst)//2-1]+lst[len(lst)//2])/2
    else:
        return lst[(len(lst)-1)/2]
def get_sum(dict):
    return sum(dict.values())
def get_product(dict):
    product=1
    for v in dict.values():
        product*=v
    return product
def get_keys(dict):
    return list(dict.keys())