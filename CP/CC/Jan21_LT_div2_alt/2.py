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
    s = [int(i) for i in input().strip()]
    if s.count(1)==0:
        print(0)
        continue
    cnt0 =[i^1 for i in s]
    cnt1 = s[:]
    res = n
    for i in range(1,n):
        cnt0[i]+=cnt0[i-1]
        cnt1[i]+=cnt1[i-1]
    cnt0 = [0]+cnt0
    cnt1 = [0]+cnt1
    for i in range(n+1):
        res = min(res, n-(cnt0[i]+cnt1[n]-cnt1[i]))
    print(res)
    # idx = s.index("1")
    # print(s[idx:].count("0"))

