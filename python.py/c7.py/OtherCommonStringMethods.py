line = "Python's strings are awesome!\n"
print( line.rstrip() )
print(line.upper())
print(line.isalpha())
print(line.endswith('awesome!\n') )
print( line.startswith('Python'))
print(line.find('awesome') != -1 )
print( 'awesome' in line)
sub = 'awesome!\n'
print(line.endswith(sub) )
print(line[-len(sub):] == sub)

