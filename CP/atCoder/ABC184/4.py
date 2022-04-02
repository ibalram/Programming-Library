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

a,b,c = imap()


@lru_cache(None)
def rec(x,y,z, cnt):
    if 100 in (x,y,z):
        return cnt
    tot = x+y+z
    return (x/tot)*rec(x+1, y,z, cnt+1)+(y/tot)*rec(x, y+1,z, cnt+1)+(z/tot)*rec(x, y,z+1, cnt+1)
print(rec(a,b,c,0))
