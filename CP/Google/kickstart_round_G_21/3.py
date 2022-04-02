import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)

def solve(n,k,b):
    a = []
    for i in range(n):
        sm = 0
        for j in range(i,n):
            sm+=b[j]
            a.append((i,j,sm))
    a.sort()
    res = float("inf")
    for i in range(len(a)):
        x,y,sm = a[i]
        if sm==k:
            res = min(res,y-x+1)
            continue
        for j in range(i+1,len(a)):
            xx,yy,ssm = a[j]
            if xx<=y:continue
            if ssm+sm==k:
                res = min(res, y-x+1+yy-xx+1)
    return res if res<float("inf") else -1





for _test in range(int(input())):
    res = 0
    n,k = imap()
    b = ilist()
    res = solve(n,k,b)

    print('Case #{}:'.format(_test+1), res)
