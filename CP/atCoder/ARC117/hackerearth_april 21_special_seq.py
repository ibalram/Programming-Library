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

a = [i*int(i**.5)+i//2 for i in range(200000)]
for i in range(1,200000):
    a[i]+=a[i-1]

def find(k):
    l,r = 0,200000
    while r-l>1:
        mid = l+r>>1
        if a[mid]>=k:
            r = mid
        else:
            l = mid
    return r

for _ in range(int(input())):
    l,r = map(int,input().split())
    print(find(r)-find(l)+1)

# print(sum(a))
