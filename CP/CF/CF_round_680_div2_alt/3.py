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
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = float("inf")
    c = [[i,j] for i,j in zip(a,b)]
    c.sort()
    # print(c)
    for i in range(1,n):
        c[i][1]+=c[i-1][1]
    # print(c)
    res = c[n-1][1]
    for i in range(n):
        # print(c[i])
        res = min(res, max(c[i][0],c[n-1][1]-c[i][1]))
    print(res)
