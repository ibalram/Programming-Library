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
    l,r = map(int,input().split())
    x = r-l-1
    if l!=1 and r!=1 and l>x and r%l:
        # anss = -1
        # # print("yes")
        # for i in range(r,r+1):#+l-x):
        #     prev = i%l
        #     f = 1
        #     for j in range(l+1,r+1,1):
        #         if i%j>=prev:
        #             f = 0
        #             break
        #         prev = i%j
        #     if f:
        #         anss = i
        #         break
        print(r)
    else:
        print(-1)




