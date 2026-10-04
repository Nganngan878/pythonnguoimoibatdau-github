#HASH TABLE functions
def get_keys(ht):
    return list(ht.keys())
def has_key(ht,key):
    return key in ht
def get_max(ht):
    mx=float("-inf")
    for v in ht.values():
        if v > mx:
            mx = v
    return mx
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

