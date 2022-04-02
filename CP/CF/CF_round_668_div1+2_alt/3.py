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
    n,k = map(int,input().split())
    s = "1"+input().strip()
    flag = 1
    o = defaultdict(int)
    z = defaultdict(int)
    q = defaultdict(int)
    for i in range(1,n+1):
        o[i] = o[i-1]+(s[i]=="1")
        z[i] = z[i-1]+(s[i]=="0")
        q[i] = q[i-1]+(s[i]=="?")
    on = 0
    ze = 0
    for i in range(k,n+1):
        one = o[i]-o[i-k]
        zero = z[i]-z[i-k]
        dif = one-zero
        que = q[i]-q[i-k]
        # print(one,zero,que)
        one = max(one-on,0)
        zero = max(zero-ze,0)
        # print(one,zero,que)
        if one>k//2 or zero>k//2 or one+zero+que<k:
            flag = 0
        on=k//2-one
        ze=k//2-zero

    print("YES" if flag else "NO")

