

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


from heapq import heapify, heappop as pp, heappush as pus

nei = [(1,0),(-1,0),(0,1),(0,-1)]


for _ in range(1,int(input())+1):
    res = None
    r,c = imap()
    mat = []
    for i in range(r):
        row = ilist()
        mat.append(row)
    res = 0
    heap = [(-mat[i][j], i,j) for j in range(c) for i in range(r)]
    heapify(heap)
    while heap:
        x,i,j = pp(heap)
        x = -x
        f = 0
        mx = -float("inf")
        for dx,dy in nei:
            ii = i+dx
            jj = j+dy
            if 0<=ii<r and 0<=jj<c:
                # mx = max(mx,mat[ii][jj])
                st
        # if mx>mat[i][j]+1:
        #     res+=mx-mat[i][j]-1
        #     mat[i][j] = mx-1
    # mark = [[0]*c for i in range(r)]
    # done = [a[:] for a in mat]
    # while True:
    #     vis = [[0]*c for i in range(r)]
    #     arr =
    #     try:mx = [mat[i][j] for j in range(c) for i in range(r) if mark[i][j]==0]
    #     except:break
    #     heap = [(-mx, i,j) for j in range(c) for i in range(r) if mat[i][j]==mx]
    #     heapify(heap)

    #     while heap:
    #         x,i,j = pp(heap)
    #         if mark[i][j]: continue
    #         x = -x
    #         done[i][j] = x
    #         mark[i][j] = 1
    #         mx = -float("inf")
    #         for dx,dy in nei:
    #             ii = i+dx
    #             jj = j+dy
    #             if 0<=ii<r and 0<=jj<c:
    #                 # mx = max(mx,mat[ii][jj])
    #                 if x-mat[i][j]<=1:
    #                     vis[ii][jj]
    #                     pus(heap, (-mat[i][j],ii,jj))
    #         if mx>mat[i][j]+1:
    #             res+=mx-mat[i][j]-1
    #             mat[i][j] = mx-1

    # res = 0
    # while True:
    #     # try:mx = max()
    #     mx =-float("inf")
    #     aa = [done[i][j] for j in range(c) for i in range(r) if mark[i][j]==0]
    #     if not aa:
    #         break
    #     mx = max(aa)
    #     for i in range(r):
    #         for j in range(c):
    #             if done[i][j]==mx:
    #                 mark[i][j] = 1
    #                 for dx,dy in nei:
    #                     ii = i+dx
    #                     jj = j+dy
    #                     if 0<=ii<r and 0<=jj<c and done[ii][jj]<mx:
    #                         done[ii][jj] = mx-1
    res = 0
    for i in range(r):
        for j in range(c):
            res+=done[i][j]-mat[i][j]


    # heap = [(-mat[i][j], i,j) for j in range(c) for i in range(r)]
    # heapify(heap)
    # res = 0
    # # print(heap)
    # while heap:
    #     x,i,j = pp(heap)
    #     x = -x
    #     f = 0
    #     mx = -float("inf")
    #     for dx,dy in nei:
    #         ii = i+dx
    #         jj = j+dy
    #         if 0<=ii<r and 0<=jj<c:
    #             mx = max(mx,mat[ii][jj])
    #     if mx>mat[i][j]+1:
    #         res+=mx-mat[i][j]-1
    #         mat[i][j] = mx-1

    print("Case #{}:".format(_),res)

