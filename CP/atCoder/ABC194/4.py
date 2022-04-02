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

n = int(input())

dp = [0]*(n+1)
dp[1] = 1
pf = 1
for i in range(2,n+1):
    dp[i] = pf/(i-1)
    pf+=dp[i]
print(dp[n])
