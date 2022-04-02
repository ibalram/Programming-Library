import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
sys.setrecursionlimit(3*10**6)
mod = int(1e9+7)

mat = []
for i in range(4):
    x = ilist()
    for j in range(4):
        if x[j]==1:
            mat.append((i+1,j+1))

dr = [(0,1),(1,0),(-1,0),(0,-1)]
path = set()
skip = set()
def rec(i,j):
    res = 0
    f = 0
    for dx,dy in dr:
        x = i+dx
        y = j+dy
        if 1<=x<=4 and 1<=y<=4 and (x,y) not in path and (x,y) not in skip:
            f = 1
            path.add((x,y))
            res+=rec(x,y)
            path.remove((x,y))
            skip.add((x,y))
            res+=rec(i,j)
            skip.remove((x,y))
    if not f:
        for x in mat:
            if x not in path:
                return 0
        return 1
    return res

print(772992//16)
# ls = [rec(i,j) for i in range(1,5) for j in range(1,5)]
ls = []
for x in range(1,5):
    for y in range(1,5):
        res = 0
        path.add((x,y))
        res+=rec(x,y)
        path.remove((x,y))
        skip.add((x,y))
        res+=rec(i,j)
        skip.remove((x,y))
        ls.append(res)
print(ls)
# print(sum(ls))
