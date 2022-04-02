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

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    res = "YES"
    n = int(input())
    a = list(map(int,input().split()))
    mul = 1
    for i in range(n):
        mul*=i+2
        if mul>10000000000:
            break
        if mul<=a[i] and a[i]%mul==0:
            res = "NO"
    print(res)
