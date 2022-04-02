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

n = int(input())

l = 0
r = n+1

def check(x):
    return x*(x+1)//2
while r-l>=0:
    mid = l+r>>1
    if check(mid)<=n+1:
        l = mid+1
    else:
        r = mid-1
# print(l-1)
print(n-l+1+1)
