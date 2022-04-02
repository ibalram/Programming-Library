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
g = defaultdict(list)
p = list(map(int,input().split()))
a = [0]+list(map(int,input().split()))
q = p[::-1]
for i in range(2,n+1):
    g[q.pop()].append(i)
sz = [0]*(n+1)
def dfs(s,par):
    sz[s] = a[s]
    for i in g[s]:
        if i != par:
            dfs(i,s)
            sz[s]+=sz[i]
dfs(1,0)
print(sz[1:])
