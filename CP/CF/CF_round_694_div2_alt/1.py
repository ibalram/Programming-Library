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
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    mn = 0
    for i in range(n):
        mn+=a[i]//x
        a[i] %=x
    # print(a)
    print(mn+(sum(a)+x-1)//x, mn+sum((1 if i>0 else 0) for i in a))
