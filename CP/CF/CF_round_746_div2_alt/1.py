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
    n,h = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    x = a[-1]
    y = a[-2]
    m = 2*(h//(x+y))
    rem = h%(x+y)
    if rem==0:
        pass
    elif (rem)<=x:
        m+=1
    else:
        m+=2
    print(m)
