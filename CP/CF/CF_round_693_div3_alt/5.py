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

from heapq import heapify, heappop, heappush
for _ in range(int(input())):
    mn = [float("inf")]*2
    mnId = 0
    mn2 = [float("inf")]*2
    mn2Id = 0
    n = int(input())
    a = []
    for i in range(n):
        h,w = map(int,input().split())
        a.append([h,w])
        if h<=mn[0] and w<=mn[1]:# or h<=mn2[0] and w<=mn2[1]:
            mnId = i
            mn =  [h,w]
        if h<=mn2[1] and w<=mn2[0]:# or h<=mn[1] and w<=mn[0]:
            mn2Id = i
            mn2 = [h,w]
    res = []
    def check(a,b):
        if b[0]<a[0] and b[1]<a[1]:
            return 1
        if b[1]<a[0] and b[0]<a[1]:
            return 1
        return 0
    print(mn)
    print(mn2)
    for i in range(n):
        if check(a[i], mn):
            res.append(mnId+1)
        elif check(a[i], mn2):
            res.append(mn2Id+1)
        else:
            res.append(-1)
    print(*res)
    # a.sort(reverse=True)
    # for i in range(n):
    # mx = float("inf")
    # idx = 0
    # res = [-2]*(n)
    # print(*res)


