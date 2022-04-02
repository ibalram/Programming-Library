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
    n = int(input())
    a = list(map(int,input().split()))
    gas = a[0]
    if not gas: print(0); continue
    f = 0
    for i in range(1,n):
        gas-=1
        if gas<0:
            break
        gas+=a[i]
        if i==n-1:
            f = 1
    if f:
        print(i+max(gas,0))
    else:
        print(i-1)
