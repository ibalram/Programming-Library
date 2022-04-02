import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(2*10**6)
mod = 998244353 #int(1e9+7)

n = int(input())
a = ilist()
ans = [0]*(10)

def rec(i,sm, k):
    if i>=n:
        return sm==k
    if dp[i][sm]!=-1:
        return dp[i][sm]
    dp[i][sm] = (rec(i+1,(sm+a[i])%10, k)%mod+rec(i+1,(sm*a[i])%10, k)%mod)%mod
    return dp[i][sm]
for i in range(10):
    dp = [[-1]*10 for i in range(n+1)]
    ans[i] = rec(1,a[0],i)
print(*ans, sep="\n")
