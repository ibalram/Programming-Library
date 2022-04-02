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
a = []
for i in range(n):
    a.append(ilist())
res = 0
for i in range(n):
    t,x,y = a[i]
    if t==2:
        y-=0.001
    elif t==3:
        x+=0.001
    elif t==4:
        x+=0.001
        y-=0.001
    if x>y:
        continue
    for j in range(i+1,n):
        tt,xx,yy = a[j]
        if tt==2:
            yy-=0.001
        elif tt==3:
            xx+=0.001
        elif tt==4:
            xx+=0.001
            yy-=0.001
        if xx>yy:
            continue
        if max(x,xx)<=min(y,yy):
            res+=1
        # print(x,y," ", xx,yy)
print(res)
