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

#kahn's algo
# lexicographically smallest topological sorting
#

from heapq import *
n,m =imap()
gr = defaultdict(list)
deg = [0]*n
for i in range(m):
    u,v = imap()
    u-=1
    v-=1
    gr[u].append(v)
    deg[v]+=1
q = []
for i in range(n):
    if deg[i]==0:
        q.append(i)
heapify(q)
order = []
cnt = 0
while q:
    s = heappop(q)
    order.append(s+1)
    for i in gr[s]:
        deg[i]-=1
        if deg[i]==0:
            heappush(q,i)
    cnt+=1

if cnt!=n:
    print(-1)
else:
    print(*order)
