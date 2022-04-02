import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------

import sys
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = int(1e9+7)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pf = [0]+a[:]
    for i in range(1,n+1):
        pf[i]^=pf[i-1]
    maxK = 0
    # @lru_cache(None)
    def recur(i,prev,k):
        global maxK
        if k<=0:
            return prev==n
        if i>n:
            return 0
        if cache[i][prev][k]!=-1:
            return cache[i][prev][k]
        res = recur(i+1,prev, k)
        cnt = maxK-k
        if (pf[i]^pf[prev])%(1<<cnt)==0:
            res = (res+ recur(i+1, i, k-1))%mod
        cache[i][prev][k] = res
        return res
    res = 0
    for k in range(1,n+1):
        maxK = k
        cache = [[[-1]*(k+1) for i in range(n+1)] for j in range(n+1)]
        res += recur(1,0,k)
        res%=mod
    print(res)

    # def solve(k):
    #     dp = [[[0]*(k+1) for i in range(n+1)] for j in range(n+1)]
    #     for i in range(1,n+1):
    #         for j in range(i):
    #             # dp[i][j][0] = dp[i-1][j][0]
    #             dp[i][j][0] = 1
    #             for _k in range(1,k+1):
    #                 dp[i][j][_k] = dp[j][0][_k]
    #                 if pf[i]^pf[j]%(1<<(_k-1))==0:
    #                     dp[i][j][_k]+=dp[j][0][_k-1]
    #                     dp[i][j][_k]%=mod
    #     return dp[n][0][_k]
