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


for _ in range(int(input())):
    n,q,r = imap()
    gr = defaultdict(list)
    for i in range(n-1):
        u,v,w = imap()
        gr[u].append([v,w])
        gr[v].append([u,w])
    anc = [[-1]*(20) for i in range(n+1)]
    level = [0]*(n+1)
    psum = [0]*(n+1)
    def dfs(s,par = -1):
        for i in range(19,0,-1):
            anc[s][i] = anc[anc[s][i-1]][i-1]
        for i,w in gr[s]:
            if i==par: continue
            level[i] = level[s]+1
            anc[i][0] = s
            psum[i] = psum[s]+w
            dfs(i,s)
    dfs(r)
    def lca(u,v):
        if level[u]>level[v]: u,v = v,u
        for i in range(19,-1,-1):
            if level[v]-(1<<i)>=level[u]:
                v = anc[v][i]
        if u==v: return v
        for i in range(19, -1,-1):
            if anc[u][i]!=anc[v][i]:
                u = anc[u][i]
                v = anc[v][i]
        return anc[u][0]
    def pathsum(u,v):
        lc = lca(u,v)
        return psum[u]+psum[v]-2*psum[lc]

    res = []
    for i in range(q):
        u,v = imap()
        res.append(str(pathsum(u,v)))
    print("\n".join(res))

