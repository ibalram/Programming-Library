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
    l = 0
    r = n-1
    while l<n-1 and a[l]>=a[l+1]:
        l+=1
    while r>0 and a[r]>=a[r-1]:
        r-=1
    sm = a[l]+a[r]
    ll = l+1
    while ll<n and a[ll-1]<=a[ll] and a[ll]<=sm:
        ll+=1
    rr = r-1
    while rr>=0 and a[rr+1]<=a[rr] and a[rr]<=sm:
        rr-=1
    print("YES" if ll>rr else "NO")
    # print(sm,ll,rr)
    # ll = 0
    # rr = n-1

    # while ll<=rr:
    #     while ll<n-1 and a[ll]>=a[ll+1]:
    #         ll+=1
    #     while rr>0 and a[rr]>=a[rr-1]:
    #         rr-=1
    #     sm = a[ll]+a[rr]
    #     if sm<prev:
    #     ll = ll+1
    #     while ll<n and a[ll-1]<=a[ll] and a[ll]<=sm:
    #         ll+=1
    #     rr = rr-1
    #     while rr>=0 and a[rr+1]<=a[rr] and a[rr]<=sm:
    #         rr-=1
    #     prev = sm

