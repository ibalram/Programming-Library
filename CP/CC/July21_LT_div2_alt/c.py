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



from bisect import *
for _ in range(int(input())):
    n,k,s = map(int,input().split())
    a = list(map(int,input().split()))
    sm = s*k
    b = []
    prev = 0
    for i in range(n):
        if a[i]>s:
            # b.append(i)
            if prev<i:
                b.append(a[prev:i])
            prev = i+1
    if prev<i:
        b.append(a[prev:i])
    m = len(b)
    res = 0
    for a in b:
        n = len(a)
        pf = [0]+a[:]
        # print(a)
        for i in range(1,n+1):
            pf[i]+=pf[i-1]
        for i in range(n+1):
            idx = bisect_right(pf,pf[i]+sm)
            idx-=1
            res = max(res, idx-i)
    print(res)

