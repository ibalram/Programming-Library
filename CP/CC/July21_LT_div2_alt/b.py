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
    b = list(map(int,input().split()))
    for i in range(n):
        a[i]%=n
        b[i]%=n
    c = [0]*n
    # mpa = defaultdict(int)
    # mpb = defaultdict(int)
    # for i in range(n):
    #     mpa[a[i]] = i
    #     mpb[b[i]] = i
    if len(set(b))==1:
        for i in range(n):
            c[i] = (a[i]+b[i])%n
        print(*c)
        continue
    cnt = 1
    # prev = 0
    # d = []
    # for i in range(1,n):
    #     if b[i]==b[i-1]:
    #         cnt+=1
    #     else:
    #         d.append([b[prev], prev, cnt])
    #         cnt = 1
    #         prev = i
    # if cnt:
    #     d.append([a[prev], prev, cnt])
    # pivot = -1
    mn = n+1
    ids = []
    # for val, idx, cnt in d:
    for idx, val in enumerate(b):
        if (a[0]+val)%n<mn:
            ids = [idx]
            mn = (a[0]+val)%n
        elif (a[0]+val)%n==mn:
            ids.append(idx)
    res = [n+1]*n
    for st in ids:
        x = [(b[(i+st)%n]+a[i])%n for i in range(n)]
        if x<res:
            res = x
    print(*res)





