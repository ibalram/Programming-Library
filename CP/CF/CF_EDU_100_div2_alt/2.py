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


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sm0 = sum(a[i] if i%2==0 else 0 for i in range(n))
    sm1 = sum(a[i] if i%2 else 0 for i in range(n))
    b = []
    if sm0>sm1:
        for i in range(n):
            if i%2==0: b.append(a[i])
            else: b.append(1)
    else:
        for i in range(n):
            if i%2: b.append(a[i])
            else: b.append(1)
    print(*b)

