import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(2*(10**6))
mod = int(1e9+7)

n = int(input())
s = list(map(int,list(input().strip())))
x = list(input().strip())

@lru_cache(None)
def rec(idx, num):
    if idx==n-1:
        nw = num*10
        if x[idx]=="A":
            return nw%7!=0 or (nw+s[idx])%7!=0
        else:
            return nw%7==0 or (nw+s[idx])%7==0
    res = 0
    for nxt in [0,s[idx]]:
        if x[idx+1]!=x[idx]:
            res|=not rec(idx+1, (num*10+nxt)%7)
        else:
            res|=rec(idx+1, (num*10+nxt)%7)
    return res
chk = rec(0,0)
if x[0]=="A":
    print("Aoki" if chk else "Takahashi")
if x[0]=="T":
    print("Aoki" if chk==0 else "Takahashi")
