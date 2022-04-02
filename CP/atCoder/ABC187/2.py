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
x = []
y = []
for i in range(n):
    a,b = imap()
    x.append(a)
    y.append(b)
res = 0
for i in range(n):
    for j in range(i+1,n):
        if abs((y[i]-y[j])/(x[i]-x[j]))<=1:
            res+=1
print(res)
