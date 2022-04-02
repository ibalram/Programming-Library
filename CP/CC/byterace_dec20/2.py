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
    n,k = map(int,input().split())
    a = []
    for i in range(26):
        if (k>>i)&1:
            a.append(-i)
    # print(n,a)
    # if n>k:
    #     print(-1)
    #     continue
    # print(n,a)
    heapify(a)
    while len(a)<n:
        x = -heappop(a)
        if x==0:
            break
        y = x-1
        heappush(a, -y)
        heappush(a, -y)
    if len(a)!=n:
        print(-1); continue
    res = []
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        res.append(s[-i])
    print("".join(res))





