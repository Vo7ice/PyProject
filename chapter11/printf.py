#!/usr/bin/env python

def printf(arg0, *nkw):
    count = 0
    result = []
    while (arg0.find('%') != -1):
        position = arg0.index('%')
        temp = arg0[0:position] + nkw[count]
        arg0 = arg0[position+2:]
        count += 1
        result.append(temp)
    else:
        print(arg0)
    print(str(result))

def main():
    printf("this is a s demo s",'end','start')

if __name__ == '__main__':
    main()
