# kick start 2021 round D, 11 july 2021
# 4th question part 1

# // https://cses.fi/problemset/task/1648
# // Dynamic range sum  queries
# // from the data structures article of usaco.guide (gold)



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
class Seg:
    # 1-indexed
    initVal = 0
    def __init__(self, n):
        self.n = n
        self.seg = [initVal]*(2*n)

    def comb(self, a,b):
        return a+b

    def pull(self,p):
        self.seg[p] = self.comb(self.seg[2*p], self.seg[2*p+1])

    def update(self,p, val):
        p+=n
        self.seg[p] = val
        p//=2
        while p:
            self.pull(p)
            p//=2

    def query(self, l,r):
        ra,rb = initVal, initVal
        l+=n
        r+=n+1
        while l<r:
            if (l&1):
                ra = self.comb(ra, self.seg[l])
                l+=1
            if (r&1):
                r-=1
                rb = self.comb(self.seg[r], rb)
            l//=2
            r//=2
        return self.comb(ra,rb)
