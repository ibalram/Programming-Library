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

n = int(input())
a = ilist()

mod = 998244353
fac = [1]*(n+1)
ifac = [1]*(n+1)
for i in range(2,n+1):
    fac[i] = fac[i-1]*i%mod
ifac[n] = pow(fac[n], mod-2, mod)
for i in range(n-1,0,-1):
    ifac[i] = (i+1)*ifac[i+1]%mod
ncr = lambda n,r: fac[n]*ifac[r]%mod*ifac[n-r]%mod

def conv(a, b):
    n = len(a)
    m = len(b)
    c = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            c[i+j]+=A[i]*B[j]
    return c

bits = [0]*31
for i in a:
    for j in range(31):
        bits[j]+=i>>j&1

polynomials = []
for i in range(31):
    ones = bits[i]
    zeros = n-ones
    A = [ncr(ones,j) if j%2 else 0 for j in range(ones+1)]
    B = [ncr(zeros,j) for j in range(zeros+1)]
    polynomials.append(conv(A,B)[:n+1])
    print(A,B,polynomials[i])

ans = [0]
for i in range(1,n+1):
    ans.append(ans[i-1])
    for j in range(31):
        ans[i] = (ans[i]+(1<<j)*polynomials[j][i]%mod)%mod

q = int(input())
for _ in range(q):
    print(ans[int(input())])
