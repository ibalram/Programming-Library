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

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mp = Counter(a)
    tot = n
    res = 0
    for i in mp:
        res+= mp[i]*(tot-mp[i])
        tot-=mp[i]
    print(2*res)
