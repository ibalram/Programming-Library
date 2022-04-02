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

def calc(a):
    cnt = 0
    for i in range(1,len(a)-1):
        if a[i-1]<a[i]>a[i+1] or a[i-1]>a[i]<a[i+1]:
            cnt+=1
    return cnt

def brute(n,a):
    res = calc(a)
    for i in range(1,n-1):
        res = min(res, calc(a[:i]+[a[i-1]]+a[i+1:]))
        res = min(res, calc(a[:i]+[a[i+1]]+a[i+1:]))
    return res
def mine(n,a):
    cnt = 0
    f = 0
    b = [0]*(n+1)
    for i in range(1,n-1):
        if a[i-1]<a[i]>a[i+1] or a[i-1]>a[i]<a[i+1]:
            cnt+=1
            b[i] = 1
    for i in range(1,n-1):
        if b[i]:
            sm = b[i-1]+b[i]+b[i+1]
            if sm==3:
                f = max(f,sm)
            elif sm==2:
                if a[i+1]:
                    f = max(f, sm-(i>1 and (a[i]<a[i+1]<a[i-1] or a[i]>a[i+1]>a[i-1])))
                else:
                    f = max(f, sm-(i<n-1 and (a[i]<a[i-1]<a[i+1] or a[i]>a[i-1]>a[i+1])))
                # f = max(f, sm)
                # f = max(f,min(3,b[i-1]+b[i]+b[i+1]))
            else:
                f = max(sm,f)
    if n>2 and (a[1] or a[-2]): f = max(1,f)
    # print(max(0,cnt-f))
    # print(f)
    return max(0,cnt-f)


# from random import *
# tt = 0
# while tt<100:
#     n = randint(1,5)
#     a = [randint(1,10) for i in range(n)]
#     x = brute(n,a)
#     y = mine(n,a)
#     if x!=y:
#         print(n)
#         print(*a)
#         break


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(mine(n,a), brute(n,a))

# -(a[i-1]!=a[i+1] and i>1 and i<n-1)
