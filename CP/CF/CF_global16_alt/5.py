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

for _ in range(int(input())):
    n,m = map(int,input().split())
    tot = n*m
    a = list(map(int,input().split()))
    l = list(range(tot))
    l.sort(key = lambda x: (a[x],x))
    mat = []
    for i in range(n):
        mat.append(l[m*i:m*(i+1)])
    for i in range(n):
        mat[i].sort(key=lambda x: (a[x],-x))
    res = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            for k in range(j):
                cnt+=mat[i][k]<mat[i][j]
        res+=cnt
    print(res)

    # mat = []
    # for i in range(n):
    #     mat.append(l[m*i:m*(i+1)])
    #     print(*(k+1 for k in l[m*i:m*(i+1)]))
    # print(*l)
    # res = 0
    # for i in range(tot):
    #     cnt = 0
    #     for j in range(i):
    #         cnt+=l[j]<l[i]
    #     res+=cnt
    # print(res)
