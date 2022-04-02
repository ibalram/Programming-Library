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

n,s =imap()
a = ilist()

sm = sum(a)-n*min(a)
if sm>=s:
    print(min(a))
else:
    rem = s-sm
    lvl = min(a)-(rem+n-1)//n
    if lvl<0:
        print(-1)
    else:
        print(lvl)
