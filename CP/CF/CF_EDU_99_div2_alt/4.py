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
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    mx = max(x,max(a))
    dp = [[[-1]*(mx+1) for i in range(mx+1)] for j in range(n+1)]
    dp[0][0][x] = 0
    for i in range(n):
        for j in range(mx+1):
            for k in range(mx+1):
                if dp[i][j][k]==-1: continue
                if a[i]>k and k>=j:
                    if dp[i+1][k][a[i]]==-1:
                        dp[i+1][k][a[i]] = float("inf")
                    dp[i+1][k][a[i]] = min(dp[i+1][k][a[i]], dp[i][j][k]+1)
                if a[i]>=j:
                    if dp[i+1][a[i]][k]==-1:
                        dp[i+1][a[i]][k] = float("inf")
                    dp[i+1][a[i]][k] = min(dp[i+1][a[i]][k], dp[i][j][k])
    res = float("inf")
    for i in range(mx+1):
        for j in range(mx+1):
            if dp[n][i][j]==-1: continue
            res = min(dp[n][i][j], res)
    print(res if res!=float("inf") else -1)
