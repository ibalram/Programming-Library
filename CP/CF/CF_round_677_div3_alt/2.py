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
    l = 0
    while l<n and a[l]==0:
        l+=1
    r = n-1
    while r>=0 and a[r]==0:
        r-=1
    cnt = 0
    res = 0
    # print(l,r)
    for i in range(l,r+1):
        if a[i]==0:
            cnt+=1
        else:
            if cnt: res+=cnt
            cnt = 0
    if cnt:res+=cnt
    print(res)

