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


def solveDijkshtra(n,m, mat):
    heap = [(0,0,0)]
    dist = [[float("inf")]*m for i in range(n)]
    dist[0][0] = 0
    while heap:
        dst, i, j = heappop(heap)
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==0 and dy==0: continue
                x = i+dx*mat[i][j][0]
                y = j+dy*mat[i][j][1]
                if valid(x,y) and dist[i][j]+1<dist[x][y]:
                    dist[x][y] = dist[i][j]+1
                    heappush(heap, (dist[x][y], x,y))
    return dist[n-1][m-1] if dist[n-1][m-1]<float("inf") else -1







def findMinimum(mat):
    n = len(mat)
    m = len(mat[0])
    q = deque([(0,0)])
    dist = [[-1]*m for i in range(n)]
    dist[0][0] = 0
    valid = lambda x,y: 0<=x<n and 0<=y<m
    while q:
        i, j = q.popleft()
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx==0 and dy==0: continue
                x = i+dx*mat[i][j][0]
                y = j+dy*mat[i][j][1]
                if valid(x,y) and dist[x][y]==-1:
                    dist[x][y] = dist[i][j]+1
                    q.append((x,y))
    return dist[n-1][m-1]

import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        mat.append(list(zip(tmp[::2], tmp[1::2])))
    result = findMinimum(mat)
    print(result)




