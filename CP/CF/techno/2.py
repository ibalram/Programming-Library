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
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    diff = []
    for i in range(1,n):
        diff.append(a[i]-a[i-1])
    if not diff:
        print(0)
        continue
    c = max(diff)
    mindiff = min(diff)
    if any(i!=c and i!=mindiff for i in diff):
        print(-1)
        continue
    diff = [i-mindiff for i in diff]
    mx = max(diff)
    if mx==0:
        print(0)
    elif mx<=max(a):
        print(-1)
    else:
        print(mx,c)
