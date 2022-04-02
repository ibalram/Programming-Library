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

from collections import defaultdict, deque
for _ in range(int(input())):
    n = int(input())
    gr = defaultdict(list)
    deg = [0]*(n+1)
    for i in range(1,n+1):
        for x in list(map(int,input().split()))[1:]:
            gr[x].append(i)
            deg[i]+=1
    q = deque()
    cnt = 0
