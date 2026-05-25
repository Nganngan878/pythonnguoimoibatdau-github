Line=' aaa bbb ccc'
col1=Line[:3]
col2=Line[4:8]
col3=Line[-3:]
print(col1,col2,col3)
line = 'aaa bbb ccc'
cols = line.split()
print(cols)
line = 'Python,3.12,scripting,33'
print( line.split(','))
line = 'youPYarePYaPYstringPYcoder'
print(line.split('PY'))
