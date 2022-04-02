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
    res = []
    cur = "()"*n
    res.append(cur)
    idx = 1
    for i in range(n-1):
        cur = cur[:idx]+cur[-2:2*n]+cur[idx:2*n-2]
        res.append(cur)
        idx+=1
    print(*res, sep="\n")
