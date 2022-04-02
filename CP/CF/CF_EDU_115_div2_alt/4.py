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
    mp1 = defaultdict(int)
    mp2 = defaultdict(int)
    a,b = [0]*n, [0]*n
    # mp12 = defaultdict(set)
    for i in range(n):
        a[i],b[i] = imap()
        mp1[a[i]]+=1
        mp2[b[i]]+=1
        # mp1[a[i]].add(i)
        # mp2[b[i]].add(i)
    res = n*(n-1)*(n-2)//6
    for i in range(n):
        res-=(mp1[a[i]]-1)*(mp2[b[i]]-1)
    print(res)
