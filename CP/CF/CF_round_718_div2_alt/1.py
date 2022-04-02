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

x = 2050

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    y = x

    while y<n:
        y*=10
    while y>=2050:
        cnt+=n//y
        n%=y
        y//=10

    if n>0:
        print(-1)
    else:
        print(cnt)
