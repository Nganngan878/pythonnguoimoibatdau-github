print({x ** 2 for x in [1, 2, 3, 4]} )
print({x for x in 'py3X'} )
print({x for x in 'py3X' if x.isdigit()} )
print( {c * 4 for c in 'py3X' + 'py2X'} )
S = {c * 4 for c in 'py3X'} 
print(S)
