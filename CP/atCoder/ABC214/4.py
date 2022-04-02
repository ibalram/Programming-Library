# https://atcoder.jp/contests/abc214/tasks/abc214_d
# https://atcoder.jp/contests/abc214/submissions/25045972


import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**4)
mod = int(1e9+7)

n = int(input())
g = defaultdict(list)
edges = []
for i in range(n-1):
    u,v,w = imap()
    # g[u].append((v,w))
    # g[v].append((u,w))
    edges.append((w,(u,v)))
size = [1]*(n+1)
par = {i:i for i in range(n+1)}
def find(a):
    if par[a]==a: return par[a]
    par[a] = find(par[a])
    return par[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b: return
    if size[a]<size[b]: a,b = b,a
    size[a]+=size[b]
    par[b] = a
res = 0
edges.sort()
for w,(u,v) in edges:
    u = find(u)
    v = find(v)
    res+=w*size[u]*size[v]
    union(u,v)
print(res)
