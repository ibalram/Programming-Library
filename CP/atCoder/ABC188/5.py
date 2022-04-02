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

n,m = imap()
A = [0]+ilist()
gr = defaultdict(list)
deg =[0]*(n+1)
for i in range(m):
    x,y = imap()
    gr[x].append(y)
    deg[y]+=1
vis = {}
res = -float("inf")

subMax = [0]*(n+1)
def rec(s, mn):
    global res
    if s in vis:
        res = max(res, subMax[s]-mn)
        return subMax[s]
    vis[s] = 1
    mx = -float("inf")
    for i in gr[s]:
        res = max(res, A[i]-mn)
        mx = max(mx,A[i],rec(i, min(A[i],mn)))
    subMax[s] = mx
    return mx

for i in range(1,n+1):
    if deg[i]==0:
        rec(i,A[i])
print(res)
