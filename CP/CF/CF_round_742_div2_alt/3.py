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

for _ in range(int(input())):
    a = list(map(int,list(input())))
    a = a[::-1]
    n = len(a)
    @lru_cache(None)
    def rec(i,x,y):
        if i==n:
            return (x,y)==(0,0)
        res = 0
        for j in range(10):
            for k in range(10):
                res+=(j+k+x)%10==a[i] and rec(i+1,y,(j+k+x)//10)
        return res
    print(rec(0,0,0)-2)
