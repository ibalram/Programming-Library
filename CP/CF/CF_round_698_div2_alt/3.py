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

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    from collections import Counter
    n = int(input())
    d = list(map(int,input().split()))
    d.sort(reverse=True)
    x = Counter(d)
    f = 1
    for i in x.values():
        if i!=2:
            f = 0
            break
    if f==0:
        print("NO")
        continue
    ad = 0
    for i in range(n):
        if (d[2*i]-2*ad)%(2*n-2*i):
            f = 0
            break
        div = (d[2*i]-2*ad)//(2*n-2*i)
        if div<=0:
            f = 0
            break
        ad+=div
    print("YES" if f else "NO")
