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
    a, b = imap()
    for i in range(a,b+1):
        ls = list(map(int, list(str(i))))
        prod = 1
        for x in ls: prod*=x
        sm = sum(ls)
        if prod%sm==0:
            res+=1

    print('Case #{}:'.format(_test+1), res)
