import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**6)
mod = int(1e9+7)


h,w,a,b = imap()
# if h>w:
#     h,w = w,h

memo = {}

@lru_cache(None)
def count_tilings_rec(uncovered, a, b):
    # if len(uncovered) & 1:
    #     return 0
    if not uncovered:
        return 1
    res = 0
    if uncovered not in memo:
        i, j = min(uncovered)
        if a:
            res+= count_tilings_rec(uncovered - {(i, j), (i, j + 1)}, a-1,b) + count_tilings_rec(uncovered - {(i, j), (i + 1, j)},a-1,b)
        if b:
            res+= count_tilings_rec(uncovered - {(i, j)}, a, b-1)
    # return memo[uncovered]
    return res
def count_tilings(m, n, a,b):
    return count_tilings_rec(frozenset((i, j) for i in range(max(m, n)) for j in range(min(m, n))), a,b)
print(count_tilings(h,w,a,b))

