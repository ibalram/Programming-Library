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

h,w,n,m = imap()

mat = [[0]*w for i in range(h)]
for i in range(n):
    a,b = imap()
    a-=1
    b-=1
    mat[a][b] = 1

for i in range(m):
    c,d = imap()
    c-=1
    d-=1
    mat[c][d] = -1
for i in range(h):
    f = 0
    for j in range(w):
        if mat[i][j]==-1:
            f = 0
        elif mat[i][j]==1:
            f = 1
        elif f:
            mat[i][j] = 2
    f = 0
    for j in range(w-1,-1,-1):
        if mat[i][j]==-1:
            f = 0
        elif mat[i][j]==1:
            f = 1
        elif f:
            mat[i][j] = 2

for j in range(w):
    f = 0
    for i in range(h):
        if mat[i][j]==-1:
            f = 0
        elif mat[i][j]==1:
            f = 1
        elif f:
            mat[i][j] = 2
    f = 0
    for i in range(h-1,-1,-1):
        if mat[i][j]==-1:
            f = 0
        elif mat[i][j]==1:
            f = 1
        elif f:
            mat[i][j] = 2
res = 0
for i in range(h):
    res+=mat[i].count(1)+mat[i].count(2)
print(res)
