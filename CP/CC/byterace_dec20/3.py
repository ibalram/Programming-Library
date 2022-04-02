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

t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    a = [0]*(n+1)
    b = [0]*(n+1)
    for i in range(q):
        l,r = map(int,input().split())
        m = r-l+1
        l-=1
        r-=1
        sm = m*(m+1)//2
        a[l]+=1
        a[r+1]-=1+m
        b[l]+=1
        b[r+1]-=1
    sm = 0
    res = []
    for i in range(n):
        res.append(a[i]+sm)
        sm+=b[i]
    for i in range(1,n):
        res[i]+=res[i-1]
    print(*res)
