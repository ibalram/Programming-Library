# https://atcoder.jp/contests/abc213/tasks/abc213_c
# https://atcoder.jp/contests/abc213/submissions/24868068

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

h,w,n = imap()
col = set()
row = set()
a = []
for i in range(n):
    x,y = imap()
    a.append((x,y))
    row.add(x)
    col.add(y)
col = list(sorted(col))
row = list(sorted(row))
mCol = defaultdict(int)
mRow = defaultdict(int)
for i,v in enumerate(col):
    mCol[v] = i+1
for i,v in enumerate(row):
    mRow[v] = i+1

for u,v in a:
    print(mRow[u], mCol[v])
