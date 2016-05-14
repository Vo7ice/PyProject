#!usr/bin/env python
a = [1,2,3]
b = ['a','b','c']

x0 = zip(a,b)
for x in x0:
    print(x)
print('*'*10)
x1 = map(lambda x,y:(x,y),a,b)
for x in x1:
    print(x)
