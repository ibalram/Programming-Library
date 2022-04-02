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
sys.setrecursionlimit(10**7)
#------------------------------------------------------------------

for _ in range(1,int(input())+1):
    res = 0
    n = int(input())
    a = list(mapi())
    def rec(dec):
        if len(dec)==1:
            return 0
        sm = 0
        for i in range(1,len(dec)):
            sm+=dec[i-1]+dec[i] +rec(dec[:i-1]+[dec[i-1]+dec[i]]+dec[i+1:])
        return sm/(len(dec)-1)
    res = rec(a)

    print("Case #{}: {}".format(_, res))
