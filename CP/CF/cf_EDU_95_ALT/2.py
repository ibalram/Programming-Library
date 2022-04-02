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

for _ in  range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    b = []
    for i in range(n):
        if l[i]==0:
            b.append(a[i])
    c = b[:]
    b.sort()
    for i in range(n-1,-1,-1):
        if l[i]==0:
            a[i]=b.pop()
    k = -1
    sm = 0
    for i in range(n):
        sm+=a[i]
        if sm<0:
            k = i
    d = a[:]
    c.sort(reverse=True)
    for i in range(n-1,-1,-1):
        if l[i]==0:
            d[i]=c.pop()
    f = -1
    sm = 0
    for i in range(n):
        sm+=d[i]
        if sm<0:
            f = i
    if k<=f:
        print(*a)
    else:
        print(*d)

