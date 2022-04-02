import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

n,m,k = imap()

# @lru_cache(None)
dp = [[-1]*(m+1) for i in range(n+1)]
def rec(i,j):
    if dp[i][j]!=-1:
        return dp[i][j]
    if i>=n and j>=m or i>=n:
        dp[i][j] = i-j<=k
        return i-j<=k
    if j>=m:
        dp[i][j] = n-j<=k
        return n-j<=k
    res = 0
    if i+1-j<=k:
        res = (res+rec(i+1,j))%mod
    if i-j-1<=k:
        res = (res+rec(i,j+1))%mod
    dp[i][j] = res
    return res
print(1*rec(0,0))
for i in range(n+1):
    for j in range(m+1):
        print(n-i,m-j,"ans:",dp[i][j])


# dp(i)
#
#
#
dp = [[0]*(m+1) for i in range(n+1)]
# dp[0] = 1
for i in range(n+1):
    # dp[i] = dp[i-1]
    for j in range(0,)
        dp[i][i-k] = 1
    for j in range(1,m+1):
        dp[i][j] = dp[i][j-1]+1
        dp[i][j]%=mod
print(dp)

