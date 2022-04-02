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
    s = input().strip()
    p = input().strip()
    m = len(s)
    n = len(p)
    j = 0
    i = 0
    while j < m and i < n:
        if s[j] == p[i]:
            j = j+1
        i = i + 1
    res = n-m if j == m else "IMPOSSIBLE"
    print('Case #{}:'.format(_test+1), res)
