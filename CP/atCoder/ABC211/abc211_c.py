# https://atcoder.jp/contests/abc211/submissions/24499123


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

s = input().strip()
n = len(s)
a = "chokudai"
m = len(a)

# @lru_cache(None)
# def rec(i,j):
#     if j>=m:
#         return 1
#     if i>=n:
#         return 0
#     res = rec(i+1,j)
#     if s[i]==a[j]:
#         res = (res+rec(i+1,j+1))%mod
#     return res

# print(rec(0,0))

def count(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n+1):
        dp[0][i] = 0
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j])%mod
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]%mod
print(count(s,a))
