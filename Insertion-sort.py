#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            temp = arr[i+1]
            j = i+1
            while j>0 and arr[j-1]>temp:
                arr[j] = arr[j-1]
                print(*(arr))
                j -= 1
            arr[j] = temp
            print(*(arr))
        
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
