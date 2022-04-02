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
    n,m = map(int,input().split())
    a = [["0"]*(m) for i in range(n)]
    cnt = 0
    for i in range(m):
        if cnt%2==0:
            a[0][i] = "1"
        cnt+=1
    for i in range(1 if cnt%2 else 2,n):
        if cnt%2==0:
            a[i][m-1] = "1"
        cnt+=1
    for i in range(m-2 if cnt%2 else m-3,-1,-1):
        if cnt%2==0:
            a[n-1][i] = "1"
        cnt+=1
    for i in range(n-2 if cnt%2 else n-3,1 if 2*(n+m-2)%2==0 else 0,-1):
        if cnt%2==0:
            a[i][0] = "1"
        cnt+=1
    for i in a:
        print("".join(i))
    print()
