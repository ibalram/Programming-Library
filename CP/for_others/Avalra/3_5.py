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
    first = 1
    flag = False
    last = 1
    e = 0
    for i in range(a,b+1):
        first *=i
        last*=i
        if len(str(first))>10:
            flag = True
            first = int(str(first)[:10])
        while last%10==0:
            last//=10
            e+=1
        if len(str(last))>10:
            last = int(str(last)[-10:])
    first = str(first)
    last = str(last)
    if flag:
        return first[:5]+"..."+last[-5:]+" * 10^"+str(e)
    else:
        return last+" * 10^"+str(e)
print(solve(a,b))

"""40238...53472 * 10^249"""

#28462...79008 * 10^2499
