#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    num = helper(n,0,len(n)-1)
    nums = str(num * k)
    return helper(nums,0,len(nums)-1)    
    
def helper(nums,left,right):
    if left == right:
        return int(nums[left])
    mid = left + (right-left)//2
    left = helper(nums,left,mid)
    right = helper(nums,mid+1,right)
    
    temp = left + right
    if temp > 9:
        temp = 1 + temp%10
    return temp
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
