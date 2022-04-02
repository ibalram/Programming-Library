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
sys.setrecursionlimit(10**6)
from functools import lru_cache
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = 0
    for i in range(n):
        for j in range(i,n):
            b = [k for k in a if i+1<=k<=j+1]
            if b==sorted(b):
                res+=1
    print(res)
