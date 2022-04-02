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

a = int(input())
b = int(input())


def solve(a,b):
    from math import log10
    res = 1
    e  = 0
    two = 0
    five = 0
    first = 0
    last = 1
    f =1
    mod = 10^10
    for i in range(a,b+1):
        x = i
        first+=log10(i)
        while x%10==0:
            x//=10
            e+=1
        while x%5==0:
            five+=1
            x//=5
        while x%2==0:
            two+=1
            x//=2
        if f :
            res*=x
        if res>10000000000:
            f = 0
        last*=x
        last%=10000
    res = str(res)
    e = e+min(two,five)
    if f:
        return str(res)+" * 10^"+str(e)
    else:
        last = last*pow(2,max(0,two-min(two,five)),100000)%100000
        ans = int(pow(10,first-int(first)+4))
        return "{}...{} * 10^{}".format(ans, int(last), e)
print(solve(a,b))

"""40238...53472 * 10^249"""

#28462...79008 * 10^2499
