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
    w,h,n = map(int,input().split())
    cnt1 = cnt2 = 1
    while w%2==0:
        w//=2
        cnt1*=2
    while h%2==0:
        h//=2
        # cnt2+=1
        cnt1*=2
    # cnt = cnt1*cnt2+1
    cnt = cnt1
    print("No" if cnt<n else "Yes")
