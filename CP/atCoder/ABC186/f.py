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


n,m,k = imap()
mpR = defaultdict(int)
mpC = defaultdict(int)
for i in range(k):
    x,y = imap()
    mpR[x].append(y)
    mpC[y].append(x)
for i in range(n):
    mp[i].sort()
def rec(i, j, rem):
    if rem<=0:
        return 0
    res = 0
    cnt = 0
    for k in (i+1, n):
        if moves[]

