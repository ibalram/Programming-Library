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
input = sys.stdin.readline
n,q = map(int,input().split())
a = list(map(int,input().split()))
cntr = a.count(1)
for i in range(q):
    t,x = map(int,input().split())
    if t==1:
        a[x-1]^=1
        if a[x-1]==1:
            cntr+=1
        else:
            cntr-=1
    else:
        print(1*(cntr>=x))
