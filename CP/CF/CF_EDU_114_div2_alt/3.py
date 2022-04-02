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


import sys
input = sys.stdin.readline
import bisect
n =int(input())
a = list(map(int,input().split()))
a.sort()
sm = sum(a)
m = int(input())
b = []
ans = [0]*m
for i in range(m):
    x,y = map(int,input().split())
    idx = bisect.bisect_left(a,x)
    if idx>=n:
        idx-=1
    res = max(0, x-a[idx])
    rem = sm-a[idx]
    res += max(0, y-rem)
    if idx>0:
        idx-=1
        cur = max(0, x-a[idx])
        rem = sm-a[idx]
        cur += max(0, y-rem)
        res =min(res,cur)
    ans[i] = str(res)
print("\n".join(ans))


