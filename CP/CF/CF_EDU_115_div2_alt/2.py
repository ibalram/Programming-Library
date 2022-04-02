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
    mp = [set() for i in range(5)]
    res = 0
    for i in range(n):
        a = ilist()
        for j in range(5):
            if a[j]:
                mp[j].add(i)
    for i in range(5):
        for j in range(i+1,5):
            common = mp[i]&mp[j]
            a = mp[i]-common
            b = mp[j]-common
            if len(a)<=n//2 and len(b)<=n//2 and len(a)+len(b)+len(common)==n:
                res = 1
        if res:
            break
    print("YES" if res else "NO")
