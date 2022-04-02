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
    l = -1
    res = float("inf")
    st = sorted(set(a))
    r = min(len(st),n)
    while r-l>4:
        m1 = l+r>>1
        m2 = m1+1
        if check(m1)>check(m2):
            l = m1
        else:
            r = m2
    ans = 0
    for i in range(max(1,l),min(r,n+1)):
        x = check(i)
        if res>x:
            res = x
            ans = i
    idx = bisect.bisect_left(st,ans)

    diff = float("inf")
    asd = -1
    for i in range(max(0,idx-2), min(idx+2, len(st))):
        # print(st[i],check(st[i]))
        if res>check(st[i]):
            res = min(res,check(st[i]))
            asd = st[i]
    # print(max(ans,asd))
    print("Case #{}: {}".format(_, res))
