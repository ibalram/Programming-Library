import os, sys, bisect
from heapq import heapify, heappop, heappush
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)

mod = int(1e9+7)

for _test in range(int(input())):
    res = 0
    n,d,c,m = imap()
    s = input().strip()
    res = "YES"
    for i in range(n):
        if s[i]=="D" and d:
            d-=1
            c+=m
        elif s[i]=="C" and c:
            c-=1
        else:
            if "D" in s[i+1:]:
                res = "NO"
            break
    print('Case #{}:'.format(_test+1), res)
