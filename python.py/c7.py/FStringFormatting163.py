what='coding'
tool='Python'
print( f'Learning {what} in {tool}')
print( 'Learning %s in %s' % (what, tool) )
print('Learning {} in {}'.format(what, tool) )
task = f'Learning {what.upper() + '!'} in {tool + str(3.12)}'
print(task)


