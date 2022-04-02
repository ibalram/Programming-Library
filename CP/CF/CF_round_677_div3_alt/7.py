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
from heapq import heapify, heappop as pop, heappush as push

n,m,k = imap()
gr = defaultdict(list)
for i in range(m):
    x,y,w = imap()
    gr[x].append([y,w])
    gr[y].append([x,w])
couriers = []
for i in range(k):
    couriers.append(ilist())

dist = [[float("inf")]*(n+1) for i in range(n+1)]
def shortestPath(s):
    q = [(0,s)]
    heapify(q)
    dist[s][s] = 0
    while q:
        wt,cur =  pop(q)
        for i,w in gr[cur]:
            nwt = w+wt
            if nwt<dist[s][i]:
                dist[s][i] = nwt
                push(q, (nwt,i))
for i in range(1,n+1):
    shortestPath(i)
res = float("inf")
for i in range(1,n+1):
    for j,_ in gr[i]:
        cost = 0
        for u,v in couriers:
            cost += min(dist[u][v],dist[u][i]+dist[j][v],dist[u][j]+dist[i][v])
        res = min(res,cost)
print(res)


