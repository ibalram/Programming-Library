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


for _ in range(int(input())):
    n,k = imap()
    a = ilist()
    a.sort()
    q = deque()
    q2 = deque()
    res = float("inf")
    for i in range(n):
        while q and q[0]<i-k+1:
            q.popleft()
        while q and a[q[-1]]<=a[i]:
            q.pop()
        q.append(i)
        while q2 and q2[0]<i-k+1:
            q2.popleft()
        while q2 and a[q2[-1]]>=a[i]:
            q2.pop()
        q2.append(i)

        if i>=k-1:
            res = min(res, a[q[0]]-a[q2[0]])
            # print(res,end=" ")
    print(res)


