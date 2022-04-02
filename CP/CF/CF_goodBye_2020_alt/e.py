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


import os, sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    w = list(map(int,input().split()))
    gr = defaultdict(list)
    for i in range(n-1):
        x,y = map(int,input().split())
        gr[x].append(y)
        gr[y].append(x)
    a = []
    for i in range(1,n+1):
        if len(gr[i])>=2:
            a.append([w[i-1],len(gr[i])-1])
    res = []
    tot = sum(w)
    a.sort()
    sm = 0
    # print(a)
    for i in range(1,n):
        res.append(tot+sm)
        if a:
            # val,cnt=a.pop()
            sm+=a[-1][0]
            a[-1][1]-=1
            if a[-1][1]==0:
                a.pop()
    print(*res)
