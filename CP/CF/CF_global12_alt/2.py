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
    n,k = map(int,input().split())
    a = []
    for i in range(n):
        x,y =map(int,input().split())
        a.append([x,y])
    # mp = defaultdict(list)
    dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
    f = -1
    for i in range(n):
        cent = a[i][:]
        cnt = 0
        for j in range(n):
            if i==j: continue
            cnt+=dist(a[i],a[j])<=k
        if cnt==n-1:
            f = 1
    print(f)
