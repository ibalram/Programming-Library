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
    n,s = map(int,input().split())
    a = [int(i) for i in str(n)][::-1]
    sm = sum(a)
    mul = 1
    res = 0
    # cr = 0
    num = 0
    while sm>s and num<len(a):
        if a[num]>0:
            res+=mul*(10-a[num])
            cr = 1
            a[num] = 0
            for i in range(num+1,len(a)):
                a[i]+=cr
                cr = a[i]//10
                a[i]%=10
            if cr:
                a.append(1)
                cr = 0
        sm = sum(a)
        mul*=10
        num+=1
    print(res)
