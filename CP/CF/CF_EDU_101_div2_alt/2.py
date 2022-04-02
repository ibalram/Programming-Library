import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------

import os, sys
from functools import lru_cache

sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    # @lru_cache(None)
    # def rec(i,j):
    #     if i>=n and j>=m:
    #         return 0
    #     if i>=n:
    #         return max(0, b[j])
    #     if j>=m:
    #         return max(0, a[i])
    #     res = 0
    #     res = max(res, rec(n,m), a[i]+rec(i+1, j), b[j]+rec(i,j+1))
    #     return res
    # print(rec(0,0))
    res = 0
    for i in range(1,n):
        a[i] += a[i-1]
    for i in range(1,m):
        b[i] += b[i-1]
    for i in range(n):
        for j in range(m):
            res = max(res, a[i],b[j], a[i]+b[j])
    print(res)
