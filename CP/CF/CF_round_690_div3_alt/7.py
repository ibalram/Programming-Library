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

from bisect import bisect_right
for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    l = [a[i][0] for i in range(n)]
    r = [a[i][1] for i in range(n)]
    l.sort()
    r.sort()
    res = float("inf")
    for i in range(n):
        lIdx = bisect_right(r,a[i][0]-1)
        rIdx = bisect_right(l,a[i][1])
        res = min(res, n-rIdx + lIdx)
    print(res)


