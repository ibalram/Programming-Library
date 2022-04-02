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

n,q = imap()
clss = [0]+ilist()

par = [i for i in range(n+1)]
sz = [1]*(n+1)
cnt = [[]]
for i in range(1,n+1):
    cnt.append({clss[i]:1})

def find(x):
    if par[x]==x: return par[x]
    par[x] = find(par[x])
    return par[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x==y: return
    if sz[x]<sz[y]: x,y = y,x
    sz[x]+=sz[y]
    par[y] = x
    # print(cnt,y)
    for i,val in cnt[y].items():
        if i in cnt[x]:
            # res += cnt[x][i]*val
            cnt[x][i]+=val
        else:
            cnt[x][i] = val
def check(x,y):
    x = find(x)
    return cnt[x][y] if y in cnt[x] else 0

for i in range(q):
    typ,x,y = imap()
    if typ==1:
        union(x,y)
    else:
        print(check(x,y))
