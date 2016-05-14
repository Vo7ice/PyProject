#!usr/bin/env python
def isYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False

def isOdd(y):
    return (y%4==0 and (y%100!=0 or y%400 ==0))
def main():
    ys = range(2000,2016)
    oddy = filter(isOdd,ys)
    for x in oddy:
        print (x)

if __name__ == '__main__':
    main()
