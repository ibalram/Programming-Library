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


n,x,pos = map(int,input().split())

def bs(pos):
    l = 0
    r = n
    small = set()
    large = set()
    eq = 0
    while l<r:
        mid = l+r>>1
        # print(mid)
        if mid<=pos:
            if mid!=pos:
                small.add(mid)
            else:
                eq+=1
            l = mid+1
        else:
            r = mid
            if mid<n:
                large.add(mid)
    if l!=pos and l<n:
        large.add(l)
    # print(small)
    # print(large)
    return eq, len(small),len(large)
eq,small,large = bs(pos)
# print(small)
# print(large)

lr = n-x
sm = n-lr-1

fact = [1]*(n+1)
for i in range(2,n+1):
    fact[i] = fact[i-1]*i%mod

def inv(x):
    return pow(x,mod-2,mod)

def ncr(n,r):
    if n<r:
        return 0
    if n<=r or r==0 or r==n:
        return 1
    # return fact[n]//fact[r]//fact[n-r]
    return fact[n]%mod*inv(fact[r])%mod*inv(fact[n-r])%mod

# if eq:
#     lr-=1
print(n,lr,small,large)
print(fact[n-large-small-1]%mod
    *ncr(n-lr-1,small)%mod*fact[small]%mod
    *ncr(lr,large)%mod*fact[large]%mod)

# print(fact[n-large-small-1],
#     ncr(n-lr-1,small)%mod,fact[small]%mod,
#     ncr(lr,large)%mod,fact[large]%mod)

