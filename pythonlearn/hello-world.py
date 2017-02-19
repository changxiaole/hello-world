#!/usr/bin/python
import sys

pystr = 'Python'
iscool = 'is cool'
print(pystr[2:5])

class b(object):
    def __init__(self):
        return 0

def func_test():
    if str == '1':
        return 1
    else:
        return '1'

a = func_test()
str = '456'
dict_test = {123 : 'hehe', str : 'value'}
print dict_test[str]
if len(sys.argv) != 4:
    sys.stderr.write('arg count:%d is not equals 3' % len(sys.argv))
    sys.exit(1)
else:
    sys.stderr.write('arg count:%d is ok' % len(sys.argv))
    print('hello world!')