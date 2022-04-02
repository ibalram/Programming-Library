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

INF = float('inf')

n,m = imap()
s = []
gr = defaultdict(set)
for i in range(m):
    a,b = imap()
    s.append((a-1,b-1))
    gr[a-1].add(b-1)

def bfs():
    q = deque()
    q.append(0)
    par = {0:0}
    vis = {0:0}
    while q:
        s = q.popleft()
        for i in gr[s]:
            if i in vis: continue
            par[i] = s
            vis[i] = vis[s]+1
            q.append(i)
    return vis,par
vis,par = bfs()
if n-1 not in vis:
    print(-1)
    exit()
ans = vis[n-1]
path = set()
cur = n-1
while cur!=par[cur]:
    path.add(tuple((par[cur],cur)))
    cur = par[cur]
for x,y in s:
    if tuple((x,y)) not in path:
        print(ans)
        continue
    gr[x].remove(y)
    vis,par = bfs()
    if n-1 not in vis:
        print(-1)
    else:
        print(vis[n-1])
    gr[x].add(y)
