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
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a<=0 or b<=0:
        print(max(a,b),0)
        continue
    if abs(a-b)==1:
        print(1,0)
        continue
    d = abs(a-b)
    if d==0:
        print(0,0)
        continue
    a,b = max(a,b),min(a,b)
    x = b%d
    y = d-x
    print(d, min(x,y))
    # if a%b==0 and d<=b:
    #     print(b,0)
    #     continue
    # x = a%d
    # y = b%d
    # xx = d-x
    # yy = d-y
    # l = x*y//gcd(x,y)
    # m = xx*yy//gcd(xx,yy)
    # print(d,min(l,m))
