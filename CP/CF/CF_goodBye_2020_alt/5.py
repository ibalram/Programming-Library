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
import os, sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

def calc(a):
    res = 0
    for i in a:
        for j in a:
            for k in a:
                res+=(i&j)*(j|k)
                res%=mod
    print(res)
    return res

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    w = [0]*(61)
    for i in a:
        for j in range(61):
            if (i>>j)&1:
                w[j]+=1
    res = 0
    for i in a:
        x = y = 0
        for j in range(61):
            tmp = 1<<j
            if (i>>j)&1:
                x = (x+tmp*n)%mod
                y = (y+tmp*w[j])%mod
            else:
                x =(x+tmp*w[j])%mod
        res  = (res+x*y)%mod
    # print(w)
    # calc(a)
    print(res)
