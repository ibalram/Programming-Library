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
    mp = [0]*31
    for i in a:
        lst = -1
        for j in range(31):
            if (i>>j)&1:
                lst = j
        if lst!=-1:
            mp[lst]+=1

    res =0
    for i in range(31):
        res+=mp[i]*(mp[i]-1)//2
    print(res)
