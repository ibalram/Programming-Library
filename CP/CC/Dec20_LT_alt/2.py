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


import os, sys, bisect
input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    b = input().strip()
    if a.count("1")!=b.count("1"):
        print("No")
        continue
    else:
        z1 = 0
        z2 = 0
        res = "Yes"
        for i in range(n):
            z1+=a[i]=="0"
            z2+=b[i]=="0"
            if z2<z1:
                res ="No"
                break
        print(res)
