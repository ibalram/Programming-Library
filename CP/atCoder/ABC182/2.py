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
# mp = defaultdict(int)
res = 0
mx = 0
for j in range(2,1001):
    cnt = 0
    for i in a:
        if i%j==0:
            cnt+=1
    if cnt>mx:
        res = j
        mx = cnt
print(res)
