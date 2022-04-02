from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect
from collections import defaultdict, Counter, deque;
# from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    res = None
    n,c = imap()
    if n-1>c or c>=n*(n+1)//2:
        print("Case #{}:".format(_+1), "IMPOSSIBLE")
        continue
    b = [i for i in range(n,1,-1)]
    sm = sum(b)
    i = 0
    while sm>c and i<len(b):
        sub = b[i]-1
        diff = sm-c
        b[i] -= min(sub,diff)
        sm-=min(sub,diff)
        i+=1
    a = list(range(1,n+1))
    for i in range(n-2,-1,-1):
        a[i:i+b[i]] = a[i:i+b[i]][::-1]
    # cost = 0
    # for i in range(n-1):
    #     mn = a.index(min(a[i:]))
    #     a[i:mn+1] = a[i:mn+1][::-1]
    #     cost+=mn-i+1
    # print(b)
    # print(cost,c)
    print("Case #{}:".format(_+1),*a)

