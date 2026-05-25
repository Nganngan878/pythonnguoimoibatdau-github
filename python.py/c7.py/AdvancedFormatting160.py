import sys
print('{0:10} = {1:10}'.format('text', 123.4567))
print( '{0:>10} = {1:<10}'.format('text', 123.4567))
print( '{1[kind]:^10} = {0.platform:^10}'.format(sys, dict(kind='laptop')))