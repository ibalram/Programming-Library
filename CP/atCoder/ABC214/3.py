# https://atcoder.jp/contests/abc214/tasks/abc214_c
# https://atcoder.jp/contests/abc214/submissions/25034404



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

from heapq import *
n = int(input())
s = ilist()
t = ilist()
a = list(range(n))
heap = [(t[i],i) for i in range(n)]
heapify(heap)
res = [0]*n
cnt = 0
while cnt<n:
    time, idx = heappop(heap)
    if res[idx]==0:
        res[idx]=time
        cnt+=1
    heappush(heap, (time+s[idx], (idx+1)%n))
print(*res, sep="\n")

