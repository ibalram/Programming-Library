import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(2*10**6)
# mod = int(1e9+7)

mod = 998244353

n,m,k = imap()
a = ilist()
gr = defaultdict(list)
for i in range(n-1):
    u,v = imap()
    gr[u].append([v,i])
    gr[v].append([u,i])
freq = [0]*(n-1)
def bfs(s,v):
    if v==-1:
        return
    q = deque([s])
    par = {s:s}
    vis = set([s])
    while q:
        s = q.popleft()
        if s==v:
            break
        for i in gr[s]:
            if i in vis: continue
            par[i] =s
            vis.add(i)
            q.append(i)
    while par[v]!=v:
        freq[(min(v,par[v]),max(v,par[v]))]+=1
        v = par[v]

def dfs(s,v,par):
    if s==v:
        return 1
    for i,idx in gr[s]:
        if i==par: continue
        if dfs(i,v,s):
            freq[idx]+=1
            return 1
    return 0


for u,v in zip(a,a[1:]):
    # bfs(u,v)
    dfs(u,v,-1)
tot = sum(freq)
m = n-1
@lru_cache(None)
def rec(i,red):
    if i>=m: return 1*(2*red-tot==k)
    return (rec(i+1,red)%mod+rec(i+1,red+freq[i])%mod)%mod
print(rec(0,0)%mod)
