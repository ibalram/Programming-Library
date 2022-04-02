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
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

# from math import gcd
def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)

def GCD(x, y):
   while(y):
       x, y = y, x % y
   return x

for _ in range(1,int(input())+1):
    res = 0
    n,q = imap()
    gr = defaultdict(list)
    edge = {}
    for i in range(n-1):
        x,y,li,ai = imap()
        gr[x].append((y,i))
        gr[y].append((x,i))
        edge[tuple(sorted([x,y]))] = [li,ai]
    def dfs(s,par):
        res = 0
        for i,idx in gr[s]:
            if i==par:continue
            parent[i] = s
            depth[i] = depth[s]+1
            dfs(i,s)
    def dfs2(s,par):
        st = [[s,par]]
        sz = [1]*(n+1)
        while st:
            s,par = st.pop()
            for i,idx in gr[s]:
                if i==par: continue
                parent[i] = s
                depth[i] = depth[s]+1
                st.append([i,s])
    parent = [i for i in range(n+1)]
    depth = [0]*(n+1)
    dfs2(1,-1)
    mp = defaultdict(list)
    res =[]
    for i in range(q):
        c,w = imap()
        mp[c].append((i,w,0))
    arr = list(range(2,n+1))
    arr.sort(key = lambda x: [-depth[x],x])
    for i in arr:
        ans = 0
        par = parent[i]
        li,ai = edge[(min(i,par),max(i,par))]
        for idx,w,ans in mp[i]:
            if li<=w:
                ans = GCD(ai,ans)
            mp[par].append((idx,w,ans))
        mp[i] = []
    res = [0]*(q)
    for i,w,ans in mp[1]:
        res[i] = ans
    # for i in range(q):
    #     c,w = imap()
    #     while c!=1:
    #         x = tuple(sorted([c,parent[c]]))
    #         l,a = edge[x]
    #         if l<=w:
    #             ans = gcd(ans,a)
    #         c = parent[c]
    #     res.append(ans)

    print("Case #{}:".format(_), *res)
