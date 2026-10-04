def get_max(ngan):
    mx=float("-inf")
    for n in ngan:
        if n > mx:
            mx = n
    return mx
def get_min(ngan):
    mn=float("inf")
    for n in ngan:
        if n < mn:
            mn = n
    return mn
def get_average(ngan):
    return sum(ngan)/len(ngan)
def get_median(ngan):
    lst=sorted(ngan)
    if len(lst)%2==0:
        return (lst[len(lst)//2-1]+lst[len(lst)//2])/2
    else:
        return lst[(len(lst)-1)//2]
def get_sum(ngan):
    return sum(ngan)
def get_product(ngan):

    product=1
    for n in ngan:
        product*=n
    return product