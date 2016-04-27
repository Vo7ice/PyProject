#!/usr/bin/env python
def minToHour(minute = 1000):
    hour = minute / 60
    left = minute % 60

    return (hour, left)

def main():
    sum_minute = long(raw_input('please enter your minute:\n'))
    (hour,minute) = minToHour(sum_minute)
    print 'hour,minute: %d:%d' % (hour,minute)

if __name__ == '__main__':
    main()
