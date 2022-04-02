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

def calc(s):
    res = 0
    for i in s:
        res+= ord(i)-ord("a")+1
    return res


for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        s = input().strip()
        a.append(s)
        wt = 0
        for j in s:
            wt+= ord(j)-ord("a")+1
        b.append([wt, i])
    b.sort()
    res = []
    for i in [n//2, n//2-1, n//2+1, n//2+2, n//2-2]:
        if i>=n or i<0: continue
        w = 0
        maxDiff = -1
        maxIdx = -1
        for j in range(n):
            diff = abs(b[i][0]-b[j][0])
            if diff> maxDiff:
                maxDiff = diff
                maxIdx = b[j][1]
            w+=diff
        w-=maxDiff
        res.append([w,maxIdx])
    res.sort()
    print(a[res[0][1]])

