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
    n,x,y = map(int,input().split())
    # if n==2:
    #     print(x,y)
    # else:
    maxn = y-x
    res = []
    sm = float("inf")
    for i in range(1,51):
        # if maxn%i:continue
        for k in range(1,51):
            # if k+i*(n-1)<y:continue
            tmp = []
            cnt = k
            tmp = [k+i*j for j in range(n)]
            if x not in tmp or y not in tmp:continue
            nsm = sum(tmp)
            if nsm<sm:
                res = tmp[:]
                sm = nsm
    print(*res)
