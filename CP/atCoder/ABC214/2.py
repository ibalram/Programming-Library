# https://atcoder.jp/contests/abc214/tasks/abc214_b
# https://atcoder.jp/contests/abc214/submissions/25027017

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

s,t = imap()

res = 0
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            if i+j+k<=s and i*j*k<=t:
                res+=1
print(res)
