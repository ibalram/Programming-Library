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

from random import randint

# x = "<>="
# print("".join(x[randint(0,2)] for i in range(1000)))

n = int(input())
a = input().strip()
# n = 100
# a = a[:n]
# @lru_cache(None)
# def dp(i, pre):
#     if i==n-1:return 1
#     res = 0
#     if a[i]=="<":
#         for j in range(pre+1,n+1):
#             res+=dp(i+1,j)
#             res%=mod
#     elif a[i]==">":
#         for j in range(pre-1,0,-1):
#             res+=dp(i+1,j)
#             res%=mod
#     else:
#         res+=dp(i+1,pre)
#         res%=mod
#     return res
# print(sum(dp(0,i) for i in range(1,n+1))%mod)

dp = [[0]*(n+1) for i in range(n+1)]
for j in range(n):
    dp[0][j] = 1
# for i in range(n-1):
#     if a[i]=="<":
#         for j in range(n):
#             for k in range(j):
#                 dp[i+1][j] += dp[i][k]
#                 dp[i+1][j]%=mod
#     elif a[i]==">":
#         for j in range(n):
#             for k in range(j+1,n):
#                 dp[i+1][j] += dp[i][k]
#                 dp[i+1][j]%=mod
#     else:
#         for j in range(n):
#             dp[i+1][j] += dp[i][j]
#             dp[i+1][j]%=mod
for i in range(n-1):
    for k in range(1,n):
        dp[i][k]+=dp[i][k-1]
        dp[i][k]%=mod
    if a[i]=="<":
        for j in range(n):
            dp[i+1][j]+=dp[i][j-1] if j else 0
            dp[i+1][j]%=mod
    elif a[i]==">":
        for j in range(n):
            dp[i+1][j] += dp[i][n-1]-dp[i][j]+mod
            dp[i+1][j]%=mod
    else:
        for j in range(n):
            dp[i+1][j] += dp[i][j]-(dp[i][j-1] if j else 0)
            dp[i+1][j]%=mod
# print(dp)
print(sum(dp[n-1])%mod)




