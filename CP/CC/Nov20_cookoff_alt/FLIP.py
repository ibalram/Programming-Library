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
    a = list(input().strip())
    b = list(input().strip())
    n = len(a)
    x = [int(a[i])^int(b[i]) for i in range(0,n,2)]
    y = [int(a[i])^int(b[i]) for i in range(1,n,2)]
    cnt = 0
    res = 0
    for i in range(len(x)):
        if x[i]:
            cnt+=1
        else:
            if cnt: res+=1
            cnt = 0
    if cnt:res+=1
    cnt = 0
    for i in range(len(y)):
        if y[i]:
            cnt+=1
        else:
            if cnt: res+=1
            cnt = 0
    if cnt:res+=1
    print(res)

    # prev = a[i]!=b[i]
    # cnt = 0
    # for i in range(2,n,2):
    #     cur = a[i]!=b[i]
    #     if cur and cur==prev:

