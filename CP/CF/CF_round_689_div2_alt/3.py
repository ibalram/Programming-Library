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
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    qe = []
    for i in range(m):
        qe.append(list(map(float,input().split())))
    b = sorted(a)
    if a==b:
        print(1.0)
        continue
    r = n-1
    while r>=0 and a[r]==b[r]: r-=1
    yes = 1
    no = 0
    qe.sort(reverse =True)
    pre = 0
    cur = 0
    for i,p in qe:
        if i-1<r: break
        cur += (i-1>=r)*p*(1-pre) #+ (i-1>=r) * p
        # print(_,i,p,"'",cur)
        pre = cur
    print("{:.7f}".format(cur))


