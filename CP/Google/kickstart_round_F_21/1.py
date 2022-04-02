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

for _test in range(int(input())):
    res = 0
    n = int(input())

    s = list(map(int,list(input())))
    a = []
    for i in range(n):
        if s[i]:
            a.append(i)
    res = 0
    for i in range(n):
        idx = bisect.bisect_right(a,i)
        cur = float("inf")
        if idx<len(a):
            cur = min(cur, abs(a[idx]-i))
        if idx>0:
            cur = min(cur, abs(a[idx-1]-i))
        res+=cur



    print('Case #{}:'.format(_test+1), res)
