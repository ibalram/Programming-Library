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

n,m = imap()
a = [0]*(m)
b = [0]*(m)
c = [0]*(m)
edges = []
for i in range(m):
    a[i],b[i],c[i] = imap()
    edges.append(i)
edges.sort(key=lambda x: c[x])

par = [i for i in range(n+1)]
def find(a):
    if par[a]==a:
        return a
    x = a
    while par[x] !=x:
        x = par[x]
    par[a] = x
    return par[a]
def union(a,b):
    a = find(a)
    b = find(b)
    par[a] = b

res = 0
for i in edges:
    C,A,B = c[i],a[i],b[i]
    x = find(A)
    y = find(B)
    if x==y:
        res += max(0,C)
    else:
        union(x,y)
print(res)
