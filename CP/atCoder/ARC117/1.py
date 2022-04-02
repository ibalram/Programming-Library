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

a,b = imap()
x = list(range(1,max(a,b)+1))
res = []
if a>b:
    res+=x
    res+=[-i for i in x[:b-1]]
    res+=[-sum(res)]
else:
    res+=[-i for i in x]
    res+=x[:a-1]
    res+=[-sum(res)]
print(*res)
