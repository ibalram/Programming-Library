import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = 998244353

n,d = imap()
d+=1
a = [0]*(d+2)
pows = [1]*(max(d,n)+1)
for i in range(1,max(d,n)+1):
    pows[i] = pows[i-1]*2%mod
if d==2:
    print((2+pows[n-1]+3*(pows[n-1]-2))%mod)
    exit()
for i in range(1,d):
    a[i] = pows[max(0,i-1)]*pows[max(0,d-1-i-1)]%mod

    # print(a[i])
    if i>0:
        a[i]+=a[i-1]
# a = [0]+a
# print(a)

def getForDepth(dep):
    height = n-dep-1
    if height*2+1<d:
        return 0
    # print(height, d)
    ans = 0
    if height>=d-1:
        ans += pows[height]
    ans +=2*(a[min(d-1,height)]-a[max(0,d-1-height)-1])%mod
    ans%=mod
    # print(dep,ans, height, a[min(d-1,height)], a[max(0,d-1-height)-1])
    return ans

res = 0
for i in range(n):
    res += (pow(2,i,mod))%mod*getForDepth(i)%mod
    res%=mod
print(res)









# Cradle Point
# ///////////////
# # import requests
# # import mysql.connector
# # import pandas as pd
# """
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# """
# """
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# """
# # print('Hello')


# """

# 2     4     6    7
#    3     5
# """

# def solve(arr):
#     n = len(arr)
#     arr.sort()
#     left = arr[0][0]
#     i = 1
#     right = arr[0][1]
#     result = []
#     for start, end in arr[1:]:
#         if start>right:
#             result.append([left, right])
#             left = start
#         right = max(right, end)
#     result.append([left,right])
#     # print(result)
#     return result

# print(solve([[1,3],[2,6],[8,10],[15,18]])==[[1,6],[8,10],[15,18]])
# print(solve([[1,4],[4,5]])==[[1,5]])





