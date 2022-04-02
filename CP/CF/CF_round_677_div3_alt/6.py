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

n,m,k = map(int,input().split())
mat = []
for i in range(n):
    mat.append(ilist())

@lru_cache(None)
def rec(i, j, count, rem):
    if i>=n:
        if rem==0: return 0
        return -float("inf")
    if j>=m:
        return rec(i+1, 0, 0, rem)
    res = max(rec(i+1, 0, 0,rem), rec(i, j+1, count,rem))
    if count<m//2:
        res = max(res, mat[i][j]+ rec(i, j+1, count+1, (rem+mat[i][j])%k))
        res = max(res, mat[i][j]+ rec(i+1, 0, 0, (rem+mat[i][j])%k))
    return res
print(rec(0,0,0,0))

