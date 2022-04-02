# https://atcoder.jp/contests/abc211/submissions/24502158


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

n,m = imap()
gr = defaultdict(list)
for i in range(m):
    u,v  = imap()
    gr[u].append(v)
    gr[v].append(u)

q = deque([1])
vis = [0]*(n+1)
dp = [0]*(n+1)
dist = [float("inf")]*(n+1)

vis[1] = 1
dist[1] = 0
dp[1] = 1
while q:
    s = q.popleft()
    for i in gr[s]:
        if vis[i]==0:
            q.append(i)
            vis[i] = 1
        if dist[i]>dist[s]+1:
            dist[i] = dist[s]+1
            dp[i] = dp[s]
        elif dist[i]==dist[s]+1:
            dp[i] = (dp[i]+dp[s])%mod
print(dp[n])
