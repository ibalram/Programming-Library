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
a = [0]*(n)
b,c,d,e = a[:],a[:],a[:],a[:]
for i in range(n):
    a[i],b[i],c[i],d[i],e[i] = imap()
mpa = defaultdict(list)
mpb  = defaultdict(list)
mpc = defaultdict(list)
mpd = defaultdict(list)
mpe = defaultdict(list)
mpij = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        mp[]
