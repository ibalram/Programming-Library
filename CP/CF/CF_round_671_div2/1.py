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
    n = int(input())
    a = list(map(int,list(input().strip())))
    cnt = 0
    cmt = 0
    if n%2==0:
        print(1)
        continue
    for i in range(n):
        if i%2==0:
            cnt+=a[i]%2==0
        else:
            cmt+=a[i]%2

    # if cnt<cmt:
    #     print("1")
    # elif cmt>cnt:
    #     print("2")
    # elif min(cnt,cmt)==n//2:
    #     print("1" if n%2 else "2")
    # else:
