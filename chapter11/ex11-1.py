#!/usr/bin/env python
def countToFour1():
    for eachNum in range(5):
        print eachNum,
    
def countToFour2(n):
    for eachNum in range(n,5):
        print eachNum,

def countToFour3(n = 1):
    for eachNum in range(n,5):
        print eachNum,

def main():
    num = int(raw_input('enter your number:\n'))
    countToFour1()
    countToFour2(num)
    countToFour3(num)

if __name__ == '__main__':
    main()
