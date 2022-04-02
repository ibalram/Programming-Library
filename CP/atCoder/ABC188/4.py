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

n,C = imap()
a = [0]*(n)
b = [0]*(n)
c = [0]*(n)
d = []
for i in range(n):
    a[i],b[i],c[i] = imap()
    d.append([a[i],-1,i])
    d.append([b[i],1,i])
d.sort()
st =[]
for val,flag,idx in d:



