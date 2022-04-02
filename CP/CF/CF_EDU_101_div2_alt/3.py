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
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    a = [i for i in range(0,(n+1)//2*(k-1), k-1)]
    x = [i+h[0] for i in a[:n//2]]
    y = [i+h[-1] for i in a[:n//2]][::-1]
    if n%2:
        if h[-1]<h[0]:
            b = x+[a[n//2]+h[-1]]+y
        else:
            b = x+[a[n//2]+h[0]]+y
    else:
        b = x+y
    f = "YES"
    for i in range(n):
        if b[i]<h[i]:
            f = "NO"
            break
    print(f)






