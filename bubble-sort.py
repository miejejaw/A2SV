import math
import os
import random
import re
import sys

def countSwaps(a):
    count = 0
    for i in range(n):
        for j in range(1,n):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
                count += 1
    print(f"Array is sorted in {count} swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
