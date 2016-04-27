#!/usr/bin/env python

def getRate(money,choice = 1):
    choices = [1,2,3,4]
    rates = [0.03,0.04,0.05,0.06]
    for eachItem in choices:
        if (choice == eachItem):
            return rates[choice-1] * money

    return rates[0] * money



def menu():
    money = float(raw_input('enter your money:'))
    print 'There is some fax rate.'
    print """ 1.goods (3%)
 2.transport (4%)
 3.finacial (5%)
 4.communicate (6%)"""
    choice = raw_input('enter your number:')
    if not choice:
        rate = getRate(money)
    else:
        rate = getRate(money,int(choice))
    print "you have to pay '%s'$" % str(rate)

if __name__ == '__main__':
    menu()
