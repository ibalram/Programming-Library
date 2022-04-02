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
    n,m = map(int,input().split())
    gr = defaultdict(list)
    edges = []
    for i in range(m):
        u,v = map(int,input().split())
        edges.append([u,v])
        gr[u].append(v)
        gr[v].append(u)
    vis = [0]*(n+1)
    gr2 = defaultdict(list)
    def dfs(s):
        vis[s] = 1
        for i in gr[s]:
            if vis[i]: continue
            gr2[i].append(s)
            gr2[s].append(i)
            dfs(i)
    dfs(1)
    if vis.count(0)>1:
        print("NO")
        continue
    def rec(s, par):
        taken = noTaken = 0
        for i in gr2[s]:
            if i==par:continue
            taken, noTaken = rec(i,s)
            res = max(res, )
