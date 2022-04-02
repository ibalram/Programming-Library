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

n = int(input())
a = ilist()
def rec(i,j):
    if i>=j:
        return a[i]
    mid = i+j>>1
    x = rec(i,mid)
    y = rec(mid+1,j)
    if i==0 and j==(1<<n)-1:
        mn = min(x,y)
        # print(x,y)
        print(a.index(mn)+1)
    return max(x,y)
rec(0,(1<<n)-1)
