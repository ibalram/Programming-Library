

from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
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

n = int(input())
mat = []
for i in range(n):
    mat.append(ilist())
f = 0
for i in range(1,n):
    diff = mat[i][0]-mat[i-1][0]
    for j in range(1,n):
        if mat[i][j]-mat[i-1][j]!=diff:
            f = 1
            break
if f:
    print("No")
    exit()

mini = -1
val0 = float("inf")
for i in range(n):
    if mat[i][0]<val0:
        mini = i
        val0 = mat[i][0]
b = mat[mini]
a = []
for i in range(n):
    diff = abs(mat[i][0]-b[0])
    a.append(diff)
print("Yes")
print(*a)
print(*b)


