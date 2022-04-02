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
a = ilist()

par = {i:i for i in set(a)}
sz = {i: 1 for i in set(a)}
def find(x):
    if par[x]==x:
        return par[x]
    par[x] = find(par[x])
    return par[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return False
    if sz[y]>sz[x]:
        x,y = y,x
    par[y] = par[x]
    sz[x] += sz[y]
    return True

for i in range(n//2):
    union(a[i],a[~i])

res = 0
for i in set(a):
    if par[i]==i:
        res+=sz[i]-1

# print(sz)
print(res)
