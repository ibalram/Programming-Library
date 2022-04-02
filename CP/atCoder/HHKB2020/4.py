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

mod = int(1e9+7)
for _ in range(int(input())):
    n,a,b = mapi()
    a,b = min(a,b),max(a,b)
    m = min(n,b-a-1)
    y = n-a+1
    z = -a+b+1
    res = 4*(y**2-z**2)
    print(res%mod)
    # if n%2==b%2:
    #     a,b = b,a
    # z = n-a-b+1
    # res = 4*(z*(z+1)%mod*(n-b+1)-z**2)%mod
    # if n%2==a%2:
    #     res+=4*(z)*(n-b+1)%mod
    # print(res%mod)
