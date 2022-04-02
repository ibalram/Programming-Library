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
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    from collections import defaultdict
    mpc = {}#defaultdict(list)
    mpd = {}
    mp = defaultdict(list)
    # for i in range(n):
    #     mp[a[i]].append(i)
    res = [0]*n
    for i in range(n):
        if t-a[i] not in mpc:
            mpc[a[i]] = 1
            res[i] = 1
        elif t-a[i] not in mpd:
            mpd[a[i]] = 1
            # res[i] = 1
        else:
            mp[a[i]].append(i)
    for key in mp.keys():
        for j in range(len(mp[key])):
            if j%2:
                res[mp[key][j]] = 1
    # for i in mpc.values():
    #     res[i] = 1
    # for i in mp.keys():
    #     for j in range(len(mp[i])):
    #         if j%2:
    #             res[mp[i][j]] = 1
    print(*res)

