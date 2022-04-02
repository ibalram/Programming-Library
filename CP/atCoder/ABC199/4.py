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

n, m = imap()

deg = [0]*(n+1)
gr =defaultdict(list)
fail = 0
for i in range(m):
    u,v = imap()
    gr[u].append(v)
    gr[v].append(u)
    deg[u]+=1
    deg[v]+=1
    if deg[u]>2 or deg[v]>2:
        fail = 1
if fail:
    print(0)
    exit()


def dfs(s, par):
    # global loop#,sz
    loop = 0
    sz = 1
    for i in gr[s]:
        if not vis[i]:
            vis[i] = 1
            x,y=dfs(i, s)
            loop|=y
            sz+=x
        elif i!=par:
            loop = 1
    return sz,loop

def calc(sz, loop):
    @lru_cache(None)
    def rec(i,color0, lst):
        if i>=sz:
            if loop: return color0!=lst
            return 1
        res = 0
        for j in [0,1,2]:
            if j!=lst:
                res+=rec(i+1, color0, j)
        return res
    return rec(1,0,0)+rec(1,1,1)+rec(1,2,2)
vis = [0]*(n+1)
ans = 1
for i in range(1,n+1):
    if not vis[i]:
        vis[i] = 1
        sz,loop = dfs(i, -1)
        # print(sz,loop)
        ans*=calc(sz,loop)
print(ans)




