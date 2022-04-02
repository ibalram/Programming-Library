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

r,x,y = imap()
dist = (x**2+y**2)**.5
# print(dist)
div = int(dist/r)
# print(dist)
rem = dist-div*r #dist%r
res = div
if rem and div:
    res+=1
elif rem:
    res = 2
print(res)
