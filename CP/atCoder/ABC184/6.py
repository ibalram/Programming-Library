# (Meet in the middle) (MITM) (mitm)
# - split array in two halfs
# - calc subset sums for these two arrays (2^(n//2) subsets) and store them
# - sort one array of subsets sums
# - iterate second array and using binary search find in another array
# to make sum <=T (2^(n//2)*log(2^(n//2)) = (n//2)*2^(n//2))
#


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

n,t = imap()
a = ilist()

n,m = n//2, n-n//2

def calc(a, n):
    smArray = []
    for i in range(1<<n):
        sm = 0
        for j in range(n):
            if (i>>j)&1!=0: continue
            if sm+a[j]<=t:
                sm+=a[j]
            else:
                break
        smArray.append(sm)
    return smArray

x = calc(a[:n], n)
y = calc(a[n:], m)
y.sort()
res = 0
for i in x:
    it = bisect.bisect_right(y, t-i) - 1
    if it<0: continue
    res = max(res, i+y[it])
print(res)
