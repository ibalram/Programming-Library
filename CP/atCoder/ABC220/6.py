import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

n = int(input())
gr = defaultdict(list)
for i in range(n-1):
    x,y = imap()
    gr[x].append(y)
    gr[y].append(x)

par = [i for i in range(n+1)]
def dfs(s,pr):
    for i in gr[s]:
        if s==pr:
            continue
        par[i] = s
        dfs(i,s)

