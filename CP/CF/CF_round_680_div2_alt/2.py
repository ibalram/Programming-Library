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
# mod = int(1e9+7)
# s =0
#     # n,m = map(int,input().split())
#     # a = list(map(int,input().split()))

for _ in range(int(input())):
    a,b = map(int,input().split())
    s = list(map(int,list(input().strip())))
    n = len(s)
    cnt0 = 0
    cnt1 = 0
    l = 0
    while l<n and s[l]==0:
        l+=1
    r = n-1
    while r>=0 and s[r]==0:
        r-=1
    x = a//b
    res = 0
    for i in range(l,r+1,1):
        if s[i]==0:
            cnt0+=1
        else:
            if cnt0:
                if cnt0<=x:
                    res+=cnt0*b
                else:
                    res+=a
            cnt0 = 0
    if cnt0:
        if cnt0<=x:
            res+=cnt0*b
        else:
            res+=a
    if l<=r:res+=a
    print(res)




