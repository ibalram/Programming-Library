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
    from collections import defaultdict
    mp = defaultdict(list)
    # mp[a[0]] = 1
    pst = {}
    # pst[a[0]] = 0
    for i in range(n):
        if len(mp[a[i]])==0:
            mp[a[i]].append(i)
            pst[a[i]] = i
        else:
            pst[a[i]] = max(pst[a[i]], i-mp[a[i]][-1]-1)
            mp[a[i]].append(i)
    for i in mp.keys():
        pst[i] = max(pst[i], n-1-mp[i][-1])
    lst = n
    res = [-1]*(n)
    # print(pst)
    for i in sorted(pst.keys()):
        # print(i,pst[i],lst)
        for j in range(pst[i], lst):
            res[j] = i
        lst = min(lst,pst[i])
    print(*res)
