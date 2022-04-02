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

pal = []
from bisect import *
def rev(n):
    res = 0
    while n:
        res = res<<1
        res = res|(n&1)
        n = n>>1
    return res
for i in range(2<<17):
    pal.append((i<<(i.bit_length())) + rev(i))
    pal.append(((i>>1)<<(i.bit_length())) + rev(i))
pal = sorted(set(pal))
print(max(pal))
for _ in range(int(input())):
    n = int(input())
    idx = bisect_left(pal,n)
    if idx>=len(pal):
        idx-=1
    res = abs(n-pal[idx])
    if idx-1>=0:
        res = min(res, abs(n-pal[idx-1]))
    if idx+1<len(pal):
        res = min(res, abs(n-pal[idx+1]))
    print(res)
