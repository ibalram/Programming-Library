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


a = list(map(int,list(input())))

n = len(a)

@lru_cache(None)
def rec(idx, sm):
    if idx>=n:
        return 0 if sm==0 else -float("inf")
    return max(1+rec(idx+1, (sm+a[idx])%3), rec(idx+1, sm))
mx = rec(0,0)
print(n-mx if mx>0 else -1)
