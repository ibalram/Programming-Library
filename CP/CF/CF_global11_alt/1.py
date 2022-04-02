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
    n = int(input())
    a = list(map(int,input().split()))
    if sum(a)==0:
        print("NO")
        continue
    a = sorted(a, reverse=(True if sum(a)>0 else False))
    sm = 0
    f = 0
    for i in a:
        sm+=i
        if sm==0:
            f = 1
            break
    if f :
        print("NO")
    else:
        print("YES")
        print(*a)
