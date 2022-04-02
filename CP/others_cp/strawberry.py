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
mod = int(1e9+7)



import sys
sys.setrecursionlimit(10**7)

def solve(arr, num):
    n = len(arr)
    from functools import lru_cache
    @lru_cache(None)
    def rec(i, num):
        if i>=n or num<=0:
            return 0
        res = rec(i+1,num)
        if arr[i]<=num:
            res = max(res, arr[i]+rec(i+2,num-arr[i]))
        return res
    return rec(0,num)







print(solve([50, 10, 20,30,40], 100))
print(solve([15,20], 10))
