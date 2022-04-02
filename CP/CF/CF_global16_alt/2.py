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

for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    a = []
    for i in range(1,n):
        if s[i]!=s[i-1]:
            a.append(s[i-1])
    a.append(s[-1])
    print(min(2,a.count("0")))
