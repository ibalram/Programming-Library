import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(10**4)
mod = int(1e9+7)

for _ in range(int(input())):
    n = int(input())
    a = [list(map(int,list(input()))) for i in range(2)]
    # print(a)
    @lru_cache(None)
    def rec(i,j):
        if i==1 and j==n-1:
            return a[i][j]==0
        res = 0
        # print(i,j)
        if i+1<2 and a[i+1][j]==0:
            res|=rec(i+1,j)
        if j+1<n and a[i][j+1]==0:
            res|=rec(i,j+1)
        if i+1<2 and j+1<n and a[i+1][j+1]==0:
            res|=rec(i+1,j+1)
        if i-1>=0 and j+1<n and a[i-1][j+1]==0:
            res|=rec(i-1,j+1)
        return res
    print("YES" if rec(0,0) else "NO")
