#!/usr/bin/env python
def max2(m, n):
    if(m > n):
        return m
    else:
        return n

def min2(m, n):
    if(m > n):
        return n
    else:
        return m

def my_max(nums):
    max = nums[0]
    for eachItem in nums:
        max = max2(max,eachItem)
    
    return max

def my_min(nums):
    min = nums[0]
    for eachItem in nums:
        min = min2(min,eachItem)

    return min



if __name__ == '__main__':
#    print 'max:%d' % max2(8,4)
#    print 'min:%d' % min2(4,8)
    nums = [3,6,1,10,9]
    print 'max:%d' % my_max(nums)
    print 'min:%d' % my_min(nums)
