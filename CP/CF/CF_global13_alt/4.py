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


import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
for _ in range(int(input())):
    u,v = map(int,input().split())
    if u==v:
        print("YES")
        continue
    res = "NO"
    if not (u<=v and bin(u).count("1")>=bin(v).count("1")):
        print("NO")
        continue
    while u<v:
        while (u&1)==(v&1):
            u//=2
            v//=2
        if not v or (u&1)<(v&1):break
        x,y = u,0
        while (x&1) and u+2*y+1<=v:
            x//=2
            y*=2
            y+=1
        u+=y
    if u==v: res = "YES"
    print(res)

