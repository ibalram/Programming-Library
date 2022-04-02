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

#4
n,m = imap()
a = ilist()
a.sort()
b = []
lst = 0
for i in a:
    if i-lst-1>0:
        b.append(i-lst-1)
    lst = i
if n-lst>0:
    b.append(n-lst)

from math import gcd

if not b:
    print(0)
    exit(0)
gc = b[0]
for i in b[1:]:
    gc = min(gc,i)
res = 0
for i in b:
    res += (i+gc-1)//gc
print(res)
# print(b,gc)


