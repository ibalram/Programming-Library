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

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = []
    for i in range(n):
        x.append([a[i],i])
        x.append([b[i],i])
    x.sort()
    lst = n
    res = n
    for i in range(2*n):
        if i%2==0:
            lst = min(lst, x[i][1])
        else:
            res = min(res,x[i][1]+lst)
    print(res)
