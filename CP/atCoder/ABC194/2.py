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

n = int(input())
a = []
b = []
for i in range(n):
    x,y = imap()
    a.append(x)
    b.append(y)
res = int(10**18)
for i in range(n):
    for j in range(n):
        if i!=j:
            res = min(res, max(a[i],b[j]))
        else:
            res = min(res, a[i]+b[j])
print(res)
