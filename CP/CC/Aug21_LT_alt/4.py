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

for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    a = list(map(int,input().split()))
    gr = defaultdict(list)
    g = defaultdict(list)
    for i in range(n-2):
        gr[p[i]].append(i+2)
    fre = [0]*(n+1)
    def dfs(s, st):
        for i in gr[s]:
            if a[st]>a[i]:
                fre[i]+=1
                g[st].append(i)
            elif a[st]<a[i]:
                fre[st]+=1
                g[i].append(st)
            dfs(i,st)
    for i in range(1,n+1):
        dfs(i,i)

    def topological_sorting(fre):
        q = deque()
        for i in range(1,n+1):
            if (not fre[i]):
                q.append(i)
        l = []
        while q:
            u = q.popleft()
            l.append(u)
            for i in g[u]:
                fre[i] -= 1
                if (not fre[i]):
                    q.append(i)
        return l
    s = topological_sorting(fre)[::-1]
    ans = 0
    for dest in range(1,n+1):
        dp = [0]*(n+1)
        dp[dest] = 1
        res = 0
        for i in s:
            for j in g[i]:
                dp[i] += dp[j]
                dp[i]%=mod
            res = (res+dp[i])%mod
        ans = (ans+res)%mod
    print(ans)
    # vis = [0]*(n+1)
    # ans = 0
    # sz = [0]*(n+1)
    # def dfs2(s):
    #     # global ans
    #     # if vis[s]: return 0
    #     # vis[s] = 1
    #     if sz[s]!=0: return sz[s]
    #     sz[s] = 1
    #     res = 1
    #     for i in g[s]:
    #         # res = (res+dfs2(i))%mod
    #         dfs2(i)
    #         sz[s]+=sz[i]
    #         sz[s]%=mod
    #     # ans = (ans+res)%mod
    #     # return res
    # res = 0
    # for i in range(1,n+1):
    #     # res = (res+dfs2(i))%mod
    #     dfs2(i)
    # for i in range(1,n+1):
    #     ans+=sz[i]
    #     ans%=mod
    # print(ans)





