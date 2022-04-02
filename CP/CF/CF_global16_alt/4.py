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
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(range(m))
    l.sort(key = lambda x: (a[x],-x))
    # print(*l)
    res = 0
    for i in range(m):
        cnt = 0
        for j in range(i):
            cnt+=l[j]<l[i]
        res+=cnt
    print(res)
