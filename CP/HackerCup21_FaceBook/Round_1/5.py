import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
def do(inp, out):
    if os.path.exists(inp+'.txt'): sys.stdin=open(inp+'.txt','r')
    if os.path.exists(out+'.txt'): sys.stdout=open(out+'.txt', 'w')

do("traffic_control_input", "out")
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

class DSU:
    def __init__(self, n):
        self.par = list(range(n+1))

    def addComp(self, comps):
        for comp in comps:
            p = comp[0]
            for i in comp[1:]:
                self.par[i] = p

    def find(self, a):
        if self.par[a]==a: return a
        cur = a
        while cur!=self.par[cur]:
            cur = self.par[cur]
        self.par[a] = cur
        return self.par[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a==b: return
        self.par[b] = a



for _ in range(int(input())):
    res = 0
    n = int(input())
    edges =[]
    gr = defaultdict(list)
    for i in range(n-1):
        edges.append(ilist())
        a,b,c = edges[i]
        gr[a].append(b)
        gr[b].append(a)
    par = [i for i in range(n+1)]
    sz = [1]*(n+1)
    def dfs(s,pr):
        for i in gr[s]:
            if i==pr: continue
            par[i] = s
            dfs(i,s)
            sz[s] +=sz[i]
    dfs(1,-1)

    lst = list(n-1)
    lst.sort(key=lambda x: -edges[2])
    dsu = DSU(n)

    print("Case #{}: {}".format(_+1, res))


# ABC214 D
# n = int(input())
# g = defaultdict(list)
# edges = []
# for i in range(n-1):
#     u,v,w = imap()
#     # g[u].append((v,w))
#     # g[v].append((u,w))
#     edges.append((w,(u,v)))
# size = [1]*(n+1)
# par = {i:i for i in range(n+1)}
# def find(a):
#     if par[a]==a: return par[a]
#     par[a] = find(par[a])
#     return par[a]

# def union(a,b):
#     a = find(a)
#     b = find(b)
#     if a==b: return
#     if size[a]<size[b]: a,b = b,a
#     size[a]+=size[b]
#     par[b] = a
# res = 0
# edges.sort()
# for w,(u,v) in edges:
#     u = find(u)
#     v = find(v)
#     res+=w*size[u]*size[v]
#     union(u,v)
# print(res)
