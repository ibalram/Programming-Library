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

n,m = imap()
a = []
for i in range(m):
    a.append(ilist())
a.sort()
# a.sort(key = lambda x: abs(x[1]-x[0]), x[1],x[0]
right = -123456
cnt = 0
for x,y in a:
    if y<=right:
        continue
    right = max(right, y)
    cnt+=1
res = cnt
left = +123456
cnt = 0
for x,y in a[::-1]:
    if y>=left:
        continue
    left = min(left, y)
    cnt+=1
res = max(cnt,res)
print(res)
