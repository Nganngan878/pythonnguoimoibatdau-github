S = 'abcdefghijklmnop'
print(S[1:10:2])
print(S[::2])
S='hello'
print(S[5:1:-1])
S='abcedfg'
print(S[5:1:-1])
print('code'[1:3])
print('code'[slice(1,3)])
print('code'[::-1])
print('code'[slice(None, None, -1)])
#FILE ECHO.PY
import sys
print(sys.argv)
