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


import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from functools import lru_cache
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a[:] #[0]*n
    res = 0
    for i in range(n):
        # res+=max(0, a[i]-b[i]-1)
        res+=b[i]-1
        b[i] = min(b[i],n*2+10)
        while b[i]>1:
            for j in range(i,n,b[i]):
                b[j] = max(1, b[j]-1)
        # for j in range(min(n-1,i+b[i]), i+1,-1):
        #     # b[j]+=1
        #     rec(j)
        # j = b[i]-a[i]+1
        # while j>0:
        #     b[j]+=1
        #     j-=1
    print(res)
