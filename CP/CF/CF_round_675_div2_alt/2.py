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

for _ in range(int(input())):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    res = 0
    for i in range(n):
        for j in range(m):
            x = sorted([mat[i][~j],mat[~i][~j], mat[~i][j],mat[i][j]])[1]
            res+=abs(mat[i][~j]-x)
            # print(x)
            mat[i][~j] = x
            res+=abs(mat[~i][~j]-x)
            mat[~i][~j] = x
            res+=abs(mat[~i][j]-x)
            mat[~i][j] = x
            res+=+abs(mat[i][j]-x)
            mat[i][j] = x
            # print(res)
            # print(*mat,sep="\n", end="\n\n")
            # print([i,j],mat[i][j], [~i,~j], mat[~i][~j])
    print(res)

