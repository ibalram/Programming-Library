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
    a,b,x,y,n = map(int,input().split())
    # if a>b:
    #     if a-x<b-y:
    #         a,b = b,a
    #         x,y = y,x
    # elif a==b:
    #     if a-x<b-y:
    #         a,b = b,a
    #         x,y = y,x
    if a-min(n,a-x)>b-min(n,b-y):
        a,b = b,a
        x,y = y,x
    a,n = a-min(n,a-x), n-min(n,a-x)
    b-=min(n,b-y)
    print(a*b)
