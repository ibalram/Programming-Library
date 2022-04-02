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
    n,s,k = imap()
    l = 0
    r = n*k
    res = -1
    # while r-l>1:
    #     mid = l+r>>1
    #     if ((mid+1)-s)%k==0 :
    #         res = ((mid+1)-s)/k
    #     if ((mid+1)-s)/k
    x = n-s
    print(n%k, n//k, k-n%k, (n-s)//k, (n-s)%k)
    a = k-n%k
    b = (n-s)%k
    # print((n//k)*()

print(715*6)

# x time k means dis = x = (n*y + n-s )/k
# (n*(y+1)-s)/k
# (y+1) *(n/k) -s/k
