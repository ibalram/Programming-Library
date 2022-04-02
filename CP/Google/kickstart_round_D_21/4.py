from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


import os, bisect
# from heapq import heapify, heappop, heappush
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


def comb(a,b):
    return a+b
class Seg:
    def __init__(self, n):
        self.n = n
        self.seg = [0]*(2*n)

    def pull(self,p):
        self.seg[p] = comb(self.seg[2*p], self.seg[2*p+1])

    def upd(self,p, val):
        p+=n
        self.seg[p] = val
        p//=2
        while p:
            self.pull(p)
            p//=2
    def query(self, l,r):
        ra = 0
        rb = 0
        l+=n
        r+=n+1
        while l<r:
            if (l&1):
                ra = comb(ra, self.seg[l])
                l+=1
            if (r&1):
                r-=1
                rb = comb(self.seg[r], rb)
            l//=2
            r//=2
        return comb(ra,rb)


for _test in range(int(input())):
    res = []
    n,q,_p = imap()
    a = [0]+ilist()

    def V(ai, s):
        x = (ai**s) -((ai%_p)**s)
        res = 0
        while x>0 and x%_p==0:
            res+=1
            x//=_p
        return res
    st = [Seg(n+1) for i in range(5)]
    for s in range(1,5):
        for i in range(1,n+1):
            st[s].upd(i,V(a[i],s))
    for i in range(q):
        qe = ilist()
        if len(qe)==3:
            _, pos, val = qe
            for s in range(1,5):
                st[s].upd(pos, V(val,s))
        else:
            _,s,l,r = qe
            res.append(st[s].query(l,r))

    print('Case #{}:'.format(_test+1), *res)
