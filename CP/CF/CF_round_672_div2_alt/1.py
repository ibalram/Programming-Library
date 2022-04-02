from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------

import sys
sys.setrecursionlimit(10**6)
def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left #i is index for left subarray*/
    j = mid #i is index for right subarray*/
    k = left #i is index for resultant merged subarray*/
    while ((i <= mid - 1) and (j <= right)):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

            #this is tricky -- see above explanation/
            # diagram for merge()*/
            inv_count = inv_count + (mid - i)

    while (i <= mid - 1):
        temp[k] = arr[i]
        k += 1
        i += 1

    while (j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1

    # Copy back the merged elements to original array*/
    for i in range(left,right+1,1):
        arr[i] = temp[i]

    return inv_count
def _mergeSort(arr, temp, left, right):
    inv_count = 0
    if (right > left):
        # Divide the array into two parts and call
        #_mergeSortAndCountInv()
        # for each of the parts */
        mid = int((right + left)/2)

        #Inversion count will be sum of inversions in
        # left-part, right-part and number of inversions
        # in merging */
        inv_count = _mergeSort(arr, temp, left, mid)
        inv_count += _mergeSort(arr, temp, mid+1, right)

        # Merge the two parts*/
        inv_count += merge(arr, temp, left, mid+1, right)

    return inv_count
def countSwaps(arr, n):
    temp = [0 for i in range(n)]
    return _mergeSort(arr, temp, 0, n - 1)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    # print(a)
    res = countSwaps(a,n)
    # if a==sorted(a):
    #     print("YES")
    #     continue
    # b = sorted(a, reverse = True)
    # if a!=b:
    if res<=n*(n-1)//2-1:
        print("YES")
    else:
        print("NO")
