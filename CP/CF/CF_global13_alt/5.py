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

n = int(input())
fb = [0]*(200005)
fb[0] = fb[1] = 1
mp = defaultdict(int)
mp[1] = 1
for i in range(2,200005):
    fb[i] = fb[i-1]+fb[i-2]
    # mp[fb[i]] = i
g = defaultdict(list)
for i in range(n-1):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
if mp[n]==0:
    print('NO')
    exit()

# exit()
par = [i for i in range(n+1)]
sz = [0]*(n+1)
mrk = [0]*(n+1)
hv = [0]*(31)
def dfs(v,pr):
    par[v] = pr
    sz[v] = 1
    for u in g[v]:
        if mrk[u] or u==pr:
            continue
        dfs(u,v)
        sz[v]+=sz[u]
    if mp[sz[v]]: hv[mp[sz[v]]] = v
def rec(root, size, val):
    if size==1: return 1
    for i in range(1,31):
        hv[i] = 1
    dfs(root,-1)
    if hv[val-1]:
        tmp = hv[val-1]
        mrk[par[tmp]] = mrk[tmp] = 1
        up = rec(par[tmp], fb[val-2], val-2)
        down = rec(tmp, fb[val-1], val-1)
        return down and up
    elif val-2>=0 and hv[val-2]:
        tmp = hv[val-2]
        mrk[par[tmp]] = mrk[tmp] = 1
        up = rec(par[tmp], fb[val-1], val-1)
        down = rec(tmp, fb[val-2], val-2)
        return down and up


dfs(1,-1)
print("YES" if rec(1,n,mp[n]) else "NO")
