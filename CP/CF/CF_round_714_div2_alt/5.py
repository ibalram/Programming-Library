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
    gr = defaultdict(list)
    edges = []
    for i in range(n-1):
        a,b = imap()
        edges.append((a,b))
        gr[a].append(b)
        gr[b].append(a)
    a = [0]+ilist()
    ssum = [0]*(n+1)
    par = [i for i in range(n+1)]
    def dfs(s,pr):
        ssum[s] = a[s]
        for i in gr[s]:
            if i==pr: continue
            par[i] = s
            dfs(i,s)
            ssum[s]+=ssum[i]
    def dfs2(s,pr):
        stack = [(s,pr)]
        st = []
        while stack:
            s,pr = stack.pop()
            st.append((s,pr))
            ssum[s] = a[s]
            for i in gr[s]:
                if i==pr: continue
                par[i] = s
                stack.append((i,s))
        while st:
            s,pr = st.pop()
            if pr!=-1:
                ssum[pr]+=ssum[s]
    dfs(1,-1)
    # print(ssum)
    tot = sum(a)
    res = float("inf")
    idx = -1
    for i,(u,v) in enumerate(edges):
        if v==par[u]:
            u,v = v,u
        if res>tot-ssum[v]:
            res = tot-ssum[v]
            idx = i
    print(idx+1)




