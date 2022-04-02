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
    n,c0,c1,h = map(int,input().split())
    a = list(map(int,input().strip()))
    # print(a)
    cnt0 = a.count(0)
    cnt1 = a.count(1)
    if c0<c1:
        print(c0*cnt0 +min(c1*cnt1,min(h+c0, c1)*cnt1))
    else:
        print(c1*cnt1 +min(c0*cnt0,min(h+c1, c0)*cnt0))
