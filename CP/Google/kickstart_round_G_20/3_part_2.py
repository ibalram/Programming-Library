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

for _ in range(1,int(input())+1):
    res = 0
    w,n = mapi()
    a = list(mapi())
    a.sort()
    l = -1
    r = n+1
    def check(mid):
        res = 0
        for i in range(w):
            res += min(abs(mid-a[i]), n-abs(mid-a[i]))
        # print(mid,res)
        return res
    res = float("inf")
    tst = []
    st = sorted(set(a))
    m = len(st)
    tst+=st[:min(2,m)]
    tst+=st[max(m-2,0):]
    tst+=st[max(m//2-1,0):min(m,m//2+1)]
    print(st)
    print(list(map(check, tst)))
    for i in tst:
        res = min(res,check(i))
    # res = check(l+1)
    print("Case #{}: {}".format(_, res))
