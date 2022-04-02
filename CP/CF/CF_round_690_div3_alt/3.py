import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
import sys
sys.setrecursionlimit(10**6)
mod = int(1e9+7)

for _ in range(int(input())):
    n =int(input())
    a = list(range(9,0,-1))
    def rec(i,sm ,mark):
        global res
        if sm<=0:
            # res = min(res, mark)
            tmp = ""
            for i in range(9):
                if (mark>>i)&1:
                    tmp+=str(a[i])
            res = min(res, int(tmp[::-1]))
            return
        if i>=9: return
        if a[i]<=sm:
            rec(i+1, sm-a[i], mark|(1<<i))
        rec(i+1, sm, mark)
    res = float("inf")
    rec(0,n,0)
    if res == float("inf"):
        print(-1)
    else:
        ans = ""
        print(res)

