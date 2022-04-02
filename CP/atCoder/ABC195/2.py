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

a,b,w = imap()
w*=1000
f = 0
mx = 0
mn = 0
ww = w
for i in range(b,a-1,-1):
    if w%i==0:
        mn+=w//i
        w%=i
        if w==0:
            break
if w:
    f = 1
for i in range(a,b+1):
    if ww%i==0:
        mx+=ww//i
        ww%=i
        if ww==0:
            break
if ww:
    f = 1
print("UNSATISFIABLE" if f else " ".join([str(mn),str(mx)]))

