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

# for _ in range(int(input())):
#     x,y,n = map(int,input().split())
#     res  = 0
#     for i in range(n+1):
#         if x^i<y^i:
#             res+=1
#     print(res)

for _ in range(int(input())):
    x,y,n = map(int,input().split())
    res  = 0
    dp = [0]
    for i in range(31):
        a = (x>>i)&1
        b = (y>>i)&1
        if a ==b:
            dp[i] = dp[i-1]
        elif a<b:
            dp[i] = dp[i-1]
    print(res)
