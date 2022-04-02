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

n,k  = imap()
a = ilist()
mp = Counter(a[:k])
res = len(mp)
for i in range(k,n):
    mp[a[i-k]]-=1
    if mp[a[i-k]]==0:
        del mp[a[i-k]]
    mp[a[i]]+=1
    res = max(res, len(mp))
print(res)

