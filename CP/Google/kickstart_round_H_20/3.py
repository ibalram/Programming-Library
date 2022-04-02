from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    n = int(input())
    xex = []
    yex = []
    for i in range(n):
        x,y = imap()
        xex.append(x)
        yex.append(y)
    xex.sort()
    yex.sort()
    xp, yp = xex[(n+1)//2-1], yex[(n+1)//2-1]
    yres = 0
    # cand = [i+xp for i in range(n)]
    cand = [0]*n
    k = xp
    for i in range((n+1)//2-1,n):
        cand[i] = k
        k+=1
    k = xp-1
    for i in range((n+1)//2-1):
        cand[i] = k
        k-=1
    for i in range(n):
        yres+=abs(yp-yex[i])
    res = yres
    # for k in range(n):
    #     ret = 0
    #     for i in range(n):
    #         ret+=abs(xex[i]-cand[i]+k)
    #     res =min(res, ret+yres)
    for i in range(n):
        res+=abs(xex[i]-cand[i])
    # print(cand)
    # print(xex)
    # print(xp,yp,yres)
    print("Case #{}:".format(_+1), res)
