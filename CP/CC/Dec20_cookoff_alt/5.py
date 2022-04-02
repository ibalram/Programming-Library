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


# from math import gcd
# for _ in range(int(input())):
#     s = input().strip()
#     n = len(s)
#     l = 0
#     i = 1
#     mp = defaultdict(int)
#     mp[s[i]]+=1
#     while i<n:
#         cnt = mp["?"]
#         if cnt%2



a = [9,19, 10,8,13]
n = len(a)


def solve(n,a):
    from bisect import bisect_left
    a.sort()
    res = 0
    for i in range(n-1):
        j = bisect_left(a, a[i]+a[i+1])-1
        if j<=i+1: continue
        res = max(res, j-i+1)
    return res
# print(solve(n,a))

mxn = 505
spf = [0]*mxn
def sieve():
    spf[1]=1
    for i in range(2,mxn): spf[i]=i
    for i in range(4,mxn,2): spf[i]=2
    for i in range(3,int(mxn**.5)+1):
        if spf[i]==i:
            for j in range(i*i, mxn, i):
                if spf[j]==j: spf[j]=i
def solve2(n,m,k):
    sieve()
    primes = [2,3,5,7]
    nonPrimes =[1,4,6,8,9]
    from functools import lru_cache
    @lru_cache(None)
    def rec(i, rem):
        if i>n: return rem==k
        res = 0
        if spf[i]==i and i!=1:
            for prime in primes:
                res+=rec(i+1, (rem*10%m+prime)%m)
        else:
            for nonPrime in nonPrimes:
                res+=rec(i+1, (rem*10%m+nonPrime)%m)
        return res
    return rec(1,0)
print(solve2(2,2,0))



