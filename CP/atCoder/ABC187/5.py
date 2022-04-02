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
par = {i:i for i in range(n+1)}
edges = []
for i in range(n-1):
    x,y = imap()
    edges.append([x,y])
    gr[x].append(y)
    gr[y].append(x)

def dfs(s,parent):
    stack = [s]
    while stack:
        s = stack.pop()
        for i in gr[s]:
            if i==1 or par[i]!=i: continue
            par[i] = s
            stack.append(i)
dfs(1,-1)

q = int(input())
c = [0]*(n+1)
for _ in range(q):
    t,e,x = imap()
    a,b = edges[e-1]
    if t==1:
        if par[a]==b:
            c[a]+=x
        else:
            c[1]+=x
            c[b]-=x
    else:
        if par[b]==a:
            c[b]+=x
        else:
            c[1]+=x
            c[a]-=x
def rec(s,parent):
    stack = [s]
    while stack:
        s = stack.pop()
        for i in gr[s]:
            if par[s]==i: continue
            c[i]+=c[s]
            stack.append(i)
rec(1,-1)
res = [str(c[i]) for i in range(1,n+1)]
print("\n".join(res))
