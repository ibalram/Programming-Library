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

n,m,c = imap()

ma = []
for i in range(n):
    ma.append(ilist())
# mat2 = [i[::-1] for i in ma]

res =float("inf")
dist = lambda x,y : abs(x[0]-y[0])+abs(x[1]-y[1])


def solve(mat):
    global res
    # for i in range(n):
    #     # print(*mat[i])
    #     for j in range(m):
    #         mat[i][j] = [mat[i][j], i,j]
    #     # print(*mat[i])
    for i in range(1,n):
        curcst = mat[i][0]
        ncst = mat[i][0]
        cst = mat[i-1][0]
        # print(cst,curcst)
        res = min(res, c+cst+curcst)
        if cst+c<ncst:
            ncst = cst+c
        mat[i][0] = ncst

    for j in range(1,m):
        curcst = mat[0][j]
        ncst  = mat[0][j]
        cst  = mat[0][j-1]
        res = min(res, c+cst+curcst)
        if cst+c<ncst:
            ncst = cst+c
        mat[0][j] = ncst
    for i in range(1,n):
        for j in range(1,m):
            curcst = mat[i][j]
            ncst = mat[i][j]
            if i-1>=0:
                cst= mat[i-1][j]
                res = min(res, c+cst+curcst)
                if cst+c<ncst:
                    ncst = cst+c
            if j-1>=0:
                cst = mat[i][j-1]
                res = min(res, c+cst+curcst)
                if cst+c< ncst:
                    ncst = cst+c
            mat[i][j] = ncst
    mat = []
solve([i[:] for i in ma])
solve([i[::-1] for i in ma])
solve([i[:] for i in ma[::-1]])
solve([i[::-1] for i in ma[::-1]])

print(res)


