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


import os, sys, bisect
for _ in range(int(input())):
    n,x = map(int,input().split())
    res = 0
    for i in range(1,int(x**.5)+1):
        if x%i==0:
            res+=x//i<=n
    print("Yes" if res else "No")
