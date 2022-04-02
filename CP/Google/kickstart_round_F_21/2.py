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
    d,n,k = imap()
    h,s,e = [0]*n,[0]*n,[0]*n
    # mp = [0]*(d+1)
    # for i in range(n):
    #     h[i],s[i],e[i] = imap()
    #     mp[s[i]-1]+=h[i]
    #     mp[e[i]]-=h[i]
    # print(mp)
    # for i in range(1,d+1):
    #     mp[i]+=mp[i-1]
    # res = max(mp)
    # print(mp)
    mp = [[] for i in range(d)]
    for i in range(n):
        h,s,e = imap()
        for j in range(s-1,e):
            heappush(mp[j], h)
            if len(mp[j])>k:
                heappop(mp[j])
    res = 0
    for i in mp:
        res = max(res, sum(i))
    print('Case #{}:'.format(_test+1), res)
