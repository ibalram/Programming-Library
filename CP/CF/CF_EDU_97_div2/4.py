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
    a = list(map(int,input().split()))
    a = a[1:]
    res = 1
    pf = [1]
    cnt = 1
    for i in range(1,n-1):
        if a[i]<=a[i-1]:
            res+=1
            pf.append(cnt)
            cnt = 1
        else:
            cnt+=1
    pf.append(cnt)
    print(pf)
    print(res)
