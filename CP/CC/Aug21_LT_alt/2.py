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
    w = list(map(int,input().split()))
    mn = min(w)
    w = [i-mn for i in w]
    a = [w[i]-i for i in range(n)]
    a.sort()
    # marked = [0]*(n+1)
    # print(*a)
    if len(set(a))==1:
        print(len(a))
    else:
        print(1)

