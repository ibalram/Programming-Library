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

n = int(input())
a = []
b = []
for i in range(n):
    x = input().strip()
    if x[0] == "!":
        a.append(x[1:])
    else:
        b.append(x)
a.sort()
if len(a)<len(b):
    a,b = b[:],a[:]
mp = set(a)
res = "satisfiable"
for i in b:
    if i in mp:
        res = i
        break
print(res)


