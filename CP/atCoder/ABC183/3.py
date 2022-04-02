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

n,k = imap()
mat = []
for i in range(n):
    mat.append(ilist())

@lru_cache(None)
def dfs(mask, last, cost):
    if mask==(1<<n)-1:
        return cost+mat[last][0]==k
    res = 0
    for i in range(n):
        if (mask>>i)&1==0:
            res+=dfs(mask|(1<<i), i, cost+mat[last][i])
    return res

print(dfs(1, 0, 0))
