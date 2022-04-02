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
a = ilist()
b = ilist()

mxa = 0
mxb = 0
c = [0]
mxaRes = 0
for i in range(n):
    # mxb = max(mxb, b[i])
    if a[i]>mxa and a[i]*b[i]>c[-1]:
        mxa = a[i]
        mxb = b[i]
    mxaRes = max(mxaRes,a[i])
    if mxaRes*b[i]>c[-1]:
        mxa = mxaRes
        mxb = b[i]
    c.append(mxa*mxb)
print(*c[1:], sep="\n")

