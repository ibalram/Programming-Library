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
    a = list(input().strip())
    res = 0
    vis = [0]*n
    out = [0]*n
    from collections import defaultdict
    gr = defaultdict(list)
    cnt = 0
    st = set()
    for i in range(n):
        if a[i]=="-":
            st.add(i)
            st.add((i+1)%n)
            cnt+=1
            vis[i] += 1
            out[i] += 1
            vis[(i+1)%n] += 1
            out[(i+1)%n] += 1
    res+=len(st)
    cnt2 = cnt
    for i in range(n):
        if a[i]==">":
            cnt+=1
            vis[(i+1)%n] +=1
            out[i]+=1
        elif a[i]=="<":
            cnt2 +=1
            vis[i] += 1
            out[(i+1)%n]+=1
    # print(*vis)
    # print(*out)
    if cnt==n or cnt2==n:
        res = n
    # res = 0
    # for i in range(n):
    #     res+= (vis[i]!=0) and (out[i]!=0)
    print(res)
