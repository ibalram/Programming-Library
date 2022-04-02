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

from math import ceil
for _ in range(int(input())):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().strip())))
    # for i in mat:
    #     print(*i)
    res = []

    def two(i,j,sqr):
        x = []
        y = []
        f = 1
        for ii in range(2):
            for jj in range(2):
                if sqr[ii][jj]==0:
                    x.append([i+ii,j+jj])
                    y.append([i+ii,j+jj])
                elif f:
                    x.append([i+ii,j+jj])
                    f = 0
                else:
                    y.append([i+ii,j+jj])

        res.append(x)
        res.append(y)

    def one(i,j,sqr,ones):
        z = []
        for ii in range(2):
            for jj in range(2):
                if sqr[ii][jj]:
                    ones = [[ii,jj]]
                    break
        anti = [ones[0][0]^1, ones[0][1]^1]
        for ii in range(2):
            for jj in range(2):
                if [ii,jj] !=anti:
                    z.append([i+ii,j+jj])
                    sqr[ii][jj]^=1
        res.append(z)
        two(i,j,sqr)
    for i in range(0,n-1,2):
        for j in range(0,m-1,2):
            sqr = [[0,0],[0,0]]
            ones = []
            if mat[i][j]:
                ones.append([i,j])
                sqr[0][0] = 1
            if mat[i+1][j]:
                ones.append([i+1,j])
                sqr[1][0] = 1
            if mat[i][j+1]:
                ones.append([i,j+1])
                sqr[0][1] = 1
            if mat[i+1][j+1]:
                ones.append([i+1,j+1])
                sqr[1][1] = 1
            if len(ones)==0:
                continue
            elif len(ones)==3:
                res.append(ones)
            elif len(ones)==2:
                two(i,j,sqr)
            elif len(ones)==1:
                one(i,j,sqr, ones)
            elif len(ones)==4:
                sqr[0][0] = sqr[0][1] = sqr[1][0] = 0
                res.append(ones[:3])
                one(i,j,sqr, ones[3:])
    if m%2:
        j = m-2
        for i in range(0,n-1,2):
            mat[i][j] = 0
            mat[i+1][j] = 0
            sqr = [[0,0],[0,0]]
            ones = []
            if mat[i][j]:
                ones.append([i,j])
                sqr[0][0] = 1
            if mat[i+1][j]:
                ones.append([i+1,j])
                sqr[1][0] = 1
            if mat[i][j+1]:
                ones.append([i,j+1])
                sqr[0][1] = 1
            if mat[i+1][j+1]:
                ones.append([i+1,j+1])
                sqr[1][1] = 1
            if len(ones)==0:
                continue
            elif len(ones)==3:
                res.append(ones)
            elif len(ones)==2:
                two(i,j,sqr)
            elif len(ones)==1:
                one(i,j,sqr,ones)
            elif len(ones)==4:
                sqr[0][0] = sqr[0][1] = sqr[1][0] = 0
                res.append(ones[:3])
                one(i,j,sqr, ones[3:])
    if n%2:
        i = n-2
        for j in range(0,m-1,2):
            mat[i][j] = 0
            mat[i][j+1] = 0
            sqr = [[0,0],[0,0]]
            ones = []
            if mat[i][j]:
                ones.append([i,j])
                sqr[0][0] = 1
            if mat[i+1][j]:
                ones.append([i+1,j])
                sqr[1][0] = 1
            if mat[i][j+1]:
                ones.append([i,j+1])
                sqr[0][1] = 1
            if mat[i+1][j+1]:
                ones.append([i+1,j+1])
                sqr[1][1] = 1
            if len(ones)==0:
                continue
            elif len(ones)==3:
                res.append(ones)
            elif len(ones)==2:
                two(i,j,sqr)
            elif len(ones)==1:
                one(i,j,sqr,ones)
            elif len(ones)==4:
                sqr[0][0] = sqr[0][1] = sqr[1][0] = 0
                res.append(ones[:3])
                one(i,j,sqr, ones[3:])

    # for i in res:
    #     print(i)
    print(len(res))
    for a,b,c in res:
        x = [i+1 for i in a]
        y = [i+1 for i in b]
        z = [i+1 for i in c]
        print(*x, *y, *z)

