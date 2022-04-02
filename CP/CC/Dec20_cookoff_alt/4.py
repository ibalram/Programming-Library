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
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    # a.sort(reverse=True)
    res = 0
    if m==1:
        res=max(n-a[0]-1,0)
        n-=res
        while n>1 and a[0]%n!=0:
            res+=1
            n-=1
        print(res)
        continue
    gc = a[0]
    for i in a[1:]:
        gc = gcd(gc, i)
    res = 0
    if n<gc:
        res=max(n-gc-1,0)
        n-=res
        while n>1 and gc%n!=0:
            res+=1
            n-=1
        print(res)
        continue
    print(n-gc)
    # res = 0
    # for i in a:
    #     if n>i:
    #         res+=n-i
    #         n = i
    #     else:
    #         while n>1 and i%n!=0:
    #             # print(n,"case",_)
    #             res+=i%n
    #             n = n-i%n
    #     if n<=1:
    #         break
    # print(res)
