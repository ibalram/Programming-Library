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

n,m,T = imap()
t = n
lst = 0
f = 1
for i in range(m):
    a,b = imap()
    t = max(0, t-(a-lst))
    # print(t)
    if not t:
        f = 0
        break
    t = min(n, t+b-a)
    # print(t)
    lst = b
t = max(0,t-(T-b))
if t and f:
    print("Yes")
else:
    print("No")
