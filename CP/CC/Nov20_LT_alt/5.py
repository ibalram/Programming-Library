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
from math import gcd
res = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        num = i*(j+1)
        den = j*(i+1)
        gc = gcd(num,den)
        a = num/gc
        b = den/gc
        res+=a+1==b
print(res)
