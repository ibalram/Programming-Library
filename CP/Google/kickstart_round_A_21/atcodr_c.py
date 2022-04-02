

from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
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
primes = list(range(2,30))#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
a = [0]*(n+1)
if n<=2:
    print(*list(range(1,n+1)))
else:
    # a = [1,2]
    # for i in range(3,n+1):
    #     for j in primes:
    #         if i%j:
    #             a.append(j)
    #             break
    # if
    a = [0]*(n+2)
    b = [0]*(n+2)
    cntr = 2
    for i in range(2,n+1):
        if b[i]!=0:
            cntr = abs(b[j])+1
        a[i]+=cntr
        a[n+1]-=cntr
        for j in range(2*i,n+1,i):
            b[j]-=cntr
        # cntr+=1
    print(*a[1:])
    a[1] = 1
    for i in range(2,n+1):
        a[i]+=a[i-1]
        a[i-1]+=b[i-1]
    a[n]+=b[n]

    print(*a[1:])
    # print(*list(range(1,n+1x)))
