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


from random import *
for _ in range(1,int(input())+1):
    while(True):
        w = randint(1,10)
        n = randint(1,10)
        a = [randint(1,n) for i in range(w)]
        res = float("inf")
        # w,n = mapi()
        # a = list(mapi())
        a.sort()
        l = -1
        r = n
        def check(mid):
            res = 0
            for i in range(w):
                res += min(abs(mid-a[i]), n-abs(mid-a[i]))
            # print(mid,res)
            return res
        def brute():
            res = float("inf")
            for i in range(1,n+1):
                res = min(res,check(i))
            return res
        def bs():
            l = -1
            res = float("inf")
            st = sorted(set(a))
            r = min(len(st),n)
            while r-l>4:
                m1 = l+r>>1
                m2 = m1+1
                x = a[m1]
                y = a[m2]
                if check(x)>check(y):
                    l = m1
                else:
                    r = m2
            ans = 0
            for i in range(max(1,l),min(r,w)):
                x = check(a[i])
                if res>x:
                    res = x
                    ans = a[i]
            idx = bisect.bisect_left(st,ans)

            diff = float("inf")
            asd = -1
            for i in range(max(0,idx-2), min(idx+2, len(st))):
                # print(st[i],check(st[i]))
                if res>check(st[i]):
                    res = min(res,check(st[i]))
                    asd = st[i]
            return res
        def simple():
            res = float("inf")
            tst = []
            st = sorted(set(a))
            m = len(st)
            tst+=st[:min(2,m)]
            tst+=st[max(m-2,0):]
            tst+=st[max(m//2-1,0):min(m,m//2+1)]
            for i in tst:
                res = min(res,check(i))
            return res
        if simple()!=brute():
            print(w,n,a,sep="\n")
            break
    # res = check(l+1)
    # print("Case #{}: {}".format(_, res))
