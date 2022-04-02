import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6+10)
mod = int(1e9+7)

n,m = imap()
a = ilist()
b = ilist()

@lru_cache(None)
def rec(i,j):
    if i>=n and j>=m:
        return 0
    if i>=n or j>=m:
        if j>=m:
            return n-i
        if i>=n:
            return m-j
    res = min(1+ rec(i+1,j), 1+rec(i,j+1))
    if a[i]==b[j]:
        res = min(res, rec(i+1,j+1))
    else: res = min(res, 1+rec(i+1,j+1))
    return res
print(rec(0,0))
