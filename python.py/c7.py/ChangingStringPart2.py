S='textly!';
print(S[:4] +'ful' +S[-1]);
S='textly!';
print(S.replace('ly','ful'))
print( '--@--@--@--'.replace('@', 'PY', 2))
S='xxxxPYxxxxPyxxx'
where = S.find('PY') 
print(where)
S = S[:where] + 'CODE' + S[(where+2):]
print(S)
S = 'xxxxPYxxxxPYxxxx'
print(S.replace('PY', 'CODE', 1) )
S = S.replace('PY', 'CODE')
print(S)
S='text'
L=list(S)
print(L)
L[0]='h'
L[3]='!'
print(L)
S=''.join(L)
print(S)
print( 'PY'.join(['which', 'language', 'is', 'best', '?']))