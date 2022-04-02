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
    a = list(sorted(list(map(int,input().split())), reverse = True))
    b = list(sorted(list(map(int,input().split())), reverse = True))
    for i in range(1,n):
        a[i]+=a[i-1]
        b[i]+=b[i-1]
    a = [0]+a
    b = [0]+b
    l = 0
    r = 10**12
    def check(mid):
        x = n+mid
        x = x-x//4
        you = 100*mid + a[x-mid]
        ill = b[min(n,x)]
        return you>=ill
    for i in range(50*n+1):
        if check(i):
            print(i)
            break


