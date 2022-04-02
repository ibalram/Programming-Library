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
from math import ceil
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    idx = ceil(n/2)-1
    other = n-idx
    idx = idx*k
    # print(idx)
    res = 0
    x = []
    while idx<n*k:
        x.append(a[idx])
        res+=a[idx]
        idx+=other
    # print(n,k,other,x)
    print(res)

