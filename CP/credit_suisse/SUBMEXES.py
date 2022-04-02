import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------


import sys
sys.setrecursionlimit(10**6)
for _ in range(int(input())):
    n = int(input())
    from collections import defaultdict
    g = defaultdict(list)
    ls = list(map(int,input().split()))
    for i in range(2,n+1):
        g[ls[i-2]].append(i)
    sz = [1]*(n+1)
    dp = [0]*(n+1)
    ans = [0]*(n+1)
    def dfs(s):
        for i in g[s]:
            dfs(i)
            sz[s]+=sz[i]
            dp[s] = max(dp[s],dp[i]+1)
        for i in g[s]:
            ans[s] = max(ans[i],ans[s])
        ans[s]+=sz[s]

    dfs(1)
    for i in range(1,n+1):
        g[i].sort(key = lambda k: [-dp[k], -sz[k]])
    mp = {}
    # print(sz)
    s = 1
    res = 1
    while g[s]:
        res+=sz[s]
        s = g[s][0]
    # res = 0
    # for i in mp.keys():
    #     res+=i
    # print(res)
    print(ans[1])

