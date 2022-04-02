

from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
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


for _ in range(1,int(input())+1):
    res = None
    r,c = imap()
    mat = []
    for i in range(r):
        row = ilist()
        mat.append(row)
    down = [a[:] for a in mat]
    right = [a[:] for a in mat]
    up = [a[:] for a in mat[::-1]]
    left = [a[::-1] for a in mat]
    for i in range(1,r):
        for j in range(c):
            if down[i][j]:
                down[i][j]+=down[i-1][j]
            if up[i][j]:
                up[i][j]+=up[i-1][j]
    up = [a[:] for a in up[::-1]]
    for i in range(1,c):
        for j in range(r):
            if right[j][i]:
                right[j][i]+=right[j][i-1]
            if left[j][i]:
                left[j][i]+=left[j][i-1]
    left = [a[::-1] for a in left]
    def bs(x,y):
        l = 0
        r = x+1
        while r-l>1:
            mid = l+r>>1
            if 2*mid<=y:
                l = mid
            else:
                r = mid
        return l

    res = 0
    def calc(x,y):
        ans = 0
        if x>=2 and y>=2:
            ans+=bs(x,y)+bs(y,x)-2
        return ans
    for i in range(r):
        for j in range(c):
            # print(down[i][j],right[i][j], up[i][j],left[i][j], end=", ")

            res+= calc(down[i][j],right[i][j])
            res+= calc(down[i][j],left[i][j])
            res+= calc(up[i][j],left[i][j])
            res+= calc(up[i][j],right[i][j])
        # print()

    # print(res)
    # column = [a[:] for a in mat]
    # row = [a[:] for a in mat]
    # for i in range(1,r):
    #     for j in range(c):
    #         column[i][j]+=column[i-1][j]
    # for i in range(1,c):
    #     for j in range(r):
    #         row[j][i]+=row[j][i-1]
    # rMap = defaultdict(dict)
    # cMap = defaultdict(dict)
    # print(*column,sep="\n")
    # print(*row,sep="\n")
    # for i in range(r):
    #     for j in range(c):
    #         if column[i][j]>=2:
    #             cMap[column[i][j]][(i,j-column[i][j]-1)] = 1
    #             cMap[column[i][j]][(i,j)] = 1
    #         if row[i][j]>=2:
    #             rMap[row[i][j]][(i-row[i][j]-1,j)] = 1
    #             rMap[row[i][j]][(i,j)] = 1
    # res = 0
    # print(rMap)
    # print(cMap)
    # for i in rMap:
    #     for j in rMap[i]:
    #         for k in range(2*i, )
    #         if j in cMap[2*i]:
    #             res+=1
    print("Case #{}:".format(_),res)

