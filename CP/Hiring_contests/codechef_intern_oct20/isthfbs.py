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


for _ in range(int(input())):
    n,m,k = imap()
    gr = defaultdict(list)
    for i in range(m):
        u,v = imap()
        gr[u].append(v)
        gr[v].append(u)
    q = deque()
    vis = {}
    for i in ilist():
        q.append(i)
        vis[i] = 0
    queries = []
    Q = int(input())
    for i in range(Q):
        queries.append(int(input()))
    while q:
        s = q.popleft()
        for i in gr[s]:
            if i in vis: continue
            vis[i] = vis[s]+1
            q.append(i)
    res = [str(vis[i] if i in vis else -1) for i in queries]
    print("\n".join(res))

