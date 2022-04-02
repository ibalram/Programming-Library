from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
# sys.setrecursionlimit(10**6)
#------------------------------------------------------------------

n,m= mapi()
mat = []
for i in range(n):
    x = list(input().strip())
    mat.append(x)
cnt = 0
for i in range(n):
    for j in range(m):
        if mat[i][j]==".":
            if i+1<n and mat[i+1][j]==".":
                cnt+=1
            if j+1<m and mat[i][j+1]==".":
                cnt+=1
print(cnt)
