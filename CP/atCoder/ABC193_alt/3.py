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
sq = int(n**.5)
import math
res = 0
mrk = [0]*(sq+1)
for i in range(2,sq+1):
    if mrk[i]:continue
    res+=max(0,int(math.log(n)/math.log(i))-1)
    j = i*i
    while j<=sq:
        mrk[j]=1
        j*=i
print(n-res)
