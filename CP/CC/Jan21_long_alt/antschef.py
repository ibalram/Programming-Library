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

from heapq import heapify, heappop, heappush
for _ in range(int(input())):
    n = int(input())
    res = 0
    lines = []
    mp = defaultdict(int)
    for i in range(n):
        a = list(map(int,input().split()))
        m = a[0]
        a = a[1:]
        # cnt = sum(1*(j<0) for j in a)
        # res+= cnt*(m-cnt)
        lines.append(a)
        for j in a:
            if mp[abs(j)]==i:
                mp[abs(j)]+=1
    for i in range(n):
        a,b = [],[]
        for j in lines[i]:
            if j<0:
                a.append(-j)
            else:
                b.append(j)
        heapify(a)
        heapify(b)
        while a and b:
            if a[0]<b[0]:
                x = heappop(a)
                if mp[x]>1: res+=len(a)
                else: res+=len(b)
            else:
                x = heappop(b)
                if mp[x]>1: res+=len(b)
                else: res+=len(a)
        while a:
            x = heappop(a)
            if mp[x]>1: res+=len(a)
        while b:
            x = heappop(b)
            if mp[x]>1: res+=len(b)
        for i in mp.values():
            if i>1: res+=1
    print(res)

    # print(res)
