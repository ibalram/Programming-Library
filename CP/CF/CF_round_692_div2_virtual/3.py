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
    n,m = map(int,input().split())
    par = [i for i in range(n+1)]
    def find(x):
        if par[x]==x:return x
        par[x] = find(par[x])
        return par[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x==y: return 1
        par[x] = y
        return 0
    res = 0
    for i in range(m):
        x,y = map(int,input().split())
        if x==y: continue
        res+=1+union(x,y)
    print(res)
