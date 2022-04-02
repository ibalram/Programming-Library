import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod =998244353 #int(1e9+7)

n = int(input())
@lru_cache(None)
def rec(n, lst):
    if n==0: return 1
    res = rec(n-1,lst)
    if lst>1:
        res+=rec(n-1, lst-1)
        res%=mod
    if lst<9:
        res+=rec(n-1,lst+1)
        res%=mod
    return res
def solve(n):
    dp = [[0]*10 for i in range(n+1)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1,n+1):
        for j in range(1,10):
            dp[i][j] = dp[i-1][j]
            if j>1:
                dp[i][j] += dp[i][j-1]
            dp[i][j]%=mod
    return sum(dp[n][1:])%mod
print(solve(n))
res = 0
for i in range(1,10):
    res = (res+rec(n,i))%mod
print(res)
