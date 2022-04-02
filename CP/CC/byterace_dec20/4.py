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

t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0]*2 for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = max(a[0],a[-1])
    for i in range(1,(n+1)//2):
        mx = max(a[i], a[~i])
        sm = a[i]+(0 if n%2 and i+1==(n+1)//2 else a[~i])
        dp[i][0] = max(dp[i-1][1], mx+dp[i-1][0])
        dp[i][1] = max(mx+dp[i-1][1], sm+dp[i-1][0])
    print("YES" if max(max(dp[n//2-1]),max(dp[n//2]))>=x else "NO")
