
L = []
print(L)
L = [123, 'abc', 1.23, {}]
print(L)
L = ['Pat', 40.0, 'dev', 'mgr']
print(L)
L = list('code')
print(L)
L = list(range(-4, 4))
print(L)

for i in range(len(L)):
    print(L[i])

L = [[1, 2], [3, 4]]
for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j])
        print(L[i:j])
        print(len(L))


x = 0
print(3 in L) 
for c in L: print(x)

L.append(4)
print(L)

L.extend([5, 6, 7])
print(L)

L.insert(0, x)
print(L)

L = [6, 2, 8, 1, 6, 4] 
print(f"Danh sách mới để test: {L}")

X = 6
if X in L:
    print(f"Index của {X}: {L.index(X)}")
    print(f"Số lần xuất hiện của {X}: {L.count(X)}")

L.sort()
print(f"Sau khi sort: {L}")
L.reverse()
print(f"Sau khi reverse: {L}")

L_moi = L.copy()
print(f"Bản copy: {L_moi}")

L.clear()
print(f"Sau khi clear: {L}")

L = [10, 20, 30]
L.pop(0) 
print(f"Sau khi pop: {L}")
L.remove(20) 
print(f"Sau khi remove: {L}")

