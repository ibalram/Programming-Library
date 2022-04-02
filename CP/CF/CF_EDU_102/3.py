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

from math import gcd
lcm = lambda x,y: x*y//gcd(x,y)
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(range(1,k+1))+list(range(k-1, 2*k-n-1,-1))
    p = list(range(1,k+1))
    p = p[:k-(n-k+1)]+p[k-(n-k+1):][::-1]
    # print(a,p)
    b = []
    # for i in range(n):
    #     b.append(p[a[i]-1])
    # print(*b)
    print(*p)
