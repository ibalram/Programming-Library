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


import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m =map(int,input().split())
    rows = []
    cols = []
    for i in range(n):
        rows.append(list(map(int,input().split())))
    for i in range(m):
        cols.append(list(map(int,input().split())))
    cccc = []
    for i in range(n):
        ls = 5005
        for j in range(m):
            ls = min(cols[j][i], ls)
        cccc.append([ls,i])
    rrrr = []
    for i in range(n):
        ls = min(rows[i])
        rrrr.append([ls,i])
    rrrr.sort()
    cccc.sort()
    # res = {}
    # for i in range(n):
    #     mp = [0]*(501)
    #     for j in range(m):
    #         mp[rows[i][j]]+=1
    #     for j in range(n):
    #         arr = [0]*(501)
    #         for k in range(m):
    #             arr[cols[k][j]]+=1
    #         if arr==mp:
    #             res[i] = j
    #             break
    # mat = [[] for i in range(n)]
    # # print(res)
    # for key in res.keys():
    #     mat[res[key]] = rows[key]

    mat = [[] for i in range(n)]
    for i in range(n):
        mat[cccc[i][1]] = rows[rrrr[i][1]]
    for i in mat:
        print(*i)
