import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(3*10**6)
mod = int(1e9+7)


n = int(input())
X,Y = imap()
a = [0]*n
b = [0]*n
for i in range(n):
    a[i],b[i] = imap()

dp = [[[-1]*(Y+1) for i in range(X+1)] for j in range(n+1)]
# def rec(i,A,B):
#     if i>=n:
#         return 0 if A>=X and B>=Y else float("inf")
#     if dp[i][A][B]!=-1:
#         return  dp[i][A][B]
#     dp[i][A][B] = min(1+rec(i+1,min(X, A+a[i]), min(Y,B+b[i])), rec(i+1,A,B))
#     return dp[i][A][B]
# ans = rec(0,0,0)
dp = [[[-1]*(Y+1) for i in range(X+1)] for j in range(n+1)]



print(ans if ans<float("inf") else -1)
