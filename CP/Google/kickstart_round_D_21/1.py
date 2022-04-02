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
    x = ilist()
    y = ilist()
    z = ilist()
    diffs = Counter([(x[0]+z[2])/2, (x[1]+z[1])/2, (x[2]+z[0])/2, (y[0]+y[1])/2])
    res = 0
    for i in diffs.keys():
        if int(i)==i:
            res = max(res, diffs[i])
    res+= 2*x[1]==x[0]+x[2]
    res+= 2*y[1]==x[2]+z[2]
    res+= 2*z[1]==z[0]+z[2]
    res+= 2*y[0]==x[0]+z[0]
    # print(diffs)

    print('Case #{}:'.format(_test+1), res)
