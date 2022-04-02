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
    if (n*(n-1)//2 )%2:
        print("NO")
        continue
    n//=2
    al = list(range(1,2*n+1))
    a = []
    b = []
    for i in range(0,n,2):
        a+=[al[i],al[~i]]
        b+=[al[i+1],al[~(i+1)]]
    print("YES")
    a.sort()
    b.sort()
    print(*a)
    print(*b)
    for i in range(1,n):
        a[i]+=a[i-1]
        b[i]+=b[i-1]
    print(*a)
    print(*b)
