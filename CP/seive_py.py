import os, sys, bisect
from collections import defaultdict, Counter, deque;
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
input = lambda: sys.stdin.readline().strip()
imap = lambda: map(int,input().split()); ilist = lambda: list(imap())
#------------------------------------------------------------------
#sys.setrecursionlimit(10**6)
mod = int(1e9+7)


from time import time
mxn =5000000


def sieve_fast(mxn):
    global ftime
    st = time()
    spf= list(range(mxn))
    spf[0] = 1
    for i in range(2,mxn,2): spf[i] = 2
    for i in range(3, int(mxn**.5)+1, 2):
        if spf[i]!=i: continue
        for j in range(i*i, mxn, i):
            if spf[j]==j: spf[j] = i
    ftime+=time()-st
    return spf
def sieve_slow(mxn):
    global stime
    st = time()
    spf2= list(range(mxn))
    spf2[0] = 1
    for i in range(2,mxn,2): spf2[i] = 2
    for i in range(3, int(mxn**.5)+1):
        if spf2[i]!=i: continue
        for j in range(i*i, mxn, i):
            if spf2[j]==j: spf2[j] = i
    stime+=time()-st
    return spf2

n = 1
stime = 0
ftime = 0
for i in range(n):
    fast = sieve_fast(mxn)
    slow = sieve_slow(mxn)
    f = fast==slow
    if not f:
        print(f)
print(stime, ftime)
