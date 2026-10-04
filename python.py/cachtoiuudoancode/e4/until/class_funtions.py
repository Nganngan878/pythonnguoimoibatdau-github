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
def get_sum(list):
    return sum(list)
def get_product(list):
    product=1
    for n in list:
        product*=n
    return product
