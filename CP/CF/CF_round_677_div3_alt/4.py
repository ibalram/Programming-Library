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
sys.setrecursionlimit(3*10**5)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    par = [i for i in range(n)]
    sz = [1]*n
    def find(x):
        if par[x]==x:
            return x
        par[x] = find(par[x])
        return par[x]
    res = []
    for u in range(n):
        for v in range(u+1,n):
            if a[u]==a[v]: continue
            x = find(u)
            y = find(v)
            if x==y: continue
            if sz[x]>sz[y]:x,y = y,x
            sz[y]+=sz[x]
            par[x] = y
            res.append([u+1,v+1])
    cnt = -1
    for i in range(n):
        if par[i]==i:
            cnt+=1
    if cnt:
        print("NO")
    else:
        print("YES")
        for i in res:
            print(*i)
