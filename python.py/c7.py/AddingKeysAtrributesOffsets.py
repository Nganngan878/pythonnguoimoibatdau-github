import sys
print('This {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
somelist = list('HACK')
print(somelist)
print('zero={0[0]}, two={0[2]}'.format(somelist))
print('first={}, last={}'.format(somelist[0], somelist[-1]) )
parts = (somelist[0], somelist[-1], somelist[1:3]) 
print('first={}, last={}, middle={}'.format(*parts) )