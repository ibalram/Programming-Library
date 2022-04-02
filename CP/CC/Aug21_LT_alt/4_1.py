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

from collections import deque, defaultdict, Counter
mod = int(1e9+7)
for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    a = list(map(int,input().split()))
    # a.sort()
    cnt = Counter(a)
    a = list(sorted(cnt.keys()))
    res = 0
    prod = 1
    pf = [0]*(n+1)
    pf[-1] = 1
    for i in range(len(a)):
        pf[i] = (pf[i-1] + cnt[a[i]])%mod
        res = (res+pf[i])%mod
        pf[i] = (pf[i]+pf[i-1])%mod
    print(pf)
    print(res)





