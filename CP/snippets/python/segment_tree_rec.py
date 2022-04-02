# kick start 2021 round D, 11 july 2021
# 4th question part 1

# // https://cses.fi/problemset/task/1648
# // Dynamic range sum  queries

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



# point update and range query/sum
# untested
class Seg:
    # 1-indexed
    def __init__(self, n):
        self.n = n
        self.initVal = 0
        self.seg = [self.initVal]*(4*n)

    def query(self, l,r):
        return self._query(1, 1, n, l, r)

    def update(self, p, val):
        self._update(1, 1, n, p, val)

    def _comb(self, a, b):
        return a+b

    def _pull(self,p):
        self.seg[p] = self._comb(self.seg[2*p], self.seg[2*p+1])

    def _update(self, root, start, end, pos, val):
        if start>end or pos<start or pos>end: return
        if start==end:
            self.seg[root]=val
            return
        mid = start+end>>1
        if pos<=mid: self._update(2*root, start, mid, pos, val)
        else: self._update(2*root+1, mid+1, end, pos, val)
        self._pull(root)

    def _query(self, root, start, end, l, r):
        res = self.initVal
        if r<start or l>end: return res
        if start<=l and r<=end: return self.seg[root]
        mid = start+end>>1
        left = self._query(2*root, start, mid, l, r)
        right = self._query(2*root+1, mid+1, end, l, r)
        return self._comb(left, right)
