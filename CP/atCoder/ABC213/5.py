# https://atcoder.jp/contests/abc213/submissions/24871360
# https://atcoder.jp/contests/abc213/submissions/24871360

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
from heapq import *

n,m = imap()
mat = []
for i in range(n):
    row = list(input().strip())
    mat.append(row)

nw = set([(0,1),(0,-1),(1,0),(-1,0)])
nt = set([(2,2),(-2,-2),(2,-2),(-2,2)])

# O(n*m*log(n*m)) ~ 5*10^6
def dijkshra(n,m,mat):
    q = [(0,0,0)]
    dist = [[float("inf")]*(m+1) for i in range(n+1)]
    dist[0][0] = 0
    valid = lambda x,y:0<=x<n and 0<=y<m
    while q:
        _,x,y = heappop(q)
        for dx,dy in nw:
            xx = x+dx
            yy = y+dy
            if valid(xx,yy):
                if mat[xx][yy]=="." and dist[xx][yy]>_:
                    dist[xx][yy] = _
                    heappush(q,(_,xx,yy))
        for dx in range(-2,3):
            for dy in range(-2,3):
                if (dx,dy) in nw or (dx,dy) in nt: continue
                xx = x+dx
                yy = y+dy
                if valid(xx,yy):
                    # print(xx,yy,_, dist)
                    if dist[xx][yy]>_+1:
                        dist[xx][yy] = _+1
                        heappush(q,(_+1,xx,yy))
    print(dist[n-1][m-1])

def bfs01(n,m,mat):
    q = deque([(0,0)])
    dist = [[float("inf")]*(m+1) for i in range(n+1)]
    dist[0][0] = 0
    valid = lambda x,y:0<=x<n and 0<=y<m
    while q:
        x,y = q.popleft()
        for dx,dy in nw:
            xx = x+dx
            yy = y+dy
            if valid(xx,yy):
                if mat[xx][yy]=="." and dist[xx][yy]>dist[x][y]:
                    dist[xx][yy] = dist[x][y]
                    q.appendleft((xx,yy))
        for dx in range(-2,3):
            for dy in range(-2,3):
                if (dx,dy) in nw or (dx,dy) in nt: continue
                xx = x+dx
                yy = y+dy
                if valid(xx,yy):
                    # print(xx,yy,_, dist)
                    if dist[xx][yy]>dist[x][y]+1:
                        dist[xx][yy] = dist[x][y]+1
                        q.append((xx,yy))
    print(dist[n-1][m-1])

# dijkshra(n,m,mat)
bfs01(n,m,mat)


