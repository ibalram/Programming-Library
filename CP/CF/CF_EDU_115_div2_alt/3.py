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

for _ in range(int(input())):
    n = int(input())
    a = ilist()
    sm = sum(a)
    c = 2*sm/n
    mp = defaultdict(int)
    res = 0
    for i in a:
        if c-i in mp:
            res += mp[c-i]
        mp[i]+=1
    print(res)
# x+a+b//n+2 = x//n
# (a+b) = 2sm//n
