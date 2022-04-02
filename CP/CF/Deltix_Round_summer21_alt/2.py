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

# wrong
for _ in range(int(input())):
    n = int(input())
    a = [i&1 for i in list(map(int,input().split()))]
    odd = a.count(1)
    even = n-odd
    if min(even,odd)!=n//2:
        print(-1)
        continue
    x = []
    for i in range(n//2):
        x+=[0,1]
    if n&1:
        if even>odd:
            x = x+[0]
        else:
            x = [1]+x
    def solve(b):
        idx = []
        for i in range(n):
            if a[i]!=b[i]:
                idx.append(i)
        res = 0
        for i in range(1,len(idx),2):
            res+=idx[i]-idx[i-1]
        return res
    print(min(solve(x), solve(x[::-1])))
    # print(a)
    # print(x)
    # x = sum(1 if a[i]!=a[i-1] for i in range(1,n))
    # print(x-1 if )


"""
0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1



1 1 1 0 1 0

"""
