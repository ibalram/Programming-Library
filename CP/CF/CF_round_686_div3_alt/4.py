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

from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    primes = []
    x = n
    for i in range(2, int(n**.5)+1):
        if x<i: break
        if x%i==0:
            cnt = 0
            while x%i==0:
                cnt+=1
                x//=i
            primes.append([i,cnt])
    if x>=2:
        primes.append([x,1])
    # print(*primes)
    res = []
    for prime,cnt in primes:
        if len(res)<cnt:
            res+=[1]*(cnt-len(res))
        for i in range(cnt):
            res[i]*=prime
    print(len(res))
    print(*res[::-1])
