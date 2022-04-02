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

a,b = map(int,input().split())
c,d = map(int,input().split())

x = abs(c-a)
y = abs(d-b)
if x==0 and y==0:
    print(0)
elif x==y or x+y<=3:
    print(1)
elif x%2==y%2 or abs(x-y)<=3:
    print(2)
else:
    print(3)
