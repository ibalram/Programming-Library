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
    res = []
    inc = [i for i in range(10)]
    # dec = inc[::-1]+[0]
    f = 0
    i = 0
    # while i<n:
    #     if f==0:
    #         j = 0
    #         while i<n and j<10:
    #             res.append(str(dec[j]))
    #             j+=1
    #             i+=1
    #         # if n-i<9:
    #         #     f = 1
    #     # else:
    #     #     j = 0
    #     #     while i<n and j<9:
    #     #         res.append(str(inc[j]))
    #     #         j+=1
    #     #         i+=1
    #     # # f^=1
    res = ["9", "8", "9"]
    x = max(0,n-3)
    res = res+[str(inc[i%10]) for i in range(x)]
    print("".join(res[:n]))
