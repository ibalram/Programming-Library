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

n,m,q = imap()
bags = []
for i in range(n):
    w,v = imap()
    bags.append((w,v))
x = ilist()
bags.sort()
for _ in range(q):
    l,r = imap()
    l-=1
    r-=1
    boxes = sorted(x[:l]+x[r+1:])
    mark = [0]*(n)
    res = 0
    for bx in boxes:
        mnVal = -float("inf")
        mnValIdx = -1
        for j in range(n):
            if bx>=bags[j][0] and mnVal<bags[j][1] and not mark[j]:
                mnValIdx = j
                mnVal = bags[j][1]
        if mnValIdx!=-1:
            mark[mnValIdx]=1
            res+=mnVal
    print(res)

