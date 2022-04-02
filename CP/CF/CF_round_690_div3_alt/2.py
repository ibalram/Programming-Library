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

import collections
for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    if "2020" in [a[:4], a[n-4:]]:
        print("YES")
    else:
        st = "2020"
        res = "NO"
        for i in range(1,4):
            one = st[:i]
            two = st[i:]
            if st[:i]==a[:i] and st[i:]==a[n-4+i:]:
                res = "YES"
                break
        print(res)


