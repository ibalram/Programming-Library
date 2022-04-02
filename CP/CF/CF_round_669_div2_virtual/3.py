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

n = int(input())
res = [0]*(n+1)
mx = 1
for i in range(2,n+1):
    print("? {} {}".format(mx,i),flush=True)
    x = int(input())
    print("? {} {}".format(i,mx),flush=True)
    y = int(input())
    if x>y:
        res[mx] = x
        mx = i
    else:
        res[i] = y
res[mx] = n
print("!",*res[1:],flush=True)


